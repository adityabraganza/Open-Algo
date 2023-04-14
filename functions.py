from datetime import datetime, timedelta
import yfinance as yf
import SimpleMathModule as SMM

def StockCLoseData(symbol: str, endDate, length: int) -> list:
    dataWantedSymbol = yf.download(
        symbol,
        start=(endDate - timedelta(days=length)).date(),
        end=(endDate).date(),
        progress = False
        )
    dataWantedSymbol = dataWantedSymbol.to_dict()

    ClosePriceValues = list()
    Dates = list(dataWantedSymbol["Close"])
    for __str__ in Dates:
        ClosePriceValues.append(dataWantedSymbol["Close"][__str__])
    return ClosePriceValues

def SimpleMovingAverage(list: list) -> dict:
    x = 0
    pastClose20days = []
    while x < 20:
        pastClose20days.append(list[len(list)-1-x])
        x += 1

    totalVal = 0
    for ele in range(0, len(pastClose20days)):
        totalVal = totalVal + pastClose20days[ele]
    MovingAverage20 = totalVal/len(pastClose20days)

    currPrice = pastClose20days[0]

    if currPrice  > ((0.05*currPrice)+MovingAverage20):
        Recomendation = "Strong Buy"
    elif currPrice  > ((0.03*currPrice)+MovingAverage20):
        Recomendation = "Weak Buy"
    elif currPrice < ((0.03*currPrice)-MovingAverage20):
        Recomendation = "Weak sell"
    elif currPrice < ((0.03*currPrice)-MovingAverage20):
        Recomendation = "Strong sell"
    else:
        Recomendation = "Neutral"

    valList = [
        "Recommendation: " + str(Recomendation),
        "Simple Moving Average: " + str(MovingAverage20),
        "Current Price: " + str(currPrice)]

    return valList

def FindBollingerBandValues(list: list) -> dict:

    x = 0
    bollingerBandStandardDeviationList = []
    while x < 20:
        bollingerBandStandardDeviationList.append(list[len(list)-1-x])
        x += 1

    totalValbollinger = 0
    for ele in range(0, len(bollingerBandStandardDeviationList)):
        totalValbollinger = totalValbollinger + bollingerBandStandardDeviationList[ele]
    MovingAverage20 = totalValbollinger/len(bollingerBandStandardDeviationList)

    currPrice = bollingerBandStandardDeviationList[0]
    UpperBand = MovingAverage20+(2*(SMM.StandardDeviation(bollingerBandStandardDeviationList)))
    LowerBand = MovingAverage20-(2*(SMM.StandardDeviation(bollingerBandStandardDeviationList)))

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
        "Bollinger Band Analysis: " + str(Recomendation),
        "Current Price: " + str(currPrice),
        "Upper Band: " + str(UpperBand),
        "Moving Average: " + str(MovingAverage20),
        "Lower Band: " + str(LowerBand)]
    return valList

def RelativeStrengthIndex(list: list) -> dict:

    x = 0
    pastClose15days = []
    while x < 15:
        pastClose15days.append(list[len(list)-1-x])
        x += 1

    postitivegrowth = []
    negativegrowth = []

    for ele in range(0, len(pastClose15days)):
        if ele != 0:
            tempval = pastClose15days[ele] - pastClose15days[ele - 1]
            if tempval > 0:
                postitivegrowth.append(tempval)
            if tempval < 0:
                negativegrowth.append(tempval)

    positivegrowthaverage = (abs(SMM.Sum(postitivegrowth)))/len(postitivegrowth)
    negativegrowthaverage = (abs(SMM.Sum(negativegrowth)))/len(negativegrowth)
    RS = positivegrowthaverage/negativegrowthaverage
    RSI = 100-(100/(1 + RS))

    Recomendation = "Error"

    if RSI >= 70:
        Recomendation = "Strong Sell"
    elif RSI <= 30:
        Recomendation = "Strong Buy"
    elif RSI > 55:
        Recomendation = "Uptrend"
    elif RSI < 45:
        Recomendation = "Downtrend"
    else:
        Recomendation = "Neutral"

    valList = [
        "RSI Analysis: " + str(Recomendation),
        "RSI Value: " + str(RSI)]
    return valList