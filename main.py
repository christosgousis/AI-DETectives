import os
from bs4 import BeautifulSoup
import requests
import json
import cohere

def scrape_article(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the title of the article
        title_tag = soup.find("h1", class_="entry-title")
        title = title_tag.get_text() if title_tag else None

        # Find all <p> tags with text
        p_tags_with_text = soup.find_all("p")

        # Extract the text content of each <p> tag
        article_text = ""
        for p_tag in p_tags_with_text:
            article_text += p_tag.get_text() + "\n"

        return {"title": title, "text": article_text}
    else:
        print(f"Failed to retrieve the webpage at {url}")
        return None

def search_urls(keywords):
    if os.path.exists("articles.json"):
        os.remove("articles.json")
    

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

    # Write the JSON array to a file
    with open('articles.json', 'a') as f:
        f.write("[\n")
    # Loop through each URL and scrape the article text
    for url in article_urls:
        article_data = scrape_article(url)
        if article_data:
            # Append the article data to a JSON file
            with open("articles.json", "a", encoding="utf-8") as json_file:
                json.dump(article_data, json_file, ensure_ascii=False)
                
                if url == article_urls[-1]:
                    json_file.write("\n]")  # Add a newline after the last object
                else:
                    json_file.write(",\n")  # Add a newline to separate objects


def api_call_1(keywords):
    # Create a new Cohere client
    co = cohere.Client("SNUTZQkRHFkybeGNay7bwNftreTkYPjsExGIpRWm")
    # Open the JSON file
    with open('articles.json', 'r', encoding='utf-8') as articles:
        # Load the JSON data
        data = json.load(articles)

    response = co.chat(
        documents=data,
        message="Θέλουμε να παράξεις μία εκτενή και ιδιαίτερα λεπτομερή αναφορά (report) έως 600 λέξεις,"
           + " της οποίας η θεματολογία περιέχει τους ακόλουθους όρους: " + ' '.join(keywords) 
    )
    response_dict = json.loads(response.json())

    return response_dict

def api_call_2(text, department):
    # Create a new Cohere client
    co = cohere.Client("SNUTZQkRHFkybeGNay7bwNftreTkYPjsExGIpRWm")
    
    response = co.chat(
        message="Με βάση αυτό:" + ' '.join(text)+ ". Θεώρησε ότι είμαι ένας νέος εργαζόμενος της NOVA στο τμήμα  " + ' '.join(department)
        + " Με ποιον τρόπο θα μπορούσε το ανωτέρω report να αξιοποιηθεί από το τμήμα "+ ' '.join(department)  + "της Εταιρείας"
        + "και να παραχθεί ωφέλιμη, καινοτομική γνώση για την βελτίωση του Οργανισμού και την παραγωγή νέων ιδεών."
        + "Απαιτούμε αυτό το κείμενο να μην υπερβαίνει τις 300 λέξεις. Αν η γνώση δεν είναι ωφέλιμη, παρακαλώ μην υπερβάλλεις και να μην τυπώσεις τίποτα απολύτως."
    )
    response_dict = json.loads(response.json())

    return response_dict

def main():
    keywords = input("Enter keywords separated for search: ").split()
    department = input("Enter department for search: ").split()
    search_urls(keywords)
    api_response_1  = api_call_1(keywords)
    print("1h Apantisi: ")
    print(api_response_1["text"])
    api_response_2 = api_call_2(api_response_1["text"], department)
    print("2h Apantisi: ")
    print(api_response_2["text"])


main()
