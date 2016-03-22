#Desenhando a estrutura de um Gene

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches


#get intron and exons
import os
from cogent.db.ensembl import HostAccount, Genome

fig = plt.figure(figsize=(18,9),dpi=720)
ax = fig.add_subplot(111)
ax.set_ylabel('Tracks')
ax.set_xlabel('Position')
ax.set_ylim(0,5)

account = None

human = Genome('human', Release=80, account=account)

#gene_symbols = ['sucla2']#'brca1', 'brca2', 

#for gene_symbol in gene_symbols:
#print gene_symbol
gene_symbol = 'sucla2'

#genes = human.getGenesMatching(Symbol=gene_symbol)

#for gene in genes:
gene = human.getGeneByStableId(StableId='ENSG00000136143')

print dir(gene)
print gene.StableId

ax.set_xlim(gene.Location.Start,gene.Location.End)
positions = range(gene.Location.Start,gene.Location.End)
plt.plot(positions, [1 for x in positions], 'k-')

print gene.Location.CoordName
print gene.Location.Start, gene.Location.End

size = gene.Location.End - gene.Location.Start
print 'Size', size
print gene.Location.Strand

exons = gene.CanonicalTranscript.Exons
#print dir(gene.CanonicalTranscript)



#print gene.CanonicalTranscript.Cds
# gene.CanonicalTranscript.UntranslatedExons5
# gene.CanonicalTranscript.UntranslatedExons3

#print gene.CanonicalTranscript.Utr5

patches_list = []
for exon in exons:
    print exon, exon.Location
    #exon = range(exon.Location.Start,exon.Location.End)
    width = exon.Location.End-exon.Location.Start
    print 'width', width
    patches_list.append(
        patches.Rectangle(
            (exon.Location.Start, 1),   # (x,y)
            width,          # width
            2,          # height
        )
    )



for patch in patches_list:
    ax.add_patch(patch)
        
plt.show()
        
