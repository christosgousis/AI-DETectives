from bs4 import BeautifulSoup
import requests

url = 'https://www.kathimerini.gr/search/nova%20united%20group/'
page = requests.get(url)

extract = BeautifulSoup(page.text, 'html')

print(extract)