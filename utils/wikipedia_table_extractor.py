import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from urllib.parse import urlparse, unquote
from io import StringIO
import re

def slugify(text):
    """Convert text to a valid filename."""
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[\s]+', '_', text.strip())

def extract_tables_from_wikipedia(url):
    # Extract article name from URL
    parsed_url = urlparse(url)
    article_name = os.path.basename(parsed_url.path)
    article_name = unquote(article_name)
    output_dir = slugify(article_name)
    os.makedirs(output_dir, exist_ok=True)

    # Fetch page content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all tables
    tables = soup.find_all("table", {"class": "wikitable"})

    for idx, table in enumerate(tables):
        # Attempt to get table caption
        caption_tag = table.find("caption")
        if caption_tag:
            table_name = caption_tag.get_text(strip=True)
        else:
            # If no caption, look for the closest preceding heading
            heading = table.find_previous(['h2', 'h3', 'h4'])
            if heading:
                table_name = heading.get_text(strip=True)
            else:
                table_name = f"table_{idx+1}"

        # Clean and slugify table name
        table_name = slugify(table_name)

        # Read the table into a DataFrame
        try:
            df = pd.read_html(StringIO(str(tables[0])))[0]
            # Save DataFrame to CSV
            filename = os.path.join(output_dir, f"{table_name}.csv")
            df.to_csv(filename, index=False, encoding="utf-8-sig")
            print(f"✅ Saved: {filename}")
        except Exception as e:
            print(f"❌ Failed to process table {idx+1}: {e}")

# Example usage
url = 'ypur_wikipidea_link_here'
extract_tables_from_wikipedia(url)
