from functions import *
from pprint import pprint as Rprint
import tkinter as tk

def analysis():
    symbol = (symbolInputBox.get()).upper() + ".NS"


    endDate = datetime.today()
    data = StockCLoseData(symbol, endDate, 60)

    analysedGUI = tk.Tk()

    tk.Label(analysedGUI, text="Analysis for " + symbolInputBox.get().upper()).pack() #Display stock symbol

    tk.Label(analysedGUI, text="").pack() #Blank

    BBData = findBollingerBandValues(data)

    tk.Label(analysedGUI, text="Bollinger Band Analysis:").pack() #Bollinger Band
    tk.Label(analysedGUI, text=(BBData[0])).pack() #Recomendation
    tk.Label(analysedGUI, text=(BBData[1])).pack() #Current price
    tk.Label(analysedGUI, text=(BBData[2])).pack() #Upper band
    tk.Label(analysedGUI, text=(BBData[3])).pack() #MA
    tk.Label(analysedGUI, text=(BBData[4])).pack() #Lower band

    tk.Label(analysedGUI, text="").pack() #Blank

    RSIData = RelativeStrengthIndex(data)

    tk.Label(analysedGUI, text="Relative Strength Index Analysis:").pack() #Relative Strength Index
    tk.Label(analysedGUI, text=(RSIData[0])).pack() #Recomendation
    tk.Label(analysedGUI, text=(RSIData[1])).pack() #RSI Value

    analysedGUI.mainloop()

root = tk.Tk()

symbolInputBox = tk.Entry(root)
symbolInputBox.pack()

symbolInputButton = tk.Button(root, text="Analyse", command=analysis)
symbolInputButton.pack()

root.mainloop()