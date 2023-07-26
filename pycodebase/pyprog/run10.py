import sys
sys.path.append('/mnt/tobynas/tmp/FromAlex/Programming/Python/pycodebase')
sys.path
import numpy as np
import importdata.yhget as yhget
import modelgen.graphModel as myGraph
import modelgen.model1 as genmodel1
import importdata.soupyahoo as yhsoup
import keras
import genutil.Timer
import time
from datetime import datetime
import pyprog.runM1 as model1
import pandas as pd
import matplotlib.pyplot as plt

def makePredict10(model, df):
    parray = []
    for x in range(df["Open"].size):
        openx = df["Open"][x]
        highx = df["High"][x]
        lowx = df["Low"][x]
        volx = df["Volume"][x]
        prediction = model1.predictModel(model = model, \
        openx = openx, highx = highx, lowx = lowx, volx = volx)
        parray.append(prediction[0][0])
    return parray

def makeDelta10(df, bound = None):
    if bound is None:
        bound = 5
    darray = []
    for x in range(df["Adj Close"].size):
        closex = df["Adj Close"][x]
        predictx = df["Predict"][x]
        val = ((abs(closex - predictx))/closex)*100
        # bound value
        if val > 5:
            val = 5
        darray.append(val)
    return darray

def run10showline(_data10):
    lines = _data10.plot(kind = "line", x = "Date",\
                             y = ["Adj Close", "Predict", "Delta"])
    plt.title('Adjusted Close vs Prediction and Delta')
    plt.show()

def run10showhist(_data10, n = 5):
    _data10["Delta"].plot.hist(bins = n)
    plt.title('Frequency of Delta in Each Group')
    plt.show()

def run10showpie(_data10):
    pie_bins = [0, 1, 2, 3, 4, 5]
    pie_groups = pd.cut(_data10["Delta"], pie_bins,\
                        labels = ['0-1', '1-2', '2-3', '3-4', '4-5'])
    pie_counts = pie_groups.value_counts()
    plt.pie(pie_counts, labels = pie_counts.index, autopct='%1.1f%%', \
            startangle = 140)
    plt.title('Frequency of Delta in Each Group')
    plt.axis('equal')
    plt.show()

def run10(sym, numDays, modelName):
    _data10 = yhget.get_stock_data(sym, numDays)
    _model = model1.loadModel(modelName)
    _predict10 = makePredict10(_model, _data10)
    _data10["Predict"] = _predict10
    _delta10 = makeDelta10(_data10)
    _data10["Delta"] = _delta10
    return _data10

# run10(sym = "RIOT", numDays = 14, modelName = "riot.m1")
# run10(sym = "TSLA", numDays = 14, modelName = "tsla.m1")

