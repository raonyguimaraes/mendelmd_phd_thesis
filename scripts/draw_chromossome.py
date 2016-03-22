#draw chromossome 1..22,X,Y,MT
import matplotlib.pyplot as plt

plt.axes()

circle = plt.Circle((0, 0), radius=0.75, fc='y')
# plt.gca().add_patch(circle)

plt.axis('scaled')



rectangle = plt.Rectangle((10, 10), 100, 100, fc='r')
plt.gca().add_patch(rectangle)


import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
# rect1 = matplotlib.patches.Rectangle((-200,-100), 400, 200, color='yellow')
rect2 = matplotlib.patches.Rectangle((0,0), 300, 20, color='red')
# rect3 = matplotlib.patches.Rectangle((0,-50), 40, 200, color='#0099FF')
circle1 = matplotlib.patches.Circle((-200,-250), radius=90, color='#EB70AA')
circle2 = matplotlib.patches.Circle((0,150), radius=5, color='#EB70AA')

# ax.add_patch(rect1)
ax.add_patch(rect2)
# ax.add_patch(rect3)
ax.add_patch(circle1)
ax.add_patch(circle2)

plt.xlim([-400, 400])
plt.ylim([-400, 400])
# plt.show()


# plt.show()
plt.savefig('chr1.png')