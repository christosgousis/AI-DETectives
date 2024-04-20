import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    # URL of the article
    url = "https://www.kathimerini.gr/pages/announcements/562934515/i-nova-anaptyssei-to-proto-ict-ergo-exypno-dasos/"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all <p> tags with text
        p_tags_with_text = soup.find_all("p")

        # Extract the text content of each <p> tag
        for p_tag in p_tags_with_text:
            print(p_tag.get_text())
    else:
        print("Failed to retrieve the webpage.")
