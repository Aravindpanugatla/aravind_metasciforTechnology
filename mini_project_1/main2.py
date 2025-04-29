import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def scrape_propertyonion():
    url = "https://propertyonion.com/property_search"
    driver = setup_driver()
    driver.get(url)

    time.sleep(10)  # Let the page load JavaScript

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    results = []
    listings = soup.select('.search-results .card')  # Adjust based on actual HTML

    for card in listings:
        title = card.select_one('.card-title')
        address = card.select_one('.property-address')
        price = card.select_one('.property-price')

        results.append({
            'Title': title.get_text(strip=True) if title else '',
            'Address': address.get_text(strip=True) if address else '',
            'Price': price.get_text(strip=True) if price else '',
        })

    return pd.DataFrame(results)

st.title("📊 PropertyOnion Scraper (CSV Export)")
st.write("Scrape property listings from propertyonion.com")

if st.button("Scrape Now"):
    with st.spinner("Scraping data from PropertyOnion..."):
        df = scrape_propertyonion()
        if not df.empty:
            csv_file = "propertyonion_output.csv"
            df.to_csv(csv_file, index=False)
            st.success("Scraping completed successfully!")
            st.download_button(
                label="📥 Download CSV",
                data=open(csv_file, "rb"),
                file_name=csv_file,
                mime="text/csv"
            )
        else:
            st.warning("No data found or failed to scrape.")
