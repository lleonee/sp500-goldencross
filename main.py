import yfinance as yf 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import pandas_datareader as pdr


ticker = "SP500"

data = pdr.DataReader(ticker, "fred", start = dt.date(2020,1,1))

data.plot()
plt.show()
