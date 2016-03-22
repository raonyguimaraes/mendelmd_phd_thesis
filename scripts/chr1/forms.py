import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
rect1 = matplotlib.patches.Rectangle((-200,-100), 400, 200, color='yellow')
rect2 = matplotlib.patches.Rectangle((0,150), 300, 20, color='red')
rect3 = matplotlib.patches.Rectangle((-300,-50), 40, 200, color='#0099FF')
circle1 = matplotlib.patches.Circle((-200,-250), radius=90, color='#EB70AA')
pts = np.array([[0,0], [4,0], [2,np.sqrt(5**2 - 2**2)]])
p = Polygon(pts, closed=True)

ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)
ax.add_patch(circle1)
ax.add_patch(p)

plt.xlim([-400, 400])
plt.ylim([-400, 400])
plt.show()