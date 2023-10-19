import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1.5, 0.01)
y = np.cos(x) -  (3 * np.sin(np.tan(x) - 1))

plt.plot(x, y)
plt.show()