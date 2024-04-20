from bs4 import BeautifulSoup
import requests

url = 'https://www.kathimerini.gr/search/nova%20united%20group/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
links = soup.find_all('a', href=True)

article_urls = []
for link in links:
    # Check if the link points to an article based on its URL pattern
    if 'pages/announcements/' in link['href']:
        article_urls.append(link['href'])

article_urls = list(set(article_urls))
print(article_urls)
