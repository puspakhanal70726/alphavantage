import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import requests
import json

DEMA = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_weekly&symbol=DEMA&apikey=KEY&datatype=json")
DEMA_json = json.loads(DEMA.text)

 TEMA = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_weekly&symbol=TEMAC&apikey=KEY&datatype=json")
TEMA_json = json.loads(TEMA.text)

TRIMA = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_weekly&symbol=TRIMA&apikey=KEY&datatype=json")
TRIMA_json = json.loads(TRIMA.text)

KAMA = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_weekly&symbol=KAMA&apikey=KEY&datatype=json")
KAMA_json= json.loads(KAMA.text)

MAMA = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_weekly&symbol=MAMA&apikey=KEY&datatype=json")
MAMA_json = json.loads(MAMA.text)

DEMAdate = []
DEMAhighPrice = []
DEMA = DEMA_json['Weekly Time Series']
for key, value in DEMA.items():
    DEMAdate.append(key)
    DEMAhighPrice.append(float(value['2. high']))
    if key == "2018-10-10":
        break
DEMAdate.reverse()
DEMAhighPrice.reverse()

fig, axs = plt.subplots()
axs.plot(DEMAdate, DEMAhighPrice)
axs.set_ylabel("Stock Price ($)")
axs.set_title("DEMA Stock Prices: Oct '5 - Oct '10")
axs.grid(True)
plt.xticks([])
fig.savefig("DEMA.png")


TEMAdate = []
TEMAhighPrice = []
TEMA = TEMA_json['Weekly Time Series']
for key, value in TEMA.items():
    TEMAdate.append(key)
    TEMAhighPrice.append(float(value['2. high']))
    if key == "2018-10-10":
        break
TEMAdate.reverse()
TEMAhighPrice.reverse()

fig, axs = plt.subplots()
axs.plot(TEMAdate, TEMAhighPrice)
axs.set_ylabel("Stock Price ($)")
axs.set_title("TEMA Stock Prices: Oct '5 - Oct '10")
axs.grid(True)
plt.xticks([])
fig.savefig("TEMA.png")


TRIMAdate = []
TRIMAhighPrice = []
TRIMA = TRIMA_json['Weekly Time Series']
for key, value in TRIMA.items():
    TRIMAdate.append(key)
    TRIMAhighPrice.append(float(value['2. high']))
    if key == "2018-10-10":
        break
TRIMAdate.reverse()
TRIMAhighPrice.reverse()

fig, axs = plt.subplots()
axs.plot(TRIMAdate, TRIMAhighPrice)
axs.set_ylabel("Stock Price ($)")
axs.set_title("TRIMA Stock Prices: Oct '5 -  Oct '10")
axs.grid(True)
plt.xticks([])
fig.savefig("TRIMA.png")


KAMAdate = []
KAMAhighPrice = []
KAMA = KAMA_json['Weekly Time Series']
for key, value in KAMA.items():
    KAMAdate.append(key)
    KAMAhighPrice.append(float(value['2. high']))
    if key == "2018-10-10":
        break
KAMAdate.reverse()
KAMAhighPrice.reverse()

fig, axs = plt.subplots()
axs.plot(KAMAdate, KAMAhighPrice)
axs.set_ylabel("Stock Price ($)")
axs.set_title("KAMA Stock Prices: Oct '5 - Oct '10")
axs.grid(True)
plt.xticks([])
fig.savefig("KAMA.png")


MAMAdate = []
MAMAhighPrice = []
MAMA = MAMA_json['Weekly Time Series']
for key, value in MAMA.items():
    MAMAdate.append(key)
    MAMAhighPrice.append(float(value['2. high']))
    if key == "2018-10-10":
        break
MAMAdate.reverse()
MAMAhighPrice.reverse()

fig, axs = plt.subplots()
axs.plot(MAMAdate, MAMAhighPrice)
axs.set_ylabel("Stock Price ($)")
axs.set_title("MAMA Stock Prices: Oct '5 - Oct '10")
axs.grid(True)
plt.xticks([])
fig.savefig("MAMA.png")
