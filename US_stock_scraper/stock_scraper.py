# -*- coding: utf-8 -*-

pip install yfinance

"""# Step 1. import the necessary package"""

# Commented out IPython magic to ensure Python compatibility.
import yfinance as yf
import matplotlib.pyplot as plt

# %matplotlib inline

"""# Step 2. Define the ticker and gather the data"""

tickerData = yf.Ticker('AMZN')
tickerData.info

tickerData.history(period='9mo')

"""# Step 3. Define the functions to show the record (basically select the period during the pandemic)"""

def extractTicker(targetTicker):
  data = yf.Ticker(targetTicker)

  companyName = data.info['longName']
  yearHigh = data.info['fiftyTwoWeekHigh']
  yearLow = data.info['fiftyTwoWeekLow']
  fiftyDayMean = data.info['fiftyDayAverage']
  twoHundredDayMean = data.info['twoHundredDayAverage']
  priceNow = data.info['ask']
  dayHigh = data.info['dayHigh']
  dayLow = data.info['dayLow']

  print('Company Name: '+companyName)
  print('Yearly high: ',yearHigh,' Yearly low: ',yearLow)
  print('Two hundred days average: ',twoHundredDayMean)
  print('The price now is ',priceNow)

  plt.rc('xtick', labelsize=20) 
  plt.rc('ytick', labelsize=20)
  showDividends(data)
  showDailyPrice(data)
  showVolume(data)


def showDividends(tickerData):
  dividendData = tickerData.dividends

  plt.figure(figsize=(20,10))
  plt.plot(dividendData.keys(), dividendData)
  plt.title(tickerData.info['longName']+' dividends',fontsize=16)
  plt.xlabel('Date',fontsize=16)
  plt.ylabel('Dividends value',fontsize=16) 

def showDailyPrice(tickerData):
  priceData = tickerData.history(period='9mo')

  plt.figure(figsize=(20,10))
  plt.plot(priceData.index, priceData['Close'])
  plt.title(tickerData.info['longName']+' Daily Price',fontsize=16)
  plt.xlabel('Date',fontsize=16)
  plt.ylabel('Close Price',fontsize=16)

def showVolume(tickerData):
  priceData = tickerData.history(period='9mo')

  plt.figure(figsize=(20,10))
  plt.plot(priceData.index, priceData['Volume'])
  plt.title(tickerData.info['longName']+' Daily Volume',fontsize=16)
  plt.xlabel('Date',fontsize=16)
  plt.ylabel('Transaction Volume',fontsize=16)

extractTicker("MSFT")

extractTicker('AMZN')

extractTicker('EXPE')

