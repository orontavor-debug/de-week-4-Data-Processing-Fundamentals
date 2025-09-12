# Web scraping and Regular Expression

---

## Learning Objective
- The objective of this module is to introduce learners to the fundamentals of web scraping and regular expressions in Python.
- You will understand how to extract structured information from websites using tools like BeautifulSoup and how to apply regex for advanced text pattern matching.
- By the end, you should be able to differentiate when to use APIs, web scraping, or regex and apply these techniques effectively to real-world datasets. 

---

## 1. Introduction

In today's data-driven world, a massive amount of information exists on the internet, locked away in web pages. Web scraping is the automated process of extracting this data from websites. It's like having a digital assistant that can read a web page and pull out exactly what you need. When combined with regular expressions (regex), this process becomes incredibly powerful and precise.

Imagine you want to collect seashells from a beach. You could either ask a shopkeeper for seashells (like using an **API**) or go to the beach and collect them yourself (like doing **web scraping**).

-   **API** = Pre-packaged data, clean, structured, and handed to you.
-   **Web Scraping** = Extracting data directly from a website, often messy and requiring cleaning.

---

## 2. What is Web Scraping?


### Think of web scraping as an expert librarian.

The internet is a vast library filled with countless books (web pages).

You, the client, need to find specific information, like the titles and authors of all books on a particular shelf.

The web scraping script is your librarian. It automatically navigates to the correct shelf (URL), scans the pages, and extracts the desired information (the titles and authors), ignoring everything else.


### Use Cases of Web Scraping

Web scraping is used for various purposes across many industries:

- **E-commerce**: Scraping competitor prices to dynamically adjust your own pricing.
- **Finance**: Gathering stock market data from financial news sites.
- **Marketing**: Collecting customer reviews and product information.
- **Research**: Building datasets for academic studies by scraping public records or scientific papers.


### The Web Scraping Process

1. **Request**: Your script sends an HTTP GET request to a target URL.  
2. **Receive**: The server responds by sending back the page's HTML, CSS, and JavaScript.  
3. **Parse**: Your script processes this raw HTML content. This is where you identify the parts of the page that contain the data you want.  
4. **Extract**: The script pulls out the specific data points (e.g., text, links, image URLs).  
5. **Store**: The extracted data is saved in a structured format, such as a CSV file, a database, or a JSON file.  


---

## 3. Tools for Web Scraping

1.  **Requests** → To fetch webpage content.
2.  **BeautifulSoup** → To parse and navigate HTML.
3.  **Regex** → To extract patterns like emails, phone numbers, or dates.
4.  **Selenium / Playwright** → To scrape dynamic JavaScript-heavy websites.
5.  **Scrapy** → Scrapy handles the entire scraping process from start to finish.

---

## 4. Headers in Web Scraping 

When your script makes a request to a website, it communicates through **HTTP headers**. These headers contain metadata that helps servers understand **who you are** and **how you want to interact** with them.  

If headers are missing or poorly set, the request may be **blocked, redirected, or throttled**, because websites often check headers to distinguish between:  
- **Legitimate users (browsers)**  
- **Automated bots/scrapers**

### Common HTTP Headers in Scraping  

#### User-Agent  
- Identifies the client making the request (browser, bot, or script).  
- Many sites block requests with no User-Agent or with suspicious ones.  
- Example:  
  ```
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
  ```

#### Accept / Accept-Language  
- Tells the server what content formats you can handle.  
- Example:  
  ```
  Accept: text/html
  Accept-Language: en-US,en;q=0.9
  ```

#### Referer  
- Indicates the source of your request (e.g., from a search page).  
- Some websites check this to prevent “deep linking.”  

#### Authorization / Cookies  
- Needed when scraping sites that require login.  
- Example:  
  ```
  Authorization: Bearer <token>
  ```

#### Connection & Keep-Alive  
- Helps maintain persistent sessions instead of opening a new connection for each request.

### Best Practices with Headers in Web Scraping  
- Always **set a User-Agent** to mimic a real browser.  
- Use **rotating headers/proxies** to avoid detection on large-scale scraping.  
- Respect **robots.txt** and website terms of service.  
- Avoid sending unnecessary headers — stick to what a normal browser would send.  

