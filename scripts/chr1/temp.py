import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(nrows=12, ncols=2, figsize=(10,10), sharex=True)

axes[0,0].plot([1,2,3,4])
axes[0,0].set_ylim([0, 10])


plt.savefig('two_example.pdf')

#
#fig2, axes2 = plt.subplots(nrows=10, ncols=1, figsize=(10,10), sharex=True)

##plt.show()
#
#plt.savefig('one_example.pdf')

#def axis_to_fig(axis):
#    fig = axis.figure
#    def transform(coord):
#        return fig.transFigure.inverted().transform(
#            axis.transAxes.transform(coord))
#    return transform
#
#def add_sub_axes(axis, rect):
#    fig = axis.figure
#    left, bottom, width, height = rect
#    trans = axis_to_fig(axis)
#    figleft, figbottom = trans((left, bottom))
#    figwidth, figheight = trans([width,height]) - trans([0,0])
#    return fig.add_axes([figleft, figbottom, figwidth, figheight])
#
#x = np.linspace(-np.pi,np.pi)
#fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
#
#for axis in axes.ravel():
#    axis.set_xlim(-np.pi, np.pi)
#    axis.set_ylim(-1, 3)
#    axis.plot(x, np.sin(x))
#    subaxis = add_sub_axes(axis, [0.2, 0.6, 0.3, 0.3])
#    subaxis.plot(x, np.cos(x))