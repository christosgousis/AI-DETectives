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
        
        # Find all paragraphs with the specified class
        relevant_paragraphs = soup.find_all('p', class_='subtitle is-7 mb-3')
        
        # Extract the links beneath the relevant paragraphs
        for paragraph in relevant_paragraphs:
            # Find the parent element of the paragraph
            parent_div = paragraph.find_parent('div')
            
            # Find all links within the parent element
            links = parent_div.find_all('a', href=True)
            
            # Extract the URLs from the links
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

# Remove duplicates from the list of article URLs
article_urls = list(set(article_urls))
num_urls = len(article_urls)

print("Number of unique article URLs:", num_urls)
