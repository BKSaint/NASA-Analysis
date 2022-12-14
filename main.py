
mainlog = open("NASA_Log")
ipaddresses = []
try:
    for lines in mainlog:
        x = lines.split("")[0]
        ipaddresses.append(x) 
except:
    print("stop")

print(ipaddresses)





