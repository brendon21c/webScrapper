from bs4 import BeautifulSoup
import requests
from datetime import *


# Single article
request = requests.get('https://arstechnica.com/science/2017/02/for-a-brighter-future-science-looks-to-re-energize-the-common-solar-cell/')

data = request.text

soup = BeautifulSoup(data, 'html.parser')

#print(soup.prettify())

# for link in soup.find_all('header'):
#      print(link.get('a'))

f = open('webScrape', 'w')

title = soup.find_all('title')
h2 = soup.find_all('h1')
titleFinal = h2[0].text

date = datetime.now()

f.write(titleFinal + "\n")
f.write(str(date) + "\n")
f.close()

print(title)
print(date)
