#!/usr/bin/python3
###
### hack the path
###
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

def runModel(symbol, numDays = 100):
    data = yhget.get_stock_data(symbol, numDays)
   #myGraph.plotData(data, symbol)
    newModel = genmodel1.genModel1(data)
    return data, newModel

def predictModel(model, openx, highx, lowx, volx):
    features = np.array([[openx, highx, lowx, volx]])
    return model.predict(features)

@genutil.Timer._timer
def soupModel(model, symbol):
    soup_data = yhsoup.getStockInfo(symbol)
    soup_open = float(soup_data["Open"])
    soup_low = float(soup_data["Day's Range"].split()[0])
    soup_high = float(soup_data["Day's Range"].split()[2])
    soup_vol = int(soup_data["Volume"].replace(',', ''))
    return predictModel(model, soup_open, soup_high, soup_low, soup_vol)

###
### Save and Load from a fixed location
###
_dataPathName = "/mnt/tobynas/tmp/FromAlex/Programming/Python/stockmodels/"

def saveModel(model, filename):
    model.save(_dataPathName + filename)

def loadModel(filename):
    return keras.models.load_model(_dataPathName + filename)

###
###
###
if __name__ == '__main__':
    runModel("RIOT", 2000)
