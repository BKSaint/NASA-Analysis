from collections import *
mainlog = open("NASA_Log")
ipaddresses = []
dates = []
files = []

try:
    for lines in mainlog:
        # x = lines.split(" ")[0]
        # ipaddresses.append(x)
        # y = lines.split(" ")[3]
        # y = y.split(":")[0]
        # dates.append(y)
        # z = lines.split('"')[1]
        # z = z.split(".")[1]
        # z = z.split(" ")[0]
        # files.append(z)
        z = lines.split('"')[1]
        z = z.split('"')[0]
        z = z.split(" ")[1]
        files.append(z)

except:
    print("stop")

print(Counter(ipaddresses).most_common(3))
print(Counter(dates).most_common(3))
print(Counter(files).most_common(5))