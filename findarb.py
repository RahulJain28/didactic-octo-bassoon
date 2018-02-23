import selenium
from selenium import webdriver
import time
from coinbase.wallet.client import Client
import argparse 
from forex_python.converter import CurrencyRates

c = CurrencyRates()
conversion = c.get_rate('USD', 'INR')
url = "https://koinex.in"
client = Client("poop","poop")
eth = float(client.get_spot_price(currency_pair = 'ETH-USD')['amount'])
btc = float(client.get_spot_price(currency_pair = 'BTC-USD')['amount'])
ltc = float(client.get_spot_price(currency_pair = 'LTC-USD')['amount'])
bch = float(client.get_spot_price(currency_pair = 'BCH-USD')['amount'])
browser = webdriver.Chrome()

def findarb(cointype): 
    list = []
    if(cointype == "ETH"):
        url = "https://koinex.in"
        coin = eth
    if(cointype == 'BTC'): 
        url = "https://koinex.in/exchange/bitcoin"
        coin = btc
    if(cointype == 'LTC'):
        url = "https://koinex.in/exchange/litecoin"
        coin = ltc
    if(cointype == "BCH"):
        url = "https://koinex.in/exchange/bitcoin_cash"
        coin = bch; 
    browser.get(url)
    time.sleep(5)
    innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
    text = innerHTML.encode('ascii', 'ignore')
    with open("Output.txt", "w") as text_file:
        text_file.write(text)
    x= text.find('<tbody class="sell-orders">')
    y= text.find('</tr><!-- end ngRepeat: order in vm.sellOrders -->')
    substring = text[x:y]
    times = 13 
    volume = []
    price = []
    while times > 0:
         x = substring.find('td class="border-right-1 ng-binding">')
         substring = substring[x:]
         x = substring.find('>')
         y = substring.find('<')
         volume.append(float(substring[x+1:y].replace(',','')))
         substring = substring[y:]
         x = substring.find('td class="ng-binding">')
         substring = substring[x:]
         x = substring.find('>')
         y = substring.find('<')
         price.append(float(substring[x+1:y].replace(',','')))
         substring = substring[y:]
         times = times - 1
    print "{0}".format(cointype)
    for i in range(len(price)):
         p = price[i]/conversion * volume[i]
         list.append([p,(price[i]/conversion - coin)/coin])
    print_arb(list)
    print("--------------------")
    return list
 
def print_arb(list):
    perc = 0;
    sum = 0; 
    for i in range(len(list)):
        print "${0:.2f} at {1:.3%} || ${2:.2f} at {3:.3%}".format(list[i][0], list[i][1],list[i][0] + sum, (sum*perc + list[i][0]*list[i][1])/(list[i][0]+sum))
        #print "${0:.2f} at {1:.3%}".format(list[i][0] + sum, (sum*perc + list[i][0]*list[i][1])/(list[i][0]+sum))
        perc = (sum*perc + list[i][0]*list[i][1])/(list[i][0]+sum)
        sum += list[i][0]
        #print perc
parser = argparse.ArgumentParser()
parser.add_argument("-eth", action="store_true")
parser.add_argument("-ltc",action="store_true")
parser.add_argument("-btc",action="store_true")
parser.add_argument("-bch",action="store_true")
args = parser.parse_args()
if(args.eth or args.ltc or args.btc or args.bch):
    if(args.eth):
        eth_list = findarb("ETH")
        print(eth_list)
        print_arb(eth_list)
    if(args.ltc):
        ltc_list = findarb("LTC")
    if(args.btc):
        btc_list = findarb("BTC")
    if(args.bch):
        bch_list = findarb("BCH")
else:
    findarb("ETH")
    findarb("BTC")
    findarb("LTC")
    findarb("BCH")
browser.quit()
