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
import time
from datetime import datetime

def createModel(symbol, numDays = 100):
    data = yhget.get_stock_data(symbol, numDays)
   #myGraph.plotData(data, symbol)
    newModel = genmodel1.genModel1(data)
    return data, newModel

def predictModel(model, openx, highx, lowx, volx):
    features = np.array([[openx, highx, lowx, volx]])
    return model.predict(features)

def webStr2Float(s):
    return float(s)

def webStr2Int(s):
    return int(s.replace(',', ''))

#@genutil.Timer._timer
def soupModel(model, symbol):
    soup_data = yhsoup.getStockInfo(symbol)
    soup_open = webStr2Float(soup_data["Open"])
    soup_low = webStr2Float(soup_data["Day's Range"].split()[0])
    soup_high = webStr2Float(soup_data["Day's Range"].split()[2])
    soup_vol = webStr2Int(soup_data["Volume"])
    soup_bid = webStr2Float(soup_data["Bid"].split()[0])
    soup_ask = webStr2Float(soup_data["Ask"].split()[0])
    soup_mid = (soup_ask + soup_bid)/2
    soup_predict = predictModel(model, soup_open, soup_high, soup_low, soup_vol)
    now = datetime.now()
    date_time = now.strftime("%Y%m%d %H:%M:%S")
    date_now = now.strftime("%Y%m%d")
    result = "%s %-5s %8.3f %8.3f %8.3f %8d %8.3f %8.3f"%\
              (date_time, symbol, soup_open, soup_low, soup_high, soup_vol, \
              soup_predict[0][0], soup_mid)
    print(result)
    myFile = open(_dataPathName + date_now + ".data", 'a')
    print(result, file=myFile)
    myFile.close()
    return soup_predict

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

###
### Unit test
###

def createModelSet1():
    riot_model = model1.loadModel("riot.m1")
    jnj_model = model1.loadModel("jnj.m1")
    dal_model = model1.loadModel("dal.m1")
    ual_model = model1.loadModel("ual.m1")
    tsla_model = model1.loadModel("tsla.m1")
    rivn_model = model1.loadModel("rivn.m1")

def updateInfoSet1():
    model1.soupModel(riot_model, "RIOT")
    model1.soupModel(dal_model, "DAL")
    model1.soupModel(ual_model, "UAL")
    model1.soupModel(tsla_model, "TSLA")
    model1.soupModel(rivn_model, "RIVN")
    model1.soupModel(jnj_model, "JNJ")

