import numpy as np
import matplotlib.pyplot as plt


from collections import OrderedDict
#http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/chromInfo.txt.gz
data = '''chr1	249250621
chr2	243199373
chr3	198022430
chr4	191154276
chr5	180915260
chr6	171115067
chr7	159138663
chr8	146364022
chr9	141213431
chr10	135534747
chr11	135006516
chr12	133851895
chr13	115169878
chr14	107349540
chr15	102531392
chr16	90354753
chr17	81195210
chr18	78077248
chr19	59128983
chr20	63025520
chr21	48129895
chr22	51304566
chrX	155270560
chrY	59373566'''

builds = OrderedDict()
count = 0
gap = 1000000
for n, line in enumerate(data.split('\n')):
    line = line.split('\t')
    chromossome = line[0].replace('chr', '')
    builds[chromossome] = {}
    builds[chromossome]['size'] = int(line[1])
    builds[chromossome]['start'] = count
    if count == 0:
        builds[chromossome]['start'] = 25000000
        
    builds[chromossome]['end'] = builds[chromossome]['start'] + builds[chromossome]['size']
    count = builds[chromossome]['end'] + 50000000
    if n == 23:
     count = builds[chromossome]['end'] + 25000000   
        
    
total = count
    
#print builds


#now convert to radian 0 360
#360 ----- 3095677412
#x ------ 287384665

#example
#chr1
#start 0
#end 249250621
##x = 28
#start = 0
#end = 249250621.0*360.0/3095677412.0
#print start, end
#np.radians(end)

def genome_to_radians(chr, pos):
    start = builds[chr]['start']
    glob_pos = start + pos
    glob_pos = glob_pos*360.0/total
    rad = np.radians(glob_pos)
#    print rad
    return rad
#
#genome_to_radians('1', 0)
#genome_to_radians('1', 249250621)
#genome_to_radians('2', 0)
#genome_to_radians('2', 243199373)
#genome_to_radians('Y', 0)
#0.50589503725480156
#die()

#Create figure and polar axis
fig = plt.figure()
ax = fig.add_subplot(111, polar = False)
# ax.set_theta_zero_location('N')
# ax.set_theta_direction(-1)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
plt.ylim( 0, 10.0) 

for chr in builds:
#    print builds[chr]
    rad_start = genome_to_radians(chr, 0)
    rad_end = genome_to_radians(chr, builds[chr]['size'])
#    print  chr,  rad_start,  rad_end
    theta = np.linspace(rad_start,rad_end,21)    
    ax.plot(theta,[10.00 for t in theta],color='blue',linewidth=5)   #Colors are set by hex codes
    label_position = (rad_start+rad_end)/2.0
    
#    print label_position
    label_height = 11
    if len(chr) > 1:
        label_height = 11.5
        #label_position - 1.5
    ax.text(label_position,label_height,chr)
    
from collections import Counter
#now add genome bands
band_colors = {'gneg': '#ffffff', 'gpos50': '#b3b3b3', 'gpos75': '#666666', 'gpos25': '#e5e5e5', 'gpos100': '#000000', 'acen': '#8b2323', 'gvar': '#ffffff', 'stalk': '#cd3333'}
bands = []
cytobandfile = open('cytoBand.txt', 'r')
header = cytobandfile.next()
for line in cytobandfile:
    band = line.strip().split('\t')
#    print band
    chr = band[0].replace('chr', '')
    start = int(band[1])
    end = int(band[2])
    bname = band[4]
    rad_start = genome_to_radians(chr, start)
    rad_end = genome_to_radians(chr, end)
    theta = np.linspace(rad_start,rad_end,21)    
    ax.plot(theta,[9.50 for t in theta],color=band_colors[bname],linewidth=10)   #Colors are set by hex codes
    

#now plot variants
#vcffile = open('vcfs/Exome_3_EDS.var.annotated.vcf', 'r')
#variants_rad_list = []
#for line in vcffile.readlines():
#    if not line.startswith('#'):
#        variant = line.strip().split('\t')
#        chr = variant[0].replace('chr', '')
#        pos = int(variant[1])
#        genotype = variant[-1].split(':')[0]
##        print genotype 
#        if genotype == '1/1':
#            rad_pos = genome_to_radians(chr, pos)
#            variants_rad_list.append(rad_pos)            
#            #plt.vlines(rad_pos, 7.0, 8.0, linewidth=0.01, color='blue',antialiased=True)
#            #plot homozygous variant
#print 'plot variants'
#plt.vlines(variants_rad_list, 7.0, 8.0, linewidth=0.01, color='blue',antialiased=True)

