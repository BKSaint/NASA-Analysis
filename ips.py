import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from collections import *

mainlog = open("FixedNASALog")


count = 0
dates = []
ipaddresses = []
timeaxis = [('00', ':00'), ('00', ':30'), ('01', ':00'), ('01', ':30'), ('02', ':00'), ('02', ':30'), ('03', ':00'), ('03', ':30'), ('04', ':00'), ('04', ':30'), ('05', ':00'), ('05', ':30'), ('06', ':00'), ('06', ':30'), ('07', ':00'), ('07', ':30'), ('08', ':00'), ('08', ':30'), ('09', ':00'), ('09', ':30'), ('10', ':00'), ('10', ':30'), ('11', ':00'), ('11', ':30'), ('12', ':00'), ('12', ':30'), ('13', ':00'), ('13', ':30'), ('14', ':00'), ('14', ':30'), ('15', ':00'), ('15', ':30'), ('16', ':00'), ('16', ':30'), ('17', ':00'), ('17', ':30'), ('18', ':00'), ('18', ':30'), ('19', ':00'), ('19', ':30'), ('20', ':00'), ('20', ':30'), ('21', ':00'), ('21', ':30'), ('22', ':00'), ('22', ':30'), ('23', ':00'), ('23', ':30')]

#153.103.3.51 - - [28/Jul/1995:12:02:52 -0400] "GET /shuttle/missions/sts-67/mission-sts-67.html HTTP/1.0" 200 21523


try:
    for lines in mainlog:
        x = lines.split(" ")[0]
        y = lines.split("[")[1]
        y = y.split("/")[0]
        if y == "13" and x == 'piweba3y.prodigy.com':
            z = lines.split(" ")[3]
            z = z.split("1995:")[1]
            z = z.split(" ")[0]
            z = z.split(":")
            z = z[0],":",z[1]
            ipaddresses.append(z)
        count += 1
except:
    print(f"discontinued at {count}")
    print(lines)

mainlog.close()
x = []
y = []
data = []
xb = []
yb = []

a = Counter(ipaddresses).keys()
b = Counter(ipaddresses).values()



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

print(xb)
print(yb)

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

