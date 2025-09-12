# API and Rest API Introduction

---
## Learning Objectives

1. What APIs are and how they enable communication between different software systems.  

2. Principles of REST (Representational State Transfer) and how REST APIs structure requests and responses.  

3. Explain the role of REST APIs in modern applications and recognize their key components

---

## 1. What is an API?

**API** stands for **Application Programming Interface**.  
It is a **set of rules and protocols** that allows one software application to interact with another.

You can think of an API as a **restaurant waiter**:

- **You** → the application requesting something.
- **Menu** → the list of possible services (API documentation).
- **Waiter (API)** → takes your request to the kitchen and brings back the result.
- **Kitchen** → the backend system where the real work happens.

Without the waiter (API), you'd have to **go into the kitchen, understand the recipes, and cook** — much more complicated.

**Core components of an API:**

**Client**: The application or service that makes a request to the API. This could be a mobile app, a web browser, or another server.

**Server**: The application or service that receives the request and sends back a response.

**Request**: A message sent from the client to the server asking for something, such as data or to perform an action.

**Response**: The message sent back from the server to the client, which contains the requested data or a status message.

---

## 2. Why Do We Need APIs?

In modern systems:
- **Applications rarely work in isolation.**
- APIs **connect services** so they can share data and functionality.
- APIs **hide complexity** by exposing only what’s necessary.

**Industry Examples**:
- **Banking**: Mobile banking apps use APIs to fetch your account balance, initiate transfers, etc.
- **E-commerce**: Shopify APIs let sellers list products, manage orders, and handle payments.
- **Healthcare**: FHIR APIs allow secure sharing of patient health records between hospitals.
- **Travel**: Expedia uses airline APIs to fetch flight availability and pricing.

---

## 3. Types of APIs

1. **Open APIs** (Public APIs)
   - Available to external developers.
   - Example: OpenWeather API.

2. **Internal APIs** (Private APIs)
   - Used only within an organization.
   - Example: Internal HR system API to fetch employee data.

3. **Partner APIs**
   - Shared with specific partners under agreements.
   - Example: Payment gateway APIs for merchant partners.

4. **Composite APIs**
   - Allow you to batch multiple requests into one.
   - Example: Fetching user profile + order history in a single API call.

---

## 4. API Communication Styles

While APIs can follow different styles, **REST** is one of the most popular.  
Before diving into REST, here are common styles:

- **REST (Representational State Transfer)** → Resource-based, uses HTTP.
- **SOAP (Simple Object Access Protocol)** → XML-based, strict rules.
- **GraphQL** → Query language for APIs, lets clients request exactly what they need.
- **gRPC** → Uses Protocol Buffers, very fast, good for internal microservices.

---

## 5. What is REST API?

The most popular and widely used type of API today is the REST API. REST stands for REpresentational State Transfer. It's not a protocol itself but rather a set of architectural principles for designing networked applications.

**REST API** is an architectural style for building APIs that:
- Uses **HTTP** methods.
- Treats everything as a **resource** identified by a unique URL.
- Is **stateless** — each request contains all needed information, and the server doesn’t remember previous requests.


Think of a REST API as an **online library**:
- **Each book** → a resource (data object).
- **Library URL** → base API endpoint.
- **Book ID** → specific resource path.
- You can **GET** a book, **POST** a new one, **PUT** to update it, or **DELETE** it.

---

## 6. Key REST Principles

1. **Client-Server Separation**  
   - Client and server evolve independently.

2. **Statelessness**  
   - Every request from the client must contain all the necessary information.

3. **Cacheability**  
   - Responses should indicate whether data can be cached.

4. **Layered System**  
   - APIs can have intermediate servers like load balancers or security layers.

5. **Uniform Interface**  
   - Standardized way of accessing resources.

---

## 7. HTTP Methods in REST APIs

| Method   | Purpose                   | Example in E-Commerce |
|----------|---------------------------|-----------------------|
| GET      | Retrieve data              | Get product details   |
| POST     | Create new resource        | Add new product       |
| PUT      | Update resource fully      | Update entire product info |
| PATCH    | Update resource partially  | Change product price  |
| DELETE   | Remove resource            | Delete product        |

---

## 8. Parsing API response

Data returned from a REST API is typically in a structured format, most often JSON (JavaScript Object Notation) or, less commonly, XML (eXtensible Markup Language). Parsing this data means converting it from a raw string format into a structured data type that your programming language can easily work with, like a dictionary, object, or list.

### Parsing JSON Data
JSON is the de facto standard for data exchange on the web because it’s lightweight, human-readable, and easy for machines to parse. It's built on two structures:

- A collection of key/value pairs (like a Python dictionary or a JavaScript object).
- An ordered list of values (like an array or list).

