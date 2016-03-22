
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
fig, ax = plt.subplots()

# y_lim = 260000000
plt.ylim([0, 25])
plt.xlim([0, 21])

for n in range(1,21):
	center = [n,0]
	print float(n)/100
	fancybox = mpatches.FancyBboxPatch(
        center, 0.5, 20,
        boxstyle=mpatches.BoxStyle("Round", pad=0.2))

	ax.add_patch(fancybox)

plt.savefig('round_corner.png')