from bs4 import BeautifulSoup
import requests

base_url = 'https://www.kathimerini.gr/search/nova%20united%20group/'
article_urls = []

# Iterate through each page of search results
page_number = 1
while True:
    url = base_url + 'page/' + str(page_number) + '/'
    
    page = requests.get(url)
    
    # Check if the page exists
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Find the container element that holds the search result links
        result_container = soup.find('div', class_='columns is-max-900 is-flex-wrap-wrap')
        
        # Check if the container element exists
        if result_container:
            # Find all links (a tags) within the container
            links = result_container.find_all('a', href=True)

            # Extract the URLs from the links that point to the articles
            for link in links:
                href = link['href']
                # Check if the URL contains 'kathimerini.gr/' and is not a category link
                if 'kathimerini.gr/' in href:
                    article_urls.append(href)
        
        # Move to the next page
        page_number += 1
    else:
        # Break the loop if the page is not found (i.e., no more pages available)
        break

article_urls = list(set(article_urls))
num_urls = len(article_urls)

print("Number of unique article URLs:", num_urls)
