
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage


from matplotlib.patches import Polygon, Wedge, Rectangle, FancyBboxPatch, BoxStyle


y_lim = 260000000
chr1_size = 249250621

fig = plt.figure(num=None, figsize=(3,6))

# 
plt.ylim([-10000000, y_lim])
plt.xlim([0, 5])
# plt.axes.get_xaxis().set_visible(False)
# plt.axes.get_yaxis().set_visible(False)

# plt.axis('off')
# figure()
# fig = plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
ax = fig.add_subplot(2, 1, 1)

# ax.set_ylabel('hello')
plt.tight_layout()

#draw chromossome region
someX, someY = 1, 0
ax.add_patch(Rectangle((someX - .5, someY - .5), 1, chr1_size, color="black", fill=False, alpha=1))


#### Draw Bands ####

band_colors = {'gneg': '#ffffff', 'gpos50': '#b3b3b3', 'gpos75': '#666666', 'gpos25': '#e5e5e5', 'gpos100': '#000000', 'acen': '#8b2323', 'gvar': '#ffffff', 'stalk': '#cd3333'}

#read bands info to dics
bands_file = open('../draw_chr/ideogram.hg19.txt')
bands_header = bands_file.next().strip().split('\t')
bands = {}
for line in bands_file:
	row = line.strip().split('\t')
	# print row
	chr=row[0].replace('chr', '')
	
	if chr not in bands:
		bands[chr] = []
	
	band = {}
	band['chr_start'] = int(row[1])
	band['chr_end'] = int(row[2])
	band['label'] = row[3]
	band['stain'] =row[4]
	bands[chr].append(band)


# plot bands_chr1

last_band_index = len(bands['1'])
for n, band in enumerate(bands['1']):
	height = band['chr_end'] - band['chr_start']

	# if (n == 0) or (n == last_band_index-1):
		# print 'firt band or last band'
		#draw on side
		#add half circle
		# center = (2.5, band['chr_start'])
		# radius = 0.5
		# theta1=0
		# theta2=180
		# w1 = Wedge(center, radius, theta1, theta2, fc='red')
		# ax.add_patch(w1)

	
	band_center = (band['chr_end'] + band['chr_start']) // 2
	# print band_center
	ax.plot(0.5, band_center, 'r_')

	ax.text(0.25, band_center, band['label'], verticalalignment='center', fontsize=8, horizontalalignment='center',)
	#treat 'acen'
	if band['stain'] == 'acen':
		if band['label'].startswith('p'):
			pts = np.array([[0.5,band['chr_start']], [1.5,band['chr_start']], [1,band['chr_end']]])
		else:
			pts = np.array([[0.5,band['chr_end']], [1.5,band['chr_end']], [1,band['chr_start']]])
		p = Polygon(pts, closed=True, color=band_colors[band['stain']])
		r = Rectangle((0.5,band['chr_start']), 1, height, color='white')
		ax.add_patch(r)

		ax.add_patch(p)

	else:
		ax.add_patch(Rectangle((0.5,band['chr_start']), 1, height, color=band_colors[band['stain']]))

# ax.add_patch(Rectangle((2, 4), 3, chr1_size, 
# 	color="black", fill=False, alpha=1, 
# 	capstyle='round', joinstyle='round',
# 	))

# wedge = Wedge((2, 4), 1, 30, 270, ec="none")
# radius= 0.5
# center = (3, 100000000)
# theta1 = 0
# theta2 = 180
# w1 = Wedge(center, radius, theta1, theta2, fc='black')
# ax.add_artist(w1)
# for n in range(3,21):

# 	center = (n, 100000000)
# 	radius= 10000
# 	theta1 = 0
# 	theta2 = 180
# 	w1 = Wedge(center, radius, theta1, theta2, fc='black')
# 	ax.add_artist(w1)


#start next columor line


# Rotated_Plot = ndimage.rotate(plt, 90)


plt.savefig('chr1.png')