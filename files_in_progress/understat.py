from bs4 import BeautifulSoup  # allows us to use the HTML and grab the data
import requests  # allows us to initially download the HTML
import pprint
import scrapy
import json

res = requests.get('https://understat.com/league/EPL')

soup = BeautifulSoup(res.text, 'html.parser')
pprint.pprint(soup.find_all('<script>'))

string = ''
value = string
print(value.encode('utf8').decode('unicode_escape'))


# class PostsSpider(scrapy.Spider):
#     name = 'posts'
#     start_urls = [
#         'https://understat.com/league/EPL/'
#     ]
#
#     def parse(self, response):
#         page = response.url.split('/')[-1]
#         filename = 'posts-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
