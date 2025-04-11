import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from io import StringIO

# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji"

# Get page content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the main kanji table
tables = soup.find_all("table", {"class": "wikitable"})
df = pd.read_html(StringIO(str(tables[0])))[0]

# Keep only useful columns
columns_to_keep = ["New (Shinjitai)", "English meaning"]
filtered_df = df[columns_to_keep]

# Clean Kanji column (remove footnote numbers like '韓 [5]')
filtered_df.loc[:, "New (Shinjitai)"] = filtered_df["New (Shinjitai)"].str.replace(r"\s*\[\d+\]", "", regex=True)

# Export cleaned CSV
filtered_df.to_csv("filtered_joyo_kanji_cleaned.csv", index=False, encoding="utf-8-sig")
print("✅ Cleaned kanji data saved to 'filtered_joyo_kanji_cleaned.csv'")

# 🔤 Join all Kanji characters into one string
all_kanji = ''.join(filtered_df["New (Shinjitai)"].dropna())

# Save to text file
with open("all_joyo_kanji.txt", "w", encoding="utf-8") as f:
    f.write(all_kanji)

# ✅ Output the full Kanji string
print("\n✅ All Jōyō Kanji characters saved to 'all_joyo_kanji.txt'")
print("🔤 Full string:\n")
print(all_kanji)
