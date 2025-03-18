import requests as req
import os
import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(description='Get the latest news from the BBC')
    parser.add_argument('-c', '--category', type=str, help='The category of news you want to see', default='')
    parser.add_argument('-n', '--number', type=int, help='The number of articles you want to see', default=5)
    parser.add_argument('-o', '--output', type=str, help='The output file to write to', default='')
    parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')
    args = parser.parse_args()
    return args

def get_news(category, number, output, verbose):
    # Retrieve API key securely
    api_key = os.getenv('NEWS_API_KEY', '05fe779a5de443e0b6a9bf0fc338085d')
    if api_key == 'YOUR_API_KEY':
        print("Error: Please set your NEWS_API_KEY in environment variables.")
        sys.exit(1)
    
    url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={"05fe779a5de443e0b6a9bf0fc338085d"}'
    
    try:
        response = req.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
    except req.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        data = response.json()
        articles = data.get('articles', [])
    except ValueError:
        print("Error: Unable to parse JSON response.")
        sys.exit(1)

    if not articles:
        print("No articles found.")
        return

    if verbose:
        print(f"Fetching data from URL: {url}")
        print(f"HTTP Status Code: {response.status_code}")

    if output:
        with open(output, 'w') as f:
            f.write('The latest news from the BBC\n')
            f.write('-----------------------------\n')

    for i, article in enumerate(articles[:number]):
        title = article.get('title', 'No Title')
        description = article.get('description', 'No Description')

        if category and category.lower() not in title.lower():
            continue
        
        if output:
            with open(output, 'a') as f:
                f.write(f"{title}\n{description}\n{'-'*30}\n")
        
        print(f"{title}\n{description}\n{'-'*30}")
    
    if output:
        print(f'The news has been written to {output}')

def main():
    args = get_args()
    get_news(args.category, args.number, args.output, args.verbose)

if __name__ == '__main__':
    main()

