#!/usr/bin/env python3

""" 
This an example using K nearest neighbors (KNN) to 
predict the stock market based on S&P500 dataset.

Author:
Neda Peyrone
"""
import pandas as pd
import numpy as np
from math import sqrt

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


def get_data(filename):
    return pd.read_csv(filename)


def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=7)

    clf = KNeighborsRegressor(n_neighbors=51, weights='uniform', algorithm='auto')
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)

    # print(pred)

    r2 = r2_score(y_test, pred)
    rmse = sqrt(mean_squared_error(y_test, pred))
    print ("KNN: r2 %f, RMSE %f" % (r2, rmse))

    show_plot(X_test, y_test, pred)

    return clf


def compute_test(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    k_range = range(1, 61)
    scores = []

    for K_value in k_range:
        neigh = KNeighborsRegressor(n_neighbors=K_value, weights='uniform', algorithm='auto')
        neigh.fit(X_train, y_train)
        pred = neigh.predict(X_test)
        scores.append(neigh.score(X_test, y_test))

        r2 = r2_score(y_test, pred)
        rmse = sqrt(mean_squared_error(y_test, pred))
        print ("KNN: r2 %f, RMSE %f" % (r2, rmse), "% for K-Value:", K_value)

    plt.figure()
    plt.xlabel('k')
    plt.ylabel('accuracy')
    plt.scatter(k_range, scores)
    plt.xticks([0,5,10,15,20,25,30,35,40,45,50,55,60])
    plt.show()


def eval_prediction(pred, X_forecast):
    y_forecast = pred.predict(X_forecast)
    return y_forecast


def show_plot(X_test, y_test, pred):
    plt.scatter(X_test, pred, c='red')
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

    compute_test(X, y)
