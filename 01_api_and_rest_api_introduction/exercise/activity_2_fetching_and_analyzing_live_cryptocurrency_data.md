# Fetching and Analyzing Live Cryptocurrency Data

## Objective
Use a public API to fetch real-time cryptocurrency data, parse the JSON response, and save key metrics to a text file.

## Instructions

1. **Get an API Key:**  
   Sign up for a free API key from a cryptocurrency data provider CoinMarketCap. You can find their API documentation online.

   https://coinmarketcap.com/api/documentation/v1/ 

3. **Make the API Call:**  
   Write a Python script that uses the `requests` library to make a GET request to the CoinMarketCap API's "cryptocurrency quotes" endpoint. Your request should include your API key in the headers.

4. **Parse the JSON Response:**  
   The API will return a JSON object. Your task is to parse this object and extract the following information for at least three different cryptocurrencies (e.g., Bitcoin, Ethereum, and Solana):
   - Cryptocurrency name  
   - Current price in USD  
   - 24-hour price change percentage  

5. **Analyze the Data:**  
   Write a conditional statement to check which of the three cryptocurrencies had the highest price increase over the last 24 hours.

6. **Save to File:**  
   Create a text file named `crypto_summary.txt`. Write the extracted data (name, price, and 24-hour change) for each of the three cryptocurrencies to this file. On a new line, also write the name of the cryptocurrency that had the highest 24-hour price increase.




