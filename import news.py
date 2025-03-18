from newsapi import NewsApiClient
import json
import requests
import os
import sys
import time
import datetime
import re
import random
import string
import urllib
api = NewsApiClient(api_key='05fe779a5de443e0b6a9bf0fc338085d')
def get_news():
    news = api.get_top_headlines(sources='bbc-news')
    return news
def get_news_by_category(category):
    news = api.get_top_headlines(category=category)
    return news
def get_news_by_country(country):
    news = api.get_top_headlines(country=country)
    return news
def get_news_by_source(source):
    news = api.get_top_headlines(sources=source)
    return news
def get_news_by_query(query):
    news = api.get_top_headlines(q=query)
    return news
print(get_news())
print('\n')
print(get_news_by_category('politics'))
print("\n") 
print("\n")
print(get_news_by_country('nepal'))
print("\n")
print(get_news_by_source('the-guardian-uk'))   
print("\n")
print("\n")
print(get_news_by_query(''))
#  Print empty line
print('\n')
#  Print empty line
# Compare this snippet from getting_news1.py:
# import requests
# import json
# import datetime
# import time
# import os
#
# def get_news():

#        url = 'https://newsapi.org/v2/everything?q=Apple&from=2025-03-16&sortBy=popularity&apiKey="
#        response = requests.get(url)

#        return response.json()
# Compare this snippet from getting_news1.py:
# import requests
# import json
# import datetime

# import time
# import os

# def get_news():
#        url = 'https://newsapi.org/v2/everything?q=Apple&from=2025-03-16&sortBy=popularity&apiKey="
#        response = requests.get(url)

#        return response.json()
# Compare this snippet from getting_news1.py:
# import requests
# import json
# import datetime
# import time
# import os


def get_news2():
        url = '"https://newsapi.org/v2/everything?q=Apple&from=2025-03-16&sortBy=popularity&apiKey="'
        response = requests.get(url)
        return response.json()
print(get_news2())
print("\n")
print("\n")

# def main():
#        while True:


#               data = get_news()
# Compare this snippet from getting_news1.py:

def get_news1():
    url = 'https://newsapi.org/v2/everything?q=Nepal&from=2025-03-16&sortBy=popularity&apiKey="05fe779a5de443e0b6a9bf0fc338085d"'   #url to get the news
    response = requests.get(url)
    return response.json()
def main():
    while True:
        data = get_news1()   #get the news
        for i in range(0, 10):
            print(data['articles'][i]['title'])              #print the title of the news
            print(data['articles'][i]['description'])
            print(data['articles'][i]['url'])               #print the url of the news   
            print(data['articles'][i]['publishedAt'])
            print(data['articles'][i]['content'])                                 
            print('-----------------------------------')
        time.sleep(10)


print(get_news1())
# Compare this snippet from request.py:
# 'This program is a simple example of a Python program that uses the requests library to make a GET request to a web server.'
# import requests # Import the requests library
#
# response = requests.get('http://www.google.com') # Make a GET request to the Google home page
# print(response.text) # Print the response from the server
#
# # This program will print the HTML of the Google home page to the console.
# # To run this program, you will need to have the requests library installed.

# You can install it with the following command:
# pip install requests
# Then you can run the program with the following command:
# python3 requests_example.py
# You should see the HTML of the Google home page printed to the console.
# If you want to save the HTML to a file, you can redirect the output to a file like this:
# python3 requests_example.py > google.html
# This will save the HTML to a file named google.html in the current directory.
# You can then open the file in a web browser to view the HTML.
# This program is a simple example of how you can use the requests library to make HTTP requests in Python.

# You can use it to make GET requests to any web server that supports HTTP.
# You can also make POST requests, PUT requests, DELETE requests, and more.
# The requests library makes it easy to work with HTTP in Python.
# You can use it to interact with web APIs, scrape web pages, and more.
# For more information on the requests library, see the official documentation:
# https://docs.python-requests.org/en/master/
# For more information on HTTP, see the HTTP/1.1 specification:
# https://tools.ietf.org/html/rfc2616
# For more information on web servers, see the Apache HTTP Server documentation:
# https://httpd.apache.org/docs/2.4/
# For more information on web development, see the Mozilla Developer Network (MDN) documentation:
# https://developer.mozilla.org/en-US/docs/Web
# For more information on Python, see the official Python documentation:
# https://docs.python.org/3/
# For more information on programming in general, see the Stack Overflow website:
# https://stackoverflow.com/
# I hope this information is helpful! Good luck!
#
# Compare this snippet from request.py:
# 'This program is a simple example of a Python program that uses the requests library to make a GET request to a web server.'
# import requests # Import the requests library
#
# response = requests.get('http://www.google.com') # Make a GET request to the Google home page
# print(response.text) # Print the response from the server
# Compare this snippet from request.py:
# 'This program is a simple example of a Python program that uses the requests library to make a GET request to a web server.'