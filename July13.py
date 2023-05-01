import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from collections import *

mainlog = open("FixedNASALog")
#slip3-24.dialin.uic.edu - - [28/Jul/1995:12:02:51 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204

a = int
b = int
count = 0
dates = []
ipaddresses = []
jul = []
files = []
time = []
xb = []
yb = []

def filetypes():

    xb = []
    yb = []

    xp = []
    yp = []

    # keys = Counter(dates).keys()
    # values = Counter(dates).values()

    # keysf = Counter(files).keys()
    # valuesf = Counter(files).values()

    commfiles = Counter(files).most_common(20)
    print(commfiles)


    # for i in keys:
    #     xp.append(i)

    # for i in values:
    #     yp.append(i)

    
    count = 0
    for i in Counter(files).most_common(9): 
        if count <= 4:
            xb.append(i[0]) #This is to seperate the graph into two graphs, to be visually more appealing
            yb.append(i[1])
        else:
            xp.append(i[0])
            yp.append(i[1])
        count += 1

    xb.remove('/images/NASA-logosmall.gif')
    yb.remove(12087)
    yaxis = [1000, 2000, 3000, 4000, 5000, 6000, 7000] # Y values


    plt.rcParams["font.family"] = 'monospace' 
    ax = plt.axes()
    plt.bar(xb, yb, color="red", alpha=.8)
    ax.set_facecolor(color='black')
    plt.xticks(rotation=10, size='8')
    plt.yticks(yaxis) #Makes the bar graphs even

    # plt.bar(xp, yp)
    # ax.set_facecolor(color='black')
    # plt.xticks(rotation=45)
    # plt.yticks(yaxis)
    plt.show()

def time():
    fulldict = (Counter(files).most_common(24))
    count = 0
    for i in fulldict:
        fulldict[count] = list(i)
        count += 1
    
    fulldict[16][0] = '24'
    fulldict = sorted(fulldict)
    for i in fulldict:
        xb.append(i[0])
        yb.append(i[1])

    plt.rcParams["font.family"] = 'monospace' 
    ax = plt.axes()
    ax.set_facecolor('black')
    plt.grid(color="#313631")
    plt.plot(xb, yb , alpha=.8, marker="o", markersize="10", color="red", linewidth="5") 
    plt.xlabel("Hours of July 13th", size="15")
    plt.ylabel("Activity", size="15")
    plt.show()

try:
    # # --DATES--
    for lines in mainlog:
        if "13/Jul/1995" in lines:
            count += 1
            x = lines.split(" ")[3] #Each split finds a unique part of the example above to split it by
            x = x.split("1995:")[1]
            x = x.split(" ")[0]
            x = x.split(":")[0]
            dates.append(x)
            jul.append(lines)
except:
    print(f"discontinued at {count}")
    print(lines)

mainlog.close()
count = 0

try:
    for items in jul:
    # --TIME--    
        x = items
        x = x.split(" ")[3] #Each split finds a unique part of the example above to split it by
        x = x.split("1995:")[1]
        x = x.split(" ")[0]
        x = x.split(":")[0]
        files.append(x)
        count += 1

    #  # --FILE TYPES-- 
    #     x = items
    #     x = x.split(" ")[6] #Each split finds a unique part of the example above to split it by
    #     y = dates[count],x
    #     files.append(x)
    #     count += 1
except:
    print(items)
    print(count)

time()

