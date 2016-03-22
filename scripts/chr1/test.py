
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

f, axarr = plt.subplots(1, 3, sharey=False)
axarr[0].plot(x, y)
axarr[0].set_title('1')

axarr[1].scatter(x, y)
axarr[2].scatter(x, y)
