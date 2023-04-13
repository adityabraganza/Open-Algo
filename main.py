from functions import *
from pprint import pprint as Rprint

symbol = (input("Enter Symbol Name: ")).upper() + ".NS"
print("Bollinger Band Analysis: ")
Rprint(findBollingerBandValues(symbol))
print("Relative Strength Index Analysis: ")
Rprint(RelativeStrengthIndex(symbol))