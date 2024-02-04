import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from bs4 import BeautifulSoup
import requests
import os
import urllib.parse
import urllib.request

def download_image(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        img_name = os.path.basename(urllib.parse.urlsplit(url).path)
        img_path = os.path.join(folder, img_name)
        with open(img_path, 'wb') as img_file:
            img_file.write(response.content)
        return img_path
    else:
        return None

def scrape_images(url, folder='output'):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Create output folder if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

        images = [img['src'] for img in soup.find_all('img') if img.get('src')]

        # Download images
        downloaded_images = []
        for img_url in images:
            img_path = download_image(img_url, folder)
            if img_path:
                downloaded_images.append(img_path)

        return downloaded_images
    else:
        return []

def on_scrape_button_click():
    url = url_entry.get()
    downloaded_images = scrape_images(url)
    
    # Display the downloaded image paths in the scrolled text widget
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.INSERT, "Downloaded Images:\n")
    for img_path in downloaded_images:
        result_text.insert(tk.INSERT, img_path + "\n")
    result_text.config(state=tk.DISABLED)

# Create a Tkinter UI
root = tk.Tk()
root.title("Image Scraper UI")

# URL Entry
url_label = ttk.Label(root, text="Enter URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

url_entry = ttk.Entry(root, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Scrape Button
scrape_button = ttk.Button(root, text="Scrape Images", command=on_scrape_button_click)
scrape_button.grid(row=1, column=0, columnspan=2, pady=10)

# Result Text
result_text = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
