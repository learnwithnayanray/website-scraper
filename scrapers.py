import requests
from bs4 import BeautifulSoup
import csv

def scrape_and_save_to_csv(url, csv_filename='scraped_data.csv'):
    # Make a GET request to the website
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the HTML using BeautifulSoup methods
        links = soup.find_all('a')
        paragraphs = soup.find_all('p')

        # Write data to CSV file
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Link', 'Paragraph'])  # Header

            for link, paragraph in zip(links, paragraphs):
                csv_writer.writerow([link.get('href'), paragraph.get_text()])
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Example usage
url_to_scrape = 'https://stackoverflow.com/questions/tagged/css'
csv_filename = 'scraped_data.csv'
scrape_and_save_to_csv(url_to_scrape, csv_filename)
