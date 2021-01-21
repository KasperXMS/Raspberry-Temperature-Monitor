#!/usr/bin/env python3
# -*- coding:"utf-8 -*-
import pymysql
import datetime
import random
import time

'''
    @Author Harter·Liang
    @Date 2021/01/19
    @Version 1.0
    @Description Provide some basic functions for SQL queries.
'''

conn = pymysql.connect(host='127.0.0.1', port=3306, user='abc', passwd='shenxm345',
                       db='temprecord', charset='utf8')


# Connecting to the database

def closeConn():
    conn.close()


# Close the connection of the session


def getData(tbName):
    idSeq = 0
    date = ""
    temp = 36.123

    curr = conn.cursor()
    dataResList = []

    selectQuery = "SELECT * FROM %s ORDER BY 5sec_record_id DESC LIMIT 0,8" % tbName
    # Select the data from tables
    curr.execute(selectQuery)

    dataResult = curr.fetchall()
    # Fetch all data received
    for res in dataResult:
        idSeq = res[0]
        # date = res[1].strftime("%a,%b,%d %H:%M")
        date = res[1].strftime("%H:%M:%S")
        temp = res[2]

        dataResList.append((idSeq, date, temp))

    return dataResList


def insertData(tbName, temp):
    curr = conn.cursor()

    currTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # A proper format for datetime

    insertQuery = "INSERT INTO " + str(tbName) + " (record_time, temp_value) VALUES(%s,%s)"
    # Insert into the columns we want

    insertPayload = (currTime, temp)
    # The data

    try:
        curr.execute(insertQuery, insertPayload)

        conn.commit()

        print("The insertion for table %s is succeed with data %s %s" % (tbName, currTime, temp))

    except RuntimeError as err:
        # For unexpected errors
        print("The insertion for table %s is failed" % tbName)

        print(err)

        conn.rollback()
        # As if nothing happened for the table


def refreshTable(tbName):
    # Clear the table when it stored so many data
    curr = conn.cursor()

    refreshQuery = "TRUNCATE TABLE " + str(tbName)

    try:
        curr.execute(refreshQuery)

        print("The table %s refreshing succeed" % tbName)

        conn.commit()

    except RuntimeError as err:
        print(err)

        conn.rollback()


def getCount(tbName):
    curr = conn.cursor()

    selectQuery = "SELECT COUNT(*) FROM %s" % tbName
    # Select the data from tables
    curr.execute(selectQuery)

    numResult = curr.fetchall()

    return numResult[0][0]


# Some samples of how to use it:

# insertData("TEMP_5SEC", 35.6)
# getData("TEMP_5SEC")
# refreshTable("TEMP_5SEC")
# closeConn()


def test():
    while True:
        temp = round(random.uniform(36, 38), 3)
        insertData("TEMP_5SEC", temp)
        time.sleep(2)

        count = getCount("TEMP_5SEC")

        if count >= 30:
            refreshTable("TEMP_5SEC")


if __name__ == '__main__':
    test()
