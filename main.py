from functions import *
import tkinter as tk

def analysis():
    symbol = (symbolInputBox.get()).upper() + ".NS"

    analysedGUI = tk.Tk()

    BBData = findBollingerBandValues(symbol)

    tk.Label(analysedGUI, text="Bollinger Band Analysis:").grid(column=0, row=0) #Bollinger Band
    tk.Label(analysedGUI, text=(BBData[0])).grid(column=0, row=1) #Recomendation
    tk.Label(analysedGUI, text=(BBData[1])).grid(column=0, row=2) #Current price
    tk.Label(analysedGUI, text=(BBData[2])).grid(column=0, row=3) #Upper band
    tk.Label(analysedGUI, text=(BBData[3])).grid(column=0, row=4) #MA
    tk.Label(analysedGUI, text=(BBData[4])).grid(column=0, row=5) #Lower band

    tk.Label(analysedGUI, text="").grid(column=0, row=6) #Blank

    RSIData = RelativeStrengthIndex(symbol)
    tk.Label(analysedGUI, text="Relative Strength Index Analysis:").grid(column=0, row=7) #Relative Strength Index
    tk.Label(analysedGUI, text=(RSIData[0])).grid(column=0, row=8) #Recomendation
    tk.Label(analysedGUI, text=(RSIData[1])).grid(column=0, row=9) #RSI Value

    analysedGUI.mainloop()

root = tk.Tk()

symbolInputBox = tk.Entry(root)
symbolInputBox.pack()

symbolInputButton = tk.Button(root, text="Analyse", command=analysis)
symbolInputButton.pack()

root.mainloop()