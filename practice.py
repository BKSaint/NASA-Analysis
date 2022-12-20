import matplotlib as mpl                                                                                                                                                                                                                                                                                                                                                                                                     aaaa
import matplotlib.pyplot as plt
import numpy as npy
from random import randint

x = []
for i in range(5):
    x.append(randint(1,100))


y = [20, 40, 60, 80, 100]

plt.subplot(3, 1, 1)
plt.plot(x,y)

plt.subplot(3, 1, 2)
plt.hist(x)

plt.subplot(3, 1, 3)
plt.pie(y)

plt.show()



