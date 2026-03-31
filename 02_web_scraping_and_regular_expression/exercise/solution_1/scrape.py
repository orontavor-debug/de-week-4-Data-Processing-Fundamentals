from bs4 import BeautifulSoup
import requests
import pandas as pd

# url = "https://www.imdb.com/chart/top/"
#headers = {
#    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#    "Accept-Language": "en-US,en;q=0.9",
#  "Accept-Encoding": "gzip, deflate, br",
#    "Connection": "keep-alive",
# }

# response = requests.get(url, headers=headers)
# print(response.status_code)  # 200 means success

with open("imdb.html", "r", encoding="utf-8") as f: ## downloaded the .html file locally, imdb kept giving 202
    html = f.read()

# print(html) test

soup = BeautifulSoup(html, "html.parser") #define soup

titles = soup.find_all("h3", class_="ipc-title__text") # find all titles in html
print(len(titles))
print(titles[:3]) 

titles= titles[:25] #limit to 25 results

for title in titles: # print all 25 titles
    print(title.text)

ratings = soup.find_all("span", class_="ipc-rating-star--rating") # find all ratings in html
ratings= ratings[:25] #limit to 25 ratings

for rating in ratings:
    print(rating.text)

# print(len(ratings)) check its 25

for title, rating in zip(titles, ratings):
    print(f"{title.text} - {rating.text}")

df = pd.DataFrame({
    "Title": [title.text for title in titles],
    "Rating": [rating.text for rating in ratings]
})

print(df.head(10))  #top10
df.to_csv("top25_movies.csv", index=False)  #csv
