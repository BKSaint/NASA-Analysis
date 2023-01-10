# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np
# from collections import *

# mainlog = open("FixedNASA_Log")

# count = 0
# dates = []
# date = []
# files = []

# try:
#     #--DATES--
#     for lines in mainlog:
#         y = lines.split(" ")[6]
#         if y == "/shuttle/countdown/liftoff.html": #Each split finds a unique part of the example above to split it by
#             y = lines.split(" ")[3]
#             y = y.split(":")[0]
#             y = y.split("[")[1]
#             y = y.split("/1995")[0]
#             dates.append(y)
#         count += 1
# except:
#     print(f"discontinued at {count}")
#     print(lines)

# mainlog.close()

# commfiles = Counter(dates).most_common(20)
# commfiles.sort()

# count = 0
# for i in commfiles:
#     files.append(i[0])
#     date.append(i[1])

# plt.plot(files, date)
# plt.xticks(rotation=30)
# plt.show()
