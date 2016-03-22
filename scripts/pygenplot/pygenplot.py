# -*- coding: utf-8 -*-
"""
Pygenplot

This is a library to plot genome dara in a plot.
"""
import numpy as np
import matplotlib.pyplot as plt


class Pygenplot():
    def __init__(self):
        self.data = []
        self.n_col = 1
        self.n_row = 24
        self.n_tracks = 2
        self.n_items = self.n_col * self.n_row
        
        print 'config1', self.n_col, self.n_col, self.n_items
        
        
        
    def main(self):
        #start plot
    
        # Simple data to display in various forms
        x = np.linspace(0, 2 * np.pi, 400)
        y = np.sin(x ** 2)

        f, ax_arr = plt.subplots(nrows=self.n_row, 
                                 ncols=self.n_col, 
                                 figsize=(self.n_row,self.n_col))
#
#        for n_row in range(0, self.n_row):
#            print 'n_row', n_row
#        ax_arr[0,0].plot(x, y)
#        ax_arr[0,0] =  plt.subplots(10,1)
#        ax_arr[0,0] = plt.subplots(nrows=10, ncols=1,figsize=(10,1))
#        ax_arr[0,0].plot(x,y)       
#                print 'n_col', n_col
            
        # Three subplots sharing both x/y axes
#        f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)
#        ax1.plot(x, y)
#        ax1.set_title('Sharing both axes')
#        ax2.scatter(x, y)
#        ax3.scatter(x, 2 * y ** 2 - 1, color='r')
        # Fine-tune figure; make subplots close to each other and hide x ticks for
        # all but bottom plot.
#        f.subplots_adjust(hspace=0)
#        plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
        
        
        

#        ax = plt.subplot2grid((2,2),(0, 0))
#        ax = plt.subplot(2,2,0)
#        ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
#        ax2 = plt.subplot2grid((3,3), (1,0), colspan=3)
#        ax3 = plt.subplot2grid((3,3), (1, 2), rowspan=1)
#        ax4 = plt.subplot2grid((3,3), (2, 0))
#        ax5 = plt.subplot2grid((3,3), (2, 1))
                
        plt.show()

        #draw ideogram
        #insert data from vcf

if __name__ == "__main__":
    pygenplot = Pygenplot()
    pygenplot.main()