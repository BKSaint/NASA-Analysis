import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from collections import *

mainlog = open("FixedNASALog")

count = 0

dates = []
ipaddresses = []
ticks = []
#153.103.3.51 - - [28/Jul/1995:12:02:52 -0400] "GET /shuttle/missions/sts-67/mission-sts-67.html HTTP/1.0" 200 21523

try:
    #--DATES--
    for lines in mainlog:
        
        x = lines.split(" ")[3] #Each split finds a unique part of the example above to split it by
        x = x.split(":")[0]
        x = x.split("[")[1]
        x = x.split("/Jul/1995")[0]
        x = int(x)
        dates.append(x)
        count += 1
except:
    print(f"discontinued at {count}")
    print(lines)

mainlog.close() #Closes the log file to save RAM
x = []
y = []


keys = Counter(dates).keys() #Keys: "Jul/01"
values = Counter(dates).values() #Values: "12000"


for i in keys:
    x.append(i)

for i in values:
    y.append(i)

for i in x:
    if (int(i) % 7) == 0:
        ticks.append(i)
    else:
        ticks.append('')

plt.rcParams["font.family"] = 'monospace' 
ax = plt.axes()
ax.set_facecolor('black')
plt.grid(color="#313631")
plt.plot(x, y , alpha=.8, marker="o", markersize="10", color="red", linewidth="5") 
plt.xlabel("Dates of July", size="15")
plt.ylabel("Activity", size="15")
# plt.xlim([0, max(x)])
# plt.ylim([0, max(y)])
plt.show()

