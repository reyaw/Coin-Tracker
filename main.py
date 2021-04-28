# This code is based on the tutorial found at https://realpython.com/python-bitcoin-ifttt/
# but has been modified for use with CoinDesk api.

# Powered by CoinDesk https://www.coindesk.com/price/bitcoin

import requests
bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(bitcoin_api_url)
response_json = response.json()
print(type(response_json))

for i in response_json:
    print(i + ": " + str(response_json[i]))

