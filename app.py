import streamlit as st
import requests
from bs4 import BeautifulSoup
from collections import Counter

# Define the base URL
BASE_URL = "https://quotes.toscrape.com/"

# Function to scrape the website
def scrape_quotes():
    # Send a GET request to the first page
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the total number of pages
    num_pages = len(soup.select(".pager a"))

    # Scrape quotes from each page
    quotes_data = []
    tags_data = []
    for page in range(1, num_pages + 1):
        url = f"{BASE_URL}page/{page}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all quote elements on the page
        quote_elements = soup.find_all("div", class_="quote")

        # Extract the data from each quote element
        for quote_element in quote_elements:
            text = quote_element.find("span", class_="text").get_text()
            author = quote_element.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in quote_element.find_all("a", class_="tag")]
            quotes_data.append({
                "text": text,
                "author": author,
                "tags": tags,
            })
            tags_data.extend(tags)

    top_tags = Counter(tags_data).most_common(10)
    return quotes_data, top_tags

# Create a Streamlit web interface
def main():
    st.title("Quotes Scraper")
    st.write("Scraping quotes from https://quotes.toscrape.com/")

    # Scrape the website
    quotes, top_tags = scrape_quotes()

    # Display the scraped quotes
    for quote in quotes:
        st.write("---")
        st.write(f"Text: {quote['text']}")
        st.write(f"Author: {quote['author']}")
        st.write(f"Tags: {', '.join(quote['tags'])}")

    # Display the overall top tags in the sidebar
    st.sidebar.title("Overall Top Tags")
    for tag, count in top_tags:
        st.sidebar.write(f"{tag}: {count}")

if __name__ == "__main__":
    main()