### Example: Sending Custom Headers with `requests`  

```python
import requests

url = "https://books.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.text[:500])  # print first 500 chars of HTML
```

---

## 5. BeautifulSoup (bs4) in detail

### Analogy
Think of **BeautifulSoup** as a **magnifying glass**.  
You already have a webpage (HTML document), and you just need a tool to carefully inspect it and pick out the data you want.  

### Key Features
- Parses HTML and XML documents.  
- Provides easy-to-use methods to search and navigate the parse tree.  
- Works well when combined with the `requests` library (to fetch the webpage).

### Example: Scrape HTML content

Let's say we have the following HTML snippet and we want to get the title and the price of the product.

```html
<div class="product-card">
  <h2>Product Name</h2>
  <span class="price">$59.99</span>
</div>
```

```python
from bs4 import BeautifulSoup

html_doc = """
<div class="product-card">
  <h2>Product Name</h2>
  <span class="price">$59.99</span>
</div>
"""


# Create a Beautiful Soup object
soup = BeautifulSoup(html_doc, 'html.parser')

# Find the <h2> tag
title_tag = soup.find('h2')

# Find the <span> tag with the class 'price'
price_tag = soup.find('span', class_='price')

# Extract the text from the tags
product_name = title_tag.get_text() if title_tag else "N/A"
product_price = price_tag.get_text() if price_tag else "N/A"

print(f"Product Name: {product_name}")
print(f"Product Price: {product_price}")
```


