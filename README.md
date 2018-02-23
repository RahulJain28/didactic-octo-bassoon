# didactic-octo-bassoon
Note: Assume spot GDAX price, no fees

Before running: pip install selenium, pip install coinbase, pip install forex-python and ensure the chromedriver is in the same directory as the script

Run with: python findarb.py

optional: -eth, -ltc, -btc, -bch to specify currency to get data for. Default is all 4

Ex: "python findarb.py -eth -btc" to only pull eth & btc data

Current functionality:
  - only koinex
  - first column is for each level in the order book, second is cumulative percentages
  
Future work: 
   - add in fees
   - combine with vamshis script so theres an option to just get a quick check on the arbs rather than waiting 25 seconds
   - input $(arb amount) and get back exactly what % return you can get for each currency
   - input $(arb amount) and show how to split up investments across pairs to optimize returns