#given a vcf file return list of homozygous variants in radians
def vcf_rad_list(vcffile):
    vcffile = open(vcffile, 'r')
    variants_rad_list = []
    for line in vcffile.readlines():
        if not line.startswith('#'):
            variant = line.strip().split('\t')
            chr = variant[0].replace('chr', '')
            pos = int(variant[1])
            genotype = variant[-1].split(':')[0]
            if genotype == '1/1':
                if variant[2] == '.':
                    if variant[6] == 'PASS':
                        rad_pos = genome_to_radians(chr, pos)
                        variants_rad_list.append(rad_pos)
                        


    return variants_rad_list
    
def plot_vcf(vcffile, pos):
    ymin = pos
    ymax = pos + 0.8
    variants_rad_list = vcf_rad_list(vcffile)
    print 'plot vcf'
    plt.vlines(variants_rad_list, ymin, ymax, linewidth=0.1, color='blue',antialiased=True)

    
# plot_vcf('/home/raony/Doutorado/phd-thesis/data/family/exome_3_eds.var.annotated.vcf', 8)
# plot_vcf('/home/raony/Doutorado/phd-thesis/data/family/exome_4_els.var.annotated.vcf', 7)
# plot_vcf('/home/raony/Doutorado/phd-thesis/data/family/exome_5_ls.var.annotated.vcf', 6)
# plot_vcf('/home/raony/Doutorado/phd-thesis/data/family/exome_6_dc.var.annotated.vcf', 5)

#remove variants from father and mother, 
def remove_from_parents():
    children_variants = []
#    for 

children = ['/home/raony/Doutorado/phd-thesis/data/family/Exome_3_EDS.var.annotated.vcf', '/home/raony/Doutorado/phd-thesis/data/family/Exome_4_ELS.var.annotated.vcf']
parents = ['/home/raony/Doutorado/phd-thesis/data/family/Exome_5_LS.var.annotated.vcf', '/home/raony/Doutorado/phd-thesis/data/family/Exome_6_DC.var.annotated.vcf']
    
#remove_from_parents()
    
#Exome_4_ELS.var.annotated.vcf.gz
#Exome_5_LS.var.annotated.vcf.gz
#plt.vlines(variants_rad_list, 7.0, 8.0, linewidth=0.01, color='blue',antialiased=True)
#Exome_6_DC.var.annotated.vcf.gz
#plt.vlines(variants_rad_list, 7.0, 8.0, linewidth=0.01, color='blue',antialiased=True)

#theta = np.array([0.50])



# print builds.values()
#total = np.sum(builds.values())
#print total

#def coordinate_to_abs(chr, pos):
    
    
#coordinate_to_abs(1, 197263)
    
#dividing by angles
#angle = 360.0/total
#print angle
#
#cytoband_file = open('cytoBand.txt', 'r')
#cytobands = OrderedDict()
#for line in cytoband_file:
#    row = line.strip().split('\t')
#    chr = row[0].replace('chr', '')
#    if chr not in cytobands:
#        cytobands[chr] = []
#    cytoband = OrderedDict()
#    cytoband['start'] = row[1]
#    cytoband['end'] = row[2]
#    cytoband['label'] = row[3]
#    cytoband['color'] = row[4]
#    cytobands[chr].append(cytoband)
#print cytobands
#for cyto in cytobands:
#    print cytobands[cyto]
#    die()
#print cytobands['2']
#die()
#def genome_to_absolute(chr, pos):
    
#genome_to_absolute(1, 2300000)
#N = 24
#theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
#new_theta = []
#new_width = []
#for chr in builds:
#    new_theta.append(builds[chr]['start'])
#    new_width.append(builds[chr]['size'])
#theta = np.array(new_theta)
#radii = 1 *  np.ones(24)  #np.random.rand(N)
#width = np.pi / 4 * np.random.rand(N)
#width = np.array(new_width)
#
#ax = plt.subplot(111, polar=False)
#
#bars = ax.bar(theta, radii, width=width, bottom=0.0) #BOTTON DEFINES TRACK


#plot cytobands


"""
Demo of bar plot on a polar axis.
"""
#
#plt.clf()
#N = 24
#theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
#new_theta = []
#new_width = []
#for chr in builds:
#    new_theta.append(builds[chr]['start'])
#    new_width.append(builds[chr]['size'])
#theta = np.array(new_theta)
#radii = 10 *  np.ones(24)  #np.random.rand(N)
#width = np.pi / 4 * np.random.rand(N)
#width = np.array(new_width)
#
#ax = plt.subplot(111, polar=True)
#ax.set_theta_zero_location('N')
#ax.set_theta_direction(-1)
#
##ax.plot(theta,[0.7 for t in theta],color='blue',linewidth=10)
#bars = ax.bar(theta, radii, width=width, bottom=0.0) #BOTTON DEFINES TRACK
#bars = ax.bar(theta, radii, width=width, bottom=1.0) #BOTTON DEFINES TRACK

# Use custom colors and opacity
#for r, bar in zip(radii, bars):
#    bar.set_facecolor(plt.cm.jet(r / 10.))
#    bar.set_alpha(0.5)

plt.show()