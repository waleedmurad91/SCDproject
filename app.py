import streamlit as st
import requests
from bs4 import BeautifulSoup

# Define the base URL
BASE_URL = "https://quotes.toscrape.com/"

# Function to scrape the website
def scrape_quotes():
    # Send a GET request to the website
    response = requests.get(BASE_URL)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all quote elements on the page
    quote_elements = soup.find_all("div", class_="quote")

    # Extract the data from each quote element
    quotes_data = []
    for quote_element in quote_elements:
        text = quote_element.find("span", class_="text").get_text()
        author = quote_element.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote_element.find_all("a", class_="tag")]
        toptags = [tag.get_text() for tag in quote_element.find_all("a", class_="tag")]

        quotes_data.append({
            "text": text,
            "author": author,
            "tags": tags,
            "toptags": top ten tags
        })

    return quotes_data

# Create a Streamlit web interface
def main():
    st.title("Quotes Scraper")
    st.write("Scraping quotes from https://quotes.toscrape.com/")

    # Scrape the website
    quotes = scrape_quotes()

    # Display the scraped quotes
    for quote in quotes:
        st.write("---")
        st.write(f"Text: {quote['text']}")
        st.write(f"Author: {quote['author']}")
        st.write(f"Tags: {', '.join(quote['tags'])}")

if __name__ == "__main__":
    main()
