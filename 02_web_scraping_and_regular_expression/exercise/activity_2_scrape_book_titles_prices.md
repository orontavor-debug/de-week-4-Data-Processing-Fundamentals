# Exercise 2: Scrape Book Titles & Prices

## Objective:  
Ask is to scrape the website [Books to Scrape](https://books.toscrape.com/) (a practice website for web scraping).  

## Instructions:
Your goal is to:  
1. Scrape the **first page** of the site.  
2. Extract for each book:  
   - **Title** (from the HTML tag).  
   - **Price** (use regex to extract the numeric value from the price string, e.g. `£51.77 → 51.77`).  
3. Store results in a **Pandas DataFrame** with two columns: `Title` and `Price`.  
4. Display the **top 5 rows** as a preview.  
5. Save the results as a CSV file named `books_page1.csv`.  

