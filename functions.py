from datetime import date, datetime, timedelta
import yfinance as yf
from SimpleMathModule import *

def findBollingerBandValues(symbol, HistoricalDataLength):

    dataWantedSymbol = yf.download(
        symbol,
        start=(datetime.today() - timedelta(days=HistoricalDataLength)).date(),
        end=date.today()
        )
    dataWantedSymbol = dataWantedSymbol.to_dict()

    ClosePriceValues = list()
    Dates = list(dataWantedSymbol["Close"])
    x = 0
    for __str__ in Dates:
        ClosePriceValues.append(dataWantedSymbol["Close"][__str__])

    x = 0
    bollingerBandStandardDeviationList = []
    while x < 20:
        bollingerBandStandardDeviationList.append(ClosePriceValues[len(ClosePriceValues)-1-x])
        x += 1
    totalValbollinger = 0
    for ele in range(0, len(bollingerBandStandardDeviationList)):
        totalValbollinger = totalValbollinger + bollingerBandStandardDeviationList[ele]
    MovingAverage20 = totalValbollinger/len(bollingerBandStandardDeviationList)

    currPrice = bollingerBandStandardDeviationList[0]
    UpperBand = MovingAverage20+(2*(StandardDeviation(bollingerBandStandardDeviationList)))
    LowerBand = MovingAverage20-(2*(StandardDeviation(bollingerBandStandardDeviationList)))

    Recomendation = "Error"

    if currPrice > UpperBand + 0.005*currPrice:
        Recomendation = "Strong Sell"
    elif currPrice < LowerBand + 0.005*currPrice:
        Recomendation = "Strong Buy"
    elif MovingAverage20 - 0.005*currPrice < currPrice and currPrice < MovingAverage20 + 0.005*currPrice:
        Recomendation = "Neutral"
    elif currPrice > currPrice + 0.005*MovingAverage20:
        Recomendation = "Weak Buy"
    else:
        Recomendation = "Weak Sell"

    valList = [
        "Current Price: " + str(currPrice),
        "Upper Band: " + str(UpperBand),
        "Moving Average: " + str(MovingAverage20),
        "Lower Band: " + str(LowerBand),
        "Analysis: " + str(Recomendation)]
    return valList

def RelativeStrengthIndex(symbol):
    return