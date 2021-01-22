import MMXXIKEYS
import numpy as np
from time import sleep
import matplotlib.pyplot as plt
from binance.client import Client
import pandas as pd
import statistics

client = Client(FILE_NAME.PRIVATE_KEYNAME,FILE_NAME.SECRET_KEYNAME)
symbol= 'AB'
BTC = client.get_historical_klines(symbol=symbol, interval='1m', start_str="24 hour ago UTC")
current = []
last = []
highs = []
lows = []
highs__ = []
lows__ = []
uhighs = []
ulows = []
	
fig, ax = plt.subplots()

On = True
while On:
	BTC = client.get_historical_klines(symbol=symbol, interval='1m', start_str="1 hour ago UTC")
	x1 = float(BTC[-1][4])
	x2 = float(BTC[-2][4])
	h = float(BTC[-1][2])
	l = float(BTC[-1][3]) 
	current.append(x1)
	highs.append(h)
	lows.append(l)
				
	plt.cla()
	plt.plot(highs)
	plt.plot(lows)
	plt.pause(0.01)
	sleep(1)
