from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url = "https://books.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
# print(response.status_code) # testing connection
# print(response.text[:500])  # print first 500 chars of HTML

soup = BeautifulSoup(response.text, "html.parser") # soup
h3_tags = soup.find_all("h3") #find h3 tags on page, books are nested in them
for h3 in h3_tags: # loop each tag, extrct book title
    title = h3.find("a").get("title")
    print(title)

prices = soup.find_all("p", class_="price_color") #price sits under the class price_color, within p
for price in prices: #loop every tag
    match = re.search(r"\d+\.\d+", price.text) #regex according to the pattern
    if match:
        print(match.group())

title_list = [h3.find("a").get("title") for h3 in h3_tags] # extract book titles from h3, find <a> and get the title
price_list = [re.search(r"\d+\.\d+", price.text).group() for price in prices] #remove £ with regex

df = pd.DataFrame({
    "Title": title_list,
    "Price": price_list
})

print(df.head())
df.to_csv("books_page1.csv", index=False)