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
"CAIRN",
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

valueDictionaryBollinger = {}

for string in nifty50list:
    try:
        valueDictionaryBollinger.update({string:findBollingerBandValues(string + ".NS", 30)})
    except: print(string + " has returned no data")

Rprint(valueDictionaryBollinger)