import requests as req
import sys


def get_news(category, number, output, verbose):
    url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey05f="e779a5de443e0b6a9bf0fc338085d"'
    try:
        response = req.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except req.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        data = response.json()
        articles = data.get('articles', [])
    except ValueError:
        print("Error: Unable to parse JSON response")
        sys.exit(1)

    if not articles:
        print("No articles found.")
        return
print(get_news('politics', 5, 'output.txt', True)) # This will print the news articles from the BBC News API
# Compare this snippet from getting_news1.py:   