import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from collections import *

mainlog = open("FixedNASALog")

# --EXAMPLE LOG-- #
#slip3-24.dialin.uic.edu - - [28/Jul/1995:12:02:51 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204

x = ""
print('Choices: "Time", "Date", "Activity"')
branch = input("Choice: ")

frequency = 20

# # --TIME--
def time(date):
    count = 0
    times = []
    for lines in mainlog:
        if date in lines:
            x = lines.split(" ")[3] #Each split finds a unique part of the example above to split it by
            x = x.split("1995:")[1]
            x = x.split(" ")[0]
            x = x.split(":")[0]
            times.append(x)
        
            x = lines.split(" ")[6] #Each split finds a unique part of the example above to split it by
            y = dates[count],x
            files.append(x)
            count += 1
        count += 1        
    return times

# # --DATES--
def date():
    count = 0
    dates = []
    for lines in mainlog: 
        x = lines.split(" ")[3] #Each split finds a unique part of the example above to split it by
        x = x.split(":")[0]
        x = x.split("[")[1]
        x = x.split("/Jul/1995")[0]
        x = int(x)
        dates.append(x)
    count += 1
    return dates

def ipadresses(date, chosenip, time=None):
    count = 0
    activity = []
    for lines in mainlog:
            x = lines.split(" ")[0]
            y = lines.split("[")[1]
            y = y.split("/")[0]
            if y == date and x == chosenip:
                z = lines.split(" ")[3]
                z = z.split("1995:")[1]
                z = z.split(" ")[0]
                z = z.split(":")
                z = z[0],":",z[1]
                activity.append(z)


            
    count += 1
    return activity

try:
    if branch == "time":
        chosentime = input("Choose a date of July (Ex: 13/Jul): ")
        times = time(chosentime)
    elif branch == "date":
        dates = date()
    elif branch == "activity":
        chosenactivity = input("Choose a date of July (Ex: 13): ")
        chosenip = input("Choose an certain ip or leave blank")
        activity = ipadresses(chosenactivity, chosenip)
    
except:
    print('discontinued')

mainlog.close()

xb = []
yb = []
ticks = []

def filegraph():

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


def timegraph():
    fulldict = (Counter(times).most_common(24))
    count = 0
    for i in fulldict:
        fulldict[count] = list(i)
        if '00' in i[0]:
            fulldict[count][0] = '24'
        count += 1
    
    fulldict = sorted(fulldict)
    for i in fulldict:
        xb.append(i[0])
        yb.append(i[1])

    print(xb)
    print(yb)
    plt.rcParams["font.family"] = 'monospace' 
    ax = plt.axes()
    ax.set_facecolor('black')
    plt.grid(color="#313631")
    plt.plot(xb, yb , alpha=.8, marker="o", markersize="10", color="red", linewidth="5") 
    plt.xlabel("Hours of July 13th", size="15")
    plt.ylabel("Activity", size="15")
    plt.show()

def dategraph():
    keys = Counter(dates).keys() #Keys: "Jul/01"
    values = Counter(dates).values() #Values: "12000"

    for i in keys:
        xb.append(i)

    for i in values:
        yb.append(i)

    for i in x: #This makes the X ticks of the graph go in multiples of 5
        if (int(i) % 7) == 0:
            ticks.append(i)
        else:
            ticks.append('')

    plt.rcParams["font.family"] = 'monospace' 
    ax = plt.axes()
    ax.set_facecolor('black')
    plt.grid(color="#313631")
    plt.plot(xb, yb , alpha=.8, marker="o", markersize="10", color="red", linewidth="5") 
    plt.xlabel("Dates of July", size="15")
    plt.ylabel("Activity", size="15")
    # plt.xlim([0, max(x)])
    # plt.ylim([0, max(y)])
    plt.show()

def activitygraph():
    timeaxis = [('00', ':00'), ('00', ':30'), ('01', ':00'), ('01', ':30'), ('02', ':00'), ('02', ':30'), ('03', ':00'), ('03', ':30'), 
                ('04', ':00'), ('04', ':30'), ('05', ':00'), ('05', ':30'), ('06', ':00'), ('06', ':30'), ('07', ':00'), ('07', ':30'), 
                ('08', ':00'), ('08', ':30'), ('09', ':00'), ('09', ':30'), ('10', ':00'), ('10', ':30'), ('11', ':00'), ('11', ':30'), 
                ('12', ':00'), ('12', ':30'), ('13', ':00'), ('13', ':30'), ('14', ':00'), ('14', ':30'), ('15', ':00'), ('15', ':30'), 
                ('16', ':00'), ('16', ':30'), ('17', ':00'), ('17', ':30'), ('18', ':00'), ('18', ':30'), ('19', ':00'), ('19', ':30'), 
                ('20', ':00'), ('20', ':30'), ('21', ':00'), ('21', ':30'), ('22', ':00'), ('22', ':30'), ('23', ':00'), ('23', ':30')]
    x = []
    a = Counter(activity).keys()
    b = Counter(activity).values()
    print(a)
    print(b)
    for i in a:
        if int(i[2]) < 30:
            x.append((i[0],":00"))
        else:
            x.append((i[0],":30"))


    data = (Counter(x).most_common(50))
    for i in timeaxis:
        if i not in x:
            data.append((i, 0))

    data = sorted(data)
    count = 0
    for i in data:
        print(i)
        xb.append(str(i[0][0]) + str(i[0][1]))
        yb.append(i[1])

    plt.rcParams["font.family"] = 'monospace' 
    ax = plt.axes()
    ax.set_facecolor('black')
    plt.grid(color="#313631")
    plt.plot(xb, yb , alpha=.8, marker="o", markersize="10", color="red", linewidth="5") 
    plt.xlabel("Dates of July", size="15")
    plt.ylabel("Activity", size="15")
    # plt.xlim([0, max(x)])
    # plt.ylim([0, max(y)])
    plt.show()

if branch == "time":
    timegraph()
elif branch == "date":
    dategraph()
elif branch == "activity":
    activitygraph()