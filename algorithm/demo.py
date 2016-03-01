import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 256)
c, s = np.cos(x), np.sin(x)

plt.plot(x,c)
plt.plot(x,s)

plt.show()
