# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np
# from collections import *

# mainlog = open("FixedNASA_Log")


# count = 0

# dates = []
# ipaddresses = []
# data = []
# #153.103.3.51 - - [28/Jul/1995:12:02:52 -0400] "GET /shuttle/missions/sts-67/mission-sts-67.html HTTP/1.0" 200 21523


# try:
#     for lines in mainlog:
#         x = lines.split(" ")[0]
#         y = lines.split("[")[1]
#         y = y.split("/")[0]
#         if y == "13" and x == 'piweba3y.prodigy.com':
#             z = lines.split(" ")[3]
#             z = z.split("1995:")[1]
#             z = z.split(" ")[0]
#             z = z.split(":")
#             z = z[0],":",z[1]
#             data.append(z)
#         count += 1
# except:
#     print(f"discontinued at {count}")
#     print(lines)

# mainlog.close()
# x = []
# y = []
# w = []

# a = Counter(data).keys()
# print(a)
# b = Counter(data).values()
# print(b)



# for i in a:
#     if int(i[2]) < 30:
#         x.append((i[0],":00"))
#     else:
#         x.append((i[0],":30"))


# print(Counter(x))

# for i in x:
#     x.append(i[0])
#     w.append(i[1])


# plt.bar(x, y)
# plt.xticks(rotation=30)
# plt.show()