#### Analogy: Unboxing a Toy Set
Imagine you order a complex LEGO set online. The box itself is the raw JSON string. You can't just play with the box; you have to parse it. You open the box and find a manual (the data structure) and bags of individual LEGO bricks (the data values). Now you can use these pieces to build what you want.

The process of parsing is like taking all the pieces out of the box and organizing them so you can actually use them.

#### Python Example
Python has a built-in json library that makes parsing straightforward. The most common method is json.loads(), which stands for "load string."

```python
import requests
import json

# A sample API response (as a string)
json_string_data = """
{
  "name": "Jane Doe",
  "age": 30,
  "isStudent": false,
  "courses": [
    {"title": "History", "credits": 3},
    {"title": "Math", "credits": 4}
  ],
  "address": {
    "street": "123 Main St",
    "city": "Anytown"
  }
}
"""

# Parsing the JSON string into a Python dictionary
parsed_data = json.loads(json_string_data)

# Now you can access the data like a dictionary
print(f"Name: {parsed_data['name']}")
print(f"Age: {parsed_data['age']}")
print(f"First course title: {parsed_data['courses'][0]['title']}")
print(f"City: {parsed_data['address']['city']}")
```

### Parsing XML Data
While less common for modern APIs, some older systems or enterprise applications still use XML. XML is a markup language with a tree-like structure, similar to HTML.

#### Analogy: Deciphering a Family Tree
An XML document is like a family tree. The root element is the family head, and nested elements are the children and grandchildren. To find a specific person, you have to follow the branches down the tree.

Parsing XML involves traversing this tree structure to find the specific data you need.

#### Python Example

The xml.etree.ElementTree library is a standard way to parse XML in Python.

```python
import xml.etree.ElementTree as ET

# A sample XML string
xml_string_data = """
<catalog>
  <book id="bk101">
    <author>Gambardella, Matthew</author>
    <title>XML Developer's Guide</title>
    <genre>Computer</genre>
    <price>44.95</price>
  </book>
  <book id="bk102">
    <author>Garcia, Hector</author>
    <title>Ikigai</title>
    <genre>Self-Help</genre>
    <price>15.99</price>
  </book>
</catalog>
"""

# Parsing the XML string
root = ET.fromstring(xml_string_data)

# Find the first book and extract its title
first_book_title = root.find('book/title').text
print(f"First book title: {first_book_title}")

# Iterate over all books
for book in root.findall('book'):
    author = book.find('author').text
    title = book.find('title').text
    print(f"Book: {title}, Author: {author}")
```


---
## 9. Basic Rest API operations

We will use the JSONPlaceholder API, which is a fake online REST API for testing. we will perform several operations on this API.

### GET Request: Fetching all posts

```python
import requests

# The API endpoint
url = 'https://jsonplaceholder.typicode.com/posts'

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the data in JSON format
    posts = response.json()
    print(posts[:2])  # Print the first two posts to save space
else:
    print(f"Error: {response.status_code}")
```

#### Understanding `requests.get()` with Arguments

When making an HTTP GET request in Python using the `requests` library, you can pass **headers** and **parameters** to customize the request.

##### 1. Syntax
```python
response = requests.get(url, headers=headers, params=parameters)
```

##### 2. Components

- **`url`** → The API endpoint you want to call.

- **`headers`** → A dictionary containing request headers, often used for:
  - Authentication (e.g., API keys, tokens).
  - Content type specification (e.g., `"Content-Type": "application/json"`).

- **`params`** → A dictionary of query parameters appended to the URL for filtering, pagination, or other dynamic requests.

```python
url = "https://api.example.com/data"
headers = {"X-API-KEY": "your_api_key_here"}
parameters = {"symbol": "BTC", "convert": "USD"}
```

### POST Request: Creating a new post

```python
import requests
import json

# The API endpoint
url = 'https://jsonplaceholder.typicode.com/posts'

# Data to be sent in the request body
new_post = {
    "title": "My New Post",
    "body": "This is a new post created using a POST request.",
    "userId": 1
}

# Make the POST request
response = requests.post(url, json=new_post)

# Check for a successful creation (status code 201)
if response.status_code == 201:
    # Print the data returned by the server
    created_post = response.json()
    print("Post created successfully!")
    print(created_post)
else:
    print(f"Error: {response.status_code}")
```

### DELETE Request: Deleting a post

```python
import requests

# The API endpoint for the post to be deleted
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Make the DELETE request
response = requests.delete(url)

# Check for a successful deletion (status code 200)
if response.status_code == 200:
    print("Post deleted successfully!")
else:
    print(f"Error: {response.status_code}")
```


