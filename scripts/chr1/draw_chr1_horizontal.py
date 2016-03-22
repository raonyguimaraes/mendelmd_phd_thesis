
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mlt
from matplotlib.patches import Polygon, Wedge, Rectangle, FancyBboxPatch, BoxStyle


x_lim = 260000000

chr1_size = 249250621

fig = plt.figure(num=None, figsize=(5,6))
# 
plt.ylim([0, 10])
plt.xlim([-10000000, x_lim])
# plt.axes.get_xaxis().set_visible(False)
# plt.axes.get_yaxis().set_visible(False)

# plt.axis('off')
# figure()
# fig = plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
ax = fig.add_subplot(1, 1, 1)
# ax.set_ylabel('hello')
plt.tight_layout()
plt.title('CHR 1')

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



#now add information from a VCF
import vcf

# positions = []
individual_variants = {
	'positions' : [],
	'cadd': {}
}

cadd_values = []
#raw method
vcffile = open('../../data/family/exome_3_eds.var.annotated.vcf')
for line in vcffile:
	if not line.startswith('#'):
		row = line.split('\t')
		chr = row[0].replace('chr', '')
		pos = row[1]
		info = row[7].split(';')

		if chr == '1':
			# positions.append(pos)
			individual_variants['positions'].append(pos)
			
			#check cadd
			for item in info:
				if item.startswith('dbNSFP_CADD_raw'):
					cadd_raw = item.split('=')[1]
					# print 'achou', cadd_raw
					cadd_values.append(float(cadd_raw))
					individual_variants['cadd'][pos] = cadd_raw


			#check qual




		# print row
		# die()


#using pyvcf
# vcf_reader = vcf.Reader(open('../../data/family/exome_3_eds.var.annotated.vcf', 'r'))
# for record in vcf_reader:
# 	if record.CHROM == '1':
# 		positions.append(record.POS)

#now plot all at once:
# print len(positions)

# print positions
ax.plot([2 for x in individual_variants['positions']], individual_variants['positions'], 'g_')


#cadd raw
min_cadd = min(cadd_values)
max_cadd = max(cadd_values)
print min_cadd, max_cadd

# print mlt.colors.Normalize(vmin = min_cadd, vmax = max_cadd)

# a = np.array(cadd_values)

# print a
# heatmap = ax.pcolor(a)
ax.plot([3 for x in individual_variants['cadd']], individual_variants['cadd'].keys(), marker='_')


# ax2 = fig.add_subplot(2,1, 2)

# x = [1, 2, 3, 4]
# y = [1, 4, 9, 6]
# labels = ['Frogs', 'Hogs', 'Bogs', 'Slogs']

# ax2.plot(x, y, 'ro')
# # You can specify a rotation for the tick labels in degrees or with keywords.
# plt.xticks(x, labels, rotation='vertical')
# # Pad margins so that markers don't get clipped by the axes
# plt.margins(0.2)
# # Tweak spacing to prevent clipping of tick-labels
# plt.subplots_adjust(bottom=0.15)

plt.savefig('chr1_variants_horizontal.png')