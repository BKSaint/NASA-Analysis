import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from collections import *

mainlog = open("FixedNASALog")


count = 0
true = []
false = []
#153.103.3.51 - - [28/Jul/1995:12:02:52 -0400] "GET /shuttle/missions/sts-67/mission-sts-67.html HTTP/1.0" 200 21523

try:
    #--FILES--
    for lines in mainlog:
        x = lines.split(" ")[6] #Each split finds a unique part of the example above to split it by
        if x.startswith("/"):
            true.append(x)
        else:
            false.append((x, count))
        count += 1
except:
    print(f"discontinued at {count}")
    print(lines)


print(len(true))
print((false))
