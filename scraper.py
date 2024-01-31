import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the HTML using BeautifulSoup methods
        # Example: Extract all the links on the page
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))

        # Example: Extract text from paragraphs
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            print(paragraph.get_text())
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Example usage
url_to_scrape = 'https://www.gogolis.com'
scrape_website(url_to_scrape)
