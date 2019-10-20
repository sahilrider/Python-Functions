#!/usr/bin/env python3

""" 
This an example using simple linear regression to predict the stock market 
based on S&P500 dataset.

Author:
Neda Peyrone 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, model_selection
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


def get_data(filename):
    return pd.read_csv(filename)


def linear_model(X, y):
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

    # Training
    clf = LinearRegression()
    clf.fit(X_train, y_train)

    # Testing
    confidence = clf.score(X_test, y_test)
    print("confidence: ", confidence)

    pred = clf.predict(X_test)
    show_plot(X_test, y_test, pred)

    return clf


def eval_prediction(pred, X_forecast):
    y_forecast = pred.predict(X_forecast)
    return y_forecast


def show_plot(X_test, y_test, pred):
    plt.scatter(X_test, y_test, c='red')
    plt.plot(X_test, pred, color='blue', linewidth=3)
    plt.xlabel('exp.')
    plt.ylabel('pred.')
    plt.show()


if __name__ == '__main__':
    df = get_data("^GSPC.csv")
    df = df[['Adj Close']]

    forecast_out = int(30)
    df['Prediction'] = df[['Adj Close']].shift(-forecast_out)

    X = np.array(df.drop(['Prediction'], 1))
    X = preprocessing.scale(X)

    X_forecast = X[-forecast_out:]
    X = X[:-forecast_out]

    y = np.array(df['Prediction'])
    y = y[:-forecast_out]

    pred = linear_model(X, y)
    y_forecast = eval_prediction(pred, X_forecast)
    print(y_forecast)
