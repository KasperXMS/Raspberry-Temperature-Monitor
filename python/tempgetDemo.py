import pymysql
import threading
import time
import random

"""
    @author Kasper X.
    @date 2021/1/19
    @desc Obtain the data from sensor and insert data to MySQL database.
"""

def spawnRandomTemp():
    """
    This is a test method which generate random values and replace the function of getTempValue().
    :return: a float number
    """
    return random.randrange(31, 36) + random.randrange(0, 8) / 8

def getTempValue():
    """
    This method read the file containing the value from sensor, and parse a 3-digit float value.
    :return: float type temperature value in Celsius 
    """
    # Where the initial value stored at.
    # often the file is located under /sys/bus/w1/["a string you need to obtain from the system"]/w1_slave
    tfile = open("/sys/bus/w1/devices/28-0300a279d1d3/w1_slave")
    text = tfile.read()
    tfile.close()

    #parse the temperature value
    secondline = text.split("\n")[1]
    tpd = secondline.split(" ")[9]
    tmp = float(tpd[2:])
    tmp = tmp / 1000
    return tmp

def getDateTime():
    """
    get current system date and time
    :return: date time string in xxxx-xx-xx xx:xx:xx format
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def insertSQL(sql):
    """
    conduct a specific SQL insert query
    :param sql: SQL query string
    :return: none
    """
    # start connection
    conn = pymysql.connect(user="your mysql username",
                           password="your password",
                           host="your mysql database host",
                           database="your designated database name")
    cursor = conn.cursor()

    try:
        # attempt to execute the query
        cursor.execute(sql)
        conn.commit()
        print(sql)
    except:
        print("action failed")
        conn.rollback()

    conn.close()

def onInsertion():
    """
    action of insertion
    :return: none
    """
    timer = 0
    while True:
        # insert hourly data which will be kept pernamently
        if timer == 1800:
            timer = 0
            insertSQL("INSERT INTO TEMP_HOUR (h_record_time, h_temp_value) VALUES ('" + getDateTime() + "', '" + str(getTempValue()) + "')")

        # insert data for every 5 sec which will be kept for 1 hour
        elif timer % 5 == 0:
            insertSQL("INSERT INTO TEMP_5SEC (5sec_record_time, 5sec_temp_value) VALUES ('" + getDateTime() + "', '" + str(getTempValue()) + "')")

        # timer ticks
        time.sleep(1)
        timer = timer + 1


def onTimeLimitTruncateTable(timeLimit):
    """
    Truncate the 5-sec table in a specific period
    :param timeLimit: the length of the period to truncate the table
    :return: none
    """
    timer = 0
    while True:
        if timer == timeLimit:
            timer = 0
            conn = pymysql.connect(user="your mysql username",
                                   password="your password",
                                   host="your mysql database host",
                                   database="your designated database name")
            cursor = conn.cursor()
            sql = "TRUNCATE TABLE TEMP_5SEC"

            try:
                cursor.execute(sql)
                conn.commit()
                print(sql)
            except:
                print("action failed")
                conn.rollback()

            conn.close()

        time.sleep(1)
        timer = timer + 1

class OnInsertionThread(threading.Thread):
    """
    Create a thread to independently run insert methods
    """
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        onInsertion()

class OnTimeLimitTruncateTableThread(threading.Thread):
    """
    Create a thread to independently run truncate method
    """
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        onTimeLimitTruncateTable(3600)

Thread1 = OnInsertionThread()
Thread2 = OnTimeLimitTruncateTableThread()
try:
    Thread1.start()
    Thread2.start()
except:
    print("thread create error!")



