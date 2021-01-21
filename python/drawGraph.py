import matplotlib.pyplot as plt
import time
import dataToDB

'''
    @Author Harter·Liang
    @Date 2021/01/20
    @Version 1.0
    @Description Plot the line chart of temperature change using matplotlib
'''

# Get the dataset
res = dataToDB.getData("TEMP_5SEC")

xList = []
yList = []

# add data to list
for content in res:
    xList.append(content[1])
    yList.append(content[2])

# since data is ordered in most recent added, reversion is needed
xList.reverse()

# plot and save the image
plt.xlabel("Time (Second)")
plt.ylabel("Temperature (Celsius)")
plt.plot(xList, yList, color='green', linewidth=3)
plt.savefig("TestFig.png")
