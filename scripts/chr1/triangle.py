import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
pts = np.array([[0,0], [4,0], [2,4]])
p = Polygon(pts, closed=True)
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(0,4)
ax.set_ylim(0,5)
plt.show()