from bs4 import BeautifulSoup
import requests

def scrape_article(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all <p> tags with text
        p_tags_with_text = soup.find_all("p")

        # Extract the text content of each <p> tag
        article_text = ""
        for p_tag in p_tags_with_text:
            article_text += p_tag.get_text() + "\n"

        return article_text
    else:
        print(f"Failed to retrieve the webpage at {url}")
        return None

def search_urls():
    keywords = input("Enter keywords separated for search: ").split()

    base_url = 'https://www.kathimerini.gr/search/' + '%20'.join(keywords) + '/'
    article_urls = []

    # Iterate through each page of search results
    page_number = 1
    while True:
        url = base_url + 'page/' + str(page_number) + '/'
        
        page = requests.get(url)
        
        # Check if the page exists
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
        
            relevant_paragraphs = soup.find_all('p', class_='subtitle is-7 mb-3')
            
            # Extract the links beneath the relevant paragraphs
            for paragraph in relevant_paragraphs:
                parent_div = paragraph.find_parent('div')            
                links = parent_div.find_all('a', href=True)
                
                # Extract the URLs from the links
                for link in links:
                    href = link['href']
                    if 'kathimerini.gr/' in href:
                        article_urls.append(href)
            
            # Move to the next page
            page_number += 1
        else:
            break

    article_urls = list(set(article_urls))

    # Loop through each URL and scrape the article text
    for url in article_urls:
        article_text = scrape_article(url)
        if article_text:
            print(article_text)

search_urls()