### Example: Scraping Quotes
Suppose you want to scrape quotes and authors from: [http://quotes.toscrape.com](http://quotes.toscrape.com)

```python
import requests
from bs4 import BeautifulSoup

# Step 1: Request the page
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract data
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for quote, author in zip(quotes, authors):
    print(f"{quote.text} - {author.text}")
```


---

## 6. What is Regex?

**Regex (Regular Expressions)** is like a **filter or magnet** that finds patterns in text.

### Example

-   Find all phone numbers in text.
-   Extract all email addresses.
-   Identify dates or specific keywords.

---

## 7. The Regex Cheat Sheet

Regex uses special characters (called **metacharacters**) to define patterns.  
Here are some of the most common ones:

| Character | Description                                    | Example  | Matches                   |
|-----------|-----------------------------------------------|----------|---------------------------|
| `.`       | Any single character (except newline)         | `c.t`    | `cat`, `cut`, `cbt`       |
| `*`       | Zero or more occurrences of the preceding character | `a*b` | `b`, `ab`, `aab`, `aaab` |
| `+`       | One or more occurrences of the preceding character | `a+b` | `ab`, `aab`, `aaab`      |
| `?`       | Zero or one occurrence of the preceding character | `a?b` | `b`, `ab`                 |
| `[ ]`     | A set of characters                           | `[abc]`  | `a`, `b`, `c`             |
| `[^ ]`    | A set of characters **NOT** to match          | `[^abc]` | Any char except `a, b, c` |
| `^`       | Matches the **beginning** of the string       | `^Hello` | `Hello world`             |
| `$`       | Matches the **end** of the string             | `world$` | `Hello world`             |
| `\d`      | Matches any digit (0-9)                       | `\d+`    | `123`, `45`, `9`          |
| `\w`      | Matches any word character (`a-z`, `A-Z`, `0-9`, `_`) | `\w+` | `hello`, `_user1`        |
| `( )`     | Creates a **capture group**                   | `(\d+)`  | Captures `123` from `123` |

---

## 8. The `re` Module in Python

Python provides the **`re` module** to work with **regular expressions (regex)**. Regular expressions are patterns used to match, search, or manipulate text efficiently.

### Why Use `re`?
- Validate inputs (e.g., emails, phone numbers, postal codes).
- Search for specific patterns in text.
- Extract useful information from unstructured data.
- Replace or clean unwanted text patterns.

### Key Functions in `re`

| Function | Description | Example |
|----------|-------------|---------|
| `re.match(pattern, string)` | Matches pattern **only at the beginning** of the string. | `re.match(r"\d+", "123abc")` → match `"123"` |
| `re.search(pattern, string)` | Searches the string for the **first occurrence** of the pattern. | `re.search(r"\d+", "abc123xyz")` → match `"123"` |
| `re.findall(pattern, string)` | Returns **all non-overlapping matches** as a list. | `re.findall(r"\d+", "abc123xyz456")` → `["123", "456"]` |
| `re.finditer(pattern, string)` | Returns an **iterator of match objects** (with position info). | `[m.group() for m in re.finditer(r"\d+", "abc123xyz456")]` |
| `re.sub(pattern, repl, string)` | Replaces all matches with a given replacement. | `re.sub(r"\d+", "#", "ID123Code456")` → `"ID#Code#"` |
| `re.split(pattern, string)` | Splits string by the given pattern. | `re.split(r"\s+", "one two   three")` → `["one", "two", "three"]` |
| `re.compile(pattern)` | Compiles a regex for repeated use. | `pattern = re.compile(r"\d+")` then `pattern.findall("abc123")` |




### Example 1: Extracting Prices from HTML

```xml
<p>Price: 19.99$</p>
```

```python
import re
html_content = "<p>Price: 19.99$</p>"
pattern = r"Price\s*:\s*(\d+\.\d{2})\$"
match = re.search(pattern, html_content)
if match:
    print("Price found:", match.group(1))  # Output: 19.99
```

### Example 2: Extracting URLs from a Web Page

```python
import re

html = '<a href="https://example.com/page1">Link 1</a>'
url_pattern = r"http[s]?://[^\s\"'>]+"
urls = re.findall(url_pattern, html)
print(urls)
```

### Example 3: Scraping + Regex in Action

Let's say we scrape a webpage containing contact info.

``` python
import requests
from bs4 import BeautifulSoup
import re

# Step 1: Get webpage content
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Extract all text
text = soup.get_text()

# Step 3: Use regex to find emails and phone numbers
emails = re.findall(r"[\w._%+-]+@[\w.-]+\.\w+", text)
phones = re.findall(r"\+?\d[\d\- ]{7,}\d", text)

print("Emails:", emails)
print("Phone Numbers:", phones)

# Step 4: Save to file
with open("scraped_data.txt", "w") as f:
    f.write("Emails:\n" + "\n".join(emails) + "\n")
    f.write("Phones:\n" + "\n".join(phones))
```

The regex would extract:

    Emails: ['support@example.com', 'info@myshop.org']
    Phones: ['+1-202-555-0173']

Use above example and scrape email id from the page `https://webscraper.io/test-sites`

```python
import requests
from bs4 import BeautifulSoup
import re

url = "https://webscraper.io/test-sites"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text()
emails = re.findall(r"[\w._%+-]+@[\w.-]+\.\w+", text)
print("Emails:", emails)
```


---

## 9. When to Use API vs Web Scraping?

Choosing between an API and web scraping depends on your use case, data availability, and technical constraints.  

| Aspect                | API                                       | Web Scraping                                 |
|------------------------|------------------------------------------|-----------------------------------------------|
| **Data Access**        | Provides structured, clean data (JSON, XML). | Extracts data directly from web pages (HTML). |
| **Ease of Use**        | Easier if documentation and endpoints exist. | Requires parsing HTML, handling tags, and selectors. |
| **Reliability**        | More reliable, data formats are consistent. | Prone to breaking if the site structure changes. |
| **Speed**              | Faster (direct server response).          | Slower (needs to load & parse web pages). |
| **Rate Limits**        | Controlled by API provider (usually defined in docs). | Limited by website restrictions or anti-bot measures. |
| **Legality**           | Usually allowed if API terms are followed. | May violate site’s Terms of Service (check before scraping). |
| **Data Availability**  | Sometimes limited; not all data is exposed via API. | Can access any visible data on the site. |
| **Authentication**     | Often requires API keys or OAuth.         | Usually none (unless scraping logged-in content). |
| **Best Use Cases**     | Real-time data, consistent formats, large datasets. | When no API exists or data is not provided via API. |


 **Rule of Thumb:**  
- Use an **API** whenever it’s available and provides the data you need.  
- Use **web scraping** as a fallback when no API exists, or the API doesn’t expose all required information.  










