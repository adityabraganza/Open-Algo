from functions import *
from pprint import pprint as Rprint

nifty50list = [
"ACC",
"ADANIPORTS",
"AMBUJACEM",
"ASIANPAINT",
"AXISBANK",
"BAJAJ-AUTO",
"BANKBARODA",
"BHEL",
"BPCL",
"BHARTIARTL",
"BOSCHLTD",
"CIPLA",
"COALINDIA",
"DRREDDY",
"GAIL",
"GRASIM",
"HCLTECH",
"HDFCBANK",
"HEROMOTOCO",
"HINDALCO",
"HINDUNILVR",
"HDFC",
"ITC",
"ICICIBANK",
"IDEA",
"INDUSINDBK",
"INFY",
"KOTAKBANK",
"LT",
"LUPIN",
"M&M",
"MARUTI",
"NTPC",
"ONGC",
"POWERGRID",
"PNB",
"RELIANCE",
"SBIN",
"SUNPHARMA",
"TCS",
"TATAMOTORS",
"TATAPOWER",
"TATASTEEL",
"TECHM",
"ULTRACEMCO",
"VEDL",
"WIPRO",
"YESBANK",
"ZEEL"
]

symbolReco = {}

valueDictionaryBollinger = {}
strongBuysBollinger = ()

for string in nifty50list:
    try:
        tempBollingerData = findBollingerBandValues(string + ".NS")
        valueDictionaryBollinger.update({string:tempBollingerData})

        symbolReco.update({string: tempBollingerData[0]})
        if tempBollingerData[0] == "Strong Buy": strongBuysBollinger.append(string)
    except: print(string + " has returned no data")

Rprint(valueDictionaryBollinger)

Rprint(symbolReco)

print("")
print("Bollinger Band Analysis based strong buys")
Rprint(strongBuysBollinger)