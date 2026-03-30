import requests

 #will use Bitcoin,Ethereum,Tether USDt,BNB for this task
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
headers = {"X-CMC_PRO_API_KEY": "00448d3a637f440fb139e5dc173f4b88"}

response = requests.get(url, headers=headers,params={"symbol": "BTC,ETH,USDT,BNB"})
#check that api call is working
#print(response.status_code)

parsed_coins=response.json()
# print(parsed_coins['data'])
#create reference variable for loops
top_coin = ""
top_change = 0

#loop over all coins
for coin in parsed_coins['data']:
    name=(parsed_coins['data'][coin]['name'])
    price=(parsed_coins['data'][coin]['quote']['USD']['price'])
    percent_change_24=(parsed_coins['data'][coin]['quote']['USD']['percent_change_24h'])
    if percent_change_24 > top_change: #find top coin
        top_change = percent_change_24
        top_coin = name

print(top_coin,top_change)
with open("crypto_summary.txt", "w") as file:
    file.write(f"{name}, {price}, {percent_change_24}\n")
    file.write(f"\nTop performer: {top_coin} with {top_change}%")