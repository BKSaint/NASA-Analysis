


# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np
# from collections import *

# mainlog = open("FixedNASA_Log")


# count = 0

# dates = []
# ipaddresses = []


# try:
#     for lines in mainlog:
#         #--IP ADDRESSES--
#         x = lines.split(" ")[0]
#         ipaddresses.append(x)
#         count += 1
# except:
#     print(f"discontinued at {count}")

# mainlog.close()
# x = []
# y = []

# z = Counter(ipaddresses).most_common(20)


# for i in z:
#     x.append(i[0])
#     y.append(i[1])

# plt.plot(x, y)
# plt.xticks(rotation=30)
# plt.xlabel("Date")
# plt.ylabel("Activity")
# plt.show()



