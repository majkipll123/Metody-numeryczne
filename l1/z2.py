import matplotlib.pyplot as plt
import numpy as np

rg = np.arange(0, 100, 1)

x = 0.1 
list = []

for i in rg:
    x = 3.5 * x * (1 - x)
    list.append(x)

plt.scatter(rg,list)
plt.show()