# LIVE_API_DATA

import MMXXIKEYS
import numpy as np
from time import sleep
import matplotlib.pyplot as plt
from binance.client import Client
import pandas as pd
import statistics

#INSERT API KEYS
client = Client(FILE_NAME.PRIVATE_KEYNAME,FILE_NAME.SECRET_KEYNAME) 

#INSERT PAIR
symbol= 'AB'

#CAN EDIT INTERVAL AND DATA START TIME
BTC = client.get_historical_klines(symbol=symbol, interval='1m', start_str="24 hour ago UTC")

#CREATE ARRAYS TO API DATA 
current = []
last = []
highs = []
lows = []
highs__ = []
lows__ = []
uhighs = []
ulows = []

#CREATE NEW PLOT
fig, ax = plt.subplots()

#LOOP THAT GETS DATA POINTS x1, x2, h, l and appends TO PREVIOUSLY CREATED ARRAYS FOR PLOT
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

		for h in highs:
			highs__.append(h)
			u_highs=np.mean(highs__)

		for l in lows:
			lows__.append(l)
			u_lows=np.mean(lows__)


		plt.cla()
		# plt.plot(u_lows)
		# plt.plot(u_highs)
		# plt.plot(current)
		plt.plot(highs)
		plt.plot(lows)

		plt.pause(0.01)
		sleep(1)
