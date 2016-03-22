# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:21:21 2015

@author: raony
"""

import numpy
from matplotlib import pyplot as plot
 
# Prepare the data
t = numpy.linspace(-numpy.pi, numpy.pi, 1024)
s = numpy.random.randn(2, 256)
 
#
# Do the plot
#
grid_size = (5, 2)
 
# Plot 1
plot.subplot2grid(grid_size, (0, 0), rowspan=2, colspan=2)
plot.plot(t, numpy.sinc(t), c= '#000000')
 
# Plot 2
plot.subplot2grid(grid_size, (2, 0), rowspan=3, colspan=1)
plot.scatter(s[0], s[1], c= '#000000')
 
# Plot 2
plot.subplot2grid(grid_size, (2, 1), rowspan=3, colspan=1)
plot.plot(numpy.sin(2 * t), numpy.cos(0.5 * t), c= '#000000')
 
# Automagically fits things together
plot.tight_layout()
 
# Done !
plot.show()