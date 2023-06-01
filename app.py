import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape car listings from PakWheels
def scrape_pakwheels():
    url = "https://www.pakwheels.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract car listings from the website
    listings = soup.find_all('li', class_='classified-listing')
    data = []
    for listing in listings:
        title = listing.find('h3', class_='title').text.strip()
        price = listing.find('span', class_='price').text.strip()
        data.append({'Title': title, 'Price': price})
    
    return data

# Streamlit app code
def main():
    st.title("PakWheels Car Listings Scraper")
    st.write("Click the button to scrape car listings from PakWheels:")
    
    if st.button("Scrape"):
        try:
            data = scrape_pakwheels()
            st.write("Scraped car listings:")
            for listing in data:
                st.write(f"Title: {listing['Title']}, Price: {listing['Price']}")
        except:
            st.write("An error occurred while scraping data. Please try again.")

if __name__ == "__main__":
    main()

