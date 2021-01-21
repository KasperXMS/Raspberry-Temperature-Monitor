#!/usr/bin/env python3
# -*- coding:"utf-8" -*-


"""
    @Author Harter·Liang
    @Date 2021/01/21
    @Version 1.1.2
    @Description Draw the graph of the temperature and time from the database.
    @Upgrades With combined functions, which bring more flexibility, and fix some problems
              related with matplotlib
"""

import matplotlib.pyplot as plt

from dbCon.dataToDB import *


# Depending the package which includes the script dataToDB.py


def getGraphData(tbName, colName):
    # Changing the function for the usage of getting data from database
    graphRawData = getData(tbName, colName)
    # Get the date from the database with the function of package dbCon

    xList = []
    yList = []
    # Save the data

    for content in graphRawData:
        xList.append(content[1])
        yList.append(content[2])
        # Appending the data from the content returned from SQL Query execution

    xList.reverse()
    # Get the right order of the data

    return xList, yList


def drawGraph(contentSource, imgName, timePeriodName):
    # The aim of this function is simplified for drawing the pictures
    xList = contentSource[0]
    yList = contentSource[1]
    # The data source for x and y label data
    plt.xlabel(timePeriodName)
    plt.ylabel("Temperature (Celsius)")
    # X and Y label of the plot fig
    plt.plot(xList, yList, color='green', linewidth=3)
    # Attribute of the pic
    plt.savefig(str(imgName) + ".png")
    # Save the picture
    plt.clf()
    # Clear the picture-cache


def drawGraphTest(tbName, colName, imgName, timePeriodName):
    # Sample of combined functions
    rawContent = getGraphData(tbName, colName)

    drawGraph(rawContent, imgName, timePeriodName)


if __name__ == "__main__":
    drawGraphTest("TEMP_5SEC", "5sec_record_id", "5sec", "Time (seconds)")
    drawGraphTest("TEMP_HOUR", "h_record_id", "hourly", "Time (hour)")

