import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict
import csv

# Scraper Functions

visited = set()
site_map = defaultdict(list)

def clean_url(base, link):
    try:
        full_url = urljoin(base, link)
        if urlparse(full_url).netloc == urlparse(base).netloc:
            return full_url.split("#")[0]
    except:
        return None

def scrape_site(url):
    visited.clear()
    content_data = {}

    def crawl(current_url):
        if current_url in visited:
            return
        try:
            res = requests.get(current_url, timeout=8)
            if res.status_code != 200:
                return
            soup = BeautifulSoup(res.text, 'html.parser')
            visited.add(current_url)

            headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]
            paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
            links = [clean_url(current_url, a['href']) for a in soup.find_all('a', href=True)]
            links = list(filter(None, links))

            site_map[current_url] = links
            content_data[current_url] = {
                "headings": headings[:3],
                "paragraphs": paragraphs[:3],
                "links": links[:3]
            }

            for link in links:
                crawl(link)

        except Exception as e:
            print(f"Error while scraping {current_url}: {e}")
            pass

    crawl(url)
    return content_data

def generate_csv_report(content_data, filename="webscraper_report.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        header = ['URL', 'Heading 1', 'Heading 2', 'Heading 3',
                  'Paragraph 1', 'Paragraph 2', 'Paragraph 3',
                  'Link 1', 'Link 2', 'Link 3']
        writer.writerow(header)

        for url, data in content_data.items():
            row = [url]
            row += data['headings'] + [''] * (3 - len(data['headings']))
            row += data['paragraphs'] + [''] * (3 - len(data['paragraphs']))
            row += data['links'] + [''] * (3 - len(data['links']))
            writer.writerow(row)
    return filename

# Streamlit UI

st.set_page_config(page_title="SiteSketcher CSV", layout="wide")
st.title("🔍 Website Scraper (CSV Report)")
st.markdown("Scrape a website and export the content as a **CSV file** (headings, paragraphs, links).")

url = st.text_input("🔗 Enter Website URL", "https://example.com")

if st.button("Scrape and Generate CSV Report"):
    with st.spinner("Scraping site... please wait"):
        data = scrape_site(url)
        if data:
            filename = generate_csv_report(data)
            with open(filename, "rb") as f:
                st.success("CSV report generated successfully!")
                st.download_button(
                    label="📥 Download Report (.csv)",
                    data=f,
                    file_name=filename,
                    mime="text/csv"
                )
        else:
            st.warning("No content could be extracted from this site.")
