from pycoingecko import CoinGeckoAPI
from datetime import datetime
import datetime
import os
import glob
import pandas as pd
import numpy as np
import statistics
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import warnings
import sys
from copy import deepcopy
from random import randrange
from sklearn.model_selection import cross_validate, GridSearchCV
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error as MRE
import time
from datetime import date
import math


def predict(coin, predictionTime=1):
    ts = math.floor(time.time())
    print(ts)
    start_date = date.today()
    warnings.filterwarnings('ignore')
    cg = CoinGeckoAPI()
    bitcoin = cg.get_coin_market_chart_range_by_id(
        id=coin, vs_currency='usd', from_timestamp='1420070400', to_timestamp=ts)
    bitcoin_prices = bitcoin.get("prices")
    bitcoin_array_prices = np.array(bitcoin_prices)

    bitcoin_df = pd.DataFrame(bitcoin_array_prices, columns=[
        "UTC_timestamp", "price"])
    # print(bitcoin_df)

    bitcoin_df["UTC_timestamp"] = pd.to_datetime(
        bitcoin_df["UTC_timestamp"], origin='unix', unit='ms')
    # print(bitcoin_df)

    test_df = bitcoin_df.copy(deep=True)

    bitcoin_df.set_index("UTC_timestamp", inplace=True)
    test_df.set_index("UTC_timestamp", inplace=True)
    # print(test_df)

    # plt.figure(figsize=(12, 6))
    # plt.plot(bitcoin_df["price"])
    # plt.xlabel('Date', fontsize=15)
    # plt.ylabel('Price', fontsize=15)
    # # plt.show()

    bitcoin_train = bitcoin_df.copy(deep=True)
    bitcoin_train = bitcoin_train.reset_index()
    # print(bitcoin_train)
    bitcoin_train.dtypes

    regular_dates = bitcoin_train["UTC_timestamp"]

    bitcoin_train["UTC_timestamp"] = bitcoin_train["UTC_timestamp"].map(
        mdates.date2num)
    bitcoin_train.head(5)
    # print(regular_dates)
    # print(type(bitcoin_train))

    X_Train_dates = bitcoin_train["UTC_timestamp"].values
    Y_Train_prices = bitcoin_df["price"].values

    # print(X_Train_dates)

    # Convert to 1d Vector
    X_Train_dates = np.reshape(X_Train_dates, (len(X_Train_dates), 1))
    Y_Train_prices = np.reshape(Y_Train_prices, (len(Y_Train_prices), 1))

    svr_rbf = SVR(kernel='rbf', C=1e5, gamma=0.001)
    svr_rbf.fit(X_Train_dates, Y_Train_prices)

    # plt.figure(figsize=(12, 6))
    # plt.plot(X_Train_dates, Y_Train_prices, color='black', label='Data')
    # plt.plot(regular_dates, svr_rbf.predict(
    #     X_Train_dates), color='red', label='RBF model')
    # plt.xlabel('Date')
    # plt.ylabel('Price')
    # plt.legend()
    # plt.show()

    ##############################################################################
    ##############################################################################
    ##############################################################################
    # 3 Day Forecast Code

    forecast_3 = 3  # number of days ahead to forecast

    prediction_3 = []  # filling list with timedelta values for prediction
    for x in range(forecast_3):
        prediction_3.append(np.datetime64(start_date) -
                            np.datetime64(-(x+1), 'D'))
    # print(prediction_3)

    prediction_3 = np.reshape(prediction_3, (len(prediction_3), 1))
    # feeding in timedelta values to predict future prices
    # print(svr_rbf.predict(prediction_3))

    forecast_dates_3 = []  # filling in list with forecasting dates in a regular format
    for x in range(forecast_3):
        forecast_dates_3.append(np.datetime64(
            start_date) + np.timedelta64(x, 'D'))
    # print(forecast_dates_3)

    plt.figure(figsize=(12, 6))
    plt.plot(forecast_dates_3, svr_rbf.predict(
        prediction_3), color='red', label=coin)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title("3-day Price Projection")
    plt.legend()
    plt.savefig('./static/images/'+coin+'-'+'3'+'.png')
    # plt.show()

    ##############################################################################
    ##############################################################################
    ##############################################################################
    # 5 Day Forecast Code

    forecast_5 = 5  # number of days ahead to forecast

    prediction_5 = []  # filling list with timedelta values for prediction
    for x in range(forecast_5):
        prediction_5.append(np.datetime64(start_date) -
                            np.datetime64(-(x+1), 'D'))
    # print(prediction_5)

    prediction_5 = np.reshape(prediction_5, (len(prediction_5), 1))
    # feeding in timedelta values to predict future prices
    # print(svr_rbf.predict(prediction_5))

    forecast_dates_5 = []  # filling in list with forecasting dates in a regular format
    for x in range(forecast_5):
        forecast_dates_5.append(np.datetime64(
            start_date) + np.timedelta64(x, 'D'))
    print(forecast_dates_5)

    plt.figure(figsize=(12, 6))
    plt.plot(forecast_dates_5, svr_rbf.predict(
        prediction_5), color='red', label=coin)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title("5-day Price Projection")
    plt.legend()
    plt.savefig('./static/images/'+coin+'-'+'5'+'.png')
    # plt.show()

    ##############################################################################
    ##############################################################################
    ##############################################################################
    # 7 Day Forecast Code

    forecast_7 = 7
    prediction_7 = []  # filling list with timedelta values for prediction
    for x in range(forecast_7):
        prediction_7.append(np.datetime64(start_date) -
                            np.datetime64(-(x+1), 'D'))
    # print(prediction_7)

    prediction_7 = np.reshape(prediction_7, (len(prediction_7), 1))
    prediction_7_list = svr_rbf.predict(prediction_7)
    # feeding in timedelta values to predict future prices
    # print(prediction_7_list)

    forecast_dates_7 = []  # filling in list with forecasting dates in a regular format
    for x in range(forecast_7):
        forecast_dates_7.append(np.datetime64(
            start_date) + np.timedelta64(x, 'D'))
    # print(forecast_dates_7)

    plt.figure(figsize=(12, 6))
    plt.plot(forecast_dates_7, svr_rbf.predict(
        prediction_7), color='red', label=coin)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title("7-day Price Projection")
    plt.legend()
    plt.savefig('./static/images/'+coin+'-'+'7'+'.png')
    # plt.show()


# predict('ethereum', 1)
