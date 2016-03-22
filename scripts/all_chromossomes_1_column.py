"""Draw all Human Chromossomes
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


# Simple data to display in various forms
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

n_row = 2
n_col = 12

chr_list = ['1', '2', '3', '4', '5', 
	'6', '7', '8', '9', '10', 
	'11', '12', '13', '14', '15', 
	'16', '17', '18', '19', '20', 
	'21', '22', 'X', 'Y', 'MT']
# print chr_list

def set_title_chr():
	chr_counter = 0
	for row_counter in range(0,n_row):
		for col_counter in range(0,n_col):
			# print row_counter, col_counter
			axarr[row_counter, col_counter].set_title(chr_list[chr_counter])
			chr_counter += 1
plt.close('all')

#get chromossome sizes
chr_sizes = {}
chr_sizes_file = open('draw_chr/hg19.chrom.canonical.sizes')
for line in chr_sizes_file:
	row = line.strip().split('\t')
	# print row
	chr = row[0].replace('chr', '')
	size = row[1]
	chr_sizes[chr] = size

# print chr_sizes

#START PLOT
# Four axes, returned as a 2-d array
f, axarr = plt.subplots(n_row, n_col)

#loop all chromossomes
chr_counter = 0
for row_counter in range(0,n_row):
	for col_counter in range(0,n_col):
		actual_chr = chr_list[chr_counter]
		
		chr_counter += 1
		chr_size = chr_sizes[actual_chr]
		# print actual_chr, chr_size
		print row_counter, col_counter
		# axarr[row_counter, col_counter].plt.axis('off')
		axarr[row_counter, col_counter].axes.get_xaxis().set_visible(False)
		axarr[row_counter, col_counter].axes.get_yaxis().set_visible(False)

		# axarr[row_counter, col_counter].add_patch(Rectangle((0 - .1, 0 - .1), 0.2, chr_size, fill=None, alpha=1))



# axarr[0, 0].plot(x, y)
# # axarr[0, 0].set_title('Axis [0,0]')
# axarr[0, 1].scatter(x, y)
# # axarr[0, 1].set_title('Axis [0,1]')
# axarr[1, 0].plot(x, y ** 2)
# # axarr[1, 0].set_title('Axis [1,0]')
# axarr[1, 1].scatter(x, y ** 2)
# axarr[1, 1].set_title('Axis [1,1]')

# set_title_chr()

# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
# plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
# plt.setp([a.get_xticklabels() for a in axarr[1, :]], visible=False)
# plt.setp([a.get_yticklabels() for a in axarr[:, 0]], visible=False)
# plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

# Four polar axes
# plt.subplots(2, 2, subplot_kw=dict(polar=True))

# plt.show()

plt.savefig('allchromossomes_1_column.png')