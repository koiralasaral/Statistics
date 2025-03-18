import requests
import json
import datetime
import time
import os

def get_news():
       url = 'https://newsapi.org/v2/everything?q=Apple&from=2025-03-16&sortBy=popularity&apiKey=05fe779a5de443e0b6a9bf0fc338085d'
       response = requests.get(url)
       return response.json()

def main():
       while True:
              data = get_news()


              for i in range(0, 10):
                     print(data['Articles'][i]['title'])              #print the title of the news
                     print(data['Articles'][i]['description'])
                     print(data['Articles'][i]['url'])               #print the url of the news
                     print(data['Articles'][i]['publishedAt'])
                     print(data['Articles'][i]['content'])
                     print('-----------------------------------')
              time.sleep(10)
              os.system('cls')

if __name__ == '__main__':
       main()

              