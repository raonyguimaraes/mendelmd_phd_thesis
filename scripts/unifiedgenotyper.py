#!/usr/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser
import os
from time import time
import datetime
import re
#Example
#python /projects/12exomes/data/unifiergenotyper.py -i /projects/12exomes/data/Exome_3_EDS.realigned-recalibrated.bam /projects/12exomes/data/Exome_4_ELS.realigned-recalibrated.bam /projects/12exomes/data/Exome_5_LS.realigned-recalibrated.bam /projects/12exomes/data/Exome_6_DC.realigned-recalibrated.bam -o quartet_only_SNPs_.vcf -t /lgc/datasets/exome_targets/SureSelect_All_Exon_V2_hg19.20110105.bed


__author__ = "Raony Guimaraes"
__copyright__ = "Copyright 2015, The Exome Pipeline"
__credits__ = ["Raony Guimaraes"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Raony Guimaraes"
__email__ = "raonyguimaraes@gmail.com"
__status__ = "Production"

#run example
#python unifiergenotyper.py -i /projects/12exomes/data/Exome_3_EDS.realigned-recalibrated.bam /projects/12exomes/data/Exome_4_ELS.realigned-recalibrated.bam /projects/12exomes/data/Exome_5_LS.realigned-recalibrated.bam /projects/12exomes/data/Exome_6_DC.realigned-recalibrated.bam

parser = OptionParser()
usage = "usage: %prog [options] -f reads1.fastq -q reads2.fastq"
parser = OptionParser(usage=usage)

parser.add_option("-i", dest="input_file",
                  help="BAM File Sorted in BAM format", metavar="BAM") #, nargs=12
parser.add_option("-t", dest="target_array",
                  help="Target Array", metavar="BEDFILE")
parser.add_option("-o", dest="output",
                  help="Output Filename", metavar="VCFFILE")
                  
(options, args) = parser.parse_args()

input_file=options.input_file

filename = ".".join(input_file.split("/")[-1].split(".")[:-1])

target_array=options.target_array

#reference="/lgc/datasets/gatk_data/b37/human_g1k_v37.fasta"
reference="/lgc/datasets/gatk_data/b37/human_g1k_v37chr.fasta"
#dbsnp="/lgc/datasets/dbsnp/dbsnp-135chr.vcf"

#reference="/lgc/datasets/gatk_data/b37/human_g1k_v37chr.fasta"
#reference="/lgc/datasets/hg19/all/hg19_cancer.fasta"
#reference="/lgc/datasets/gatk_data/hg19/ucsc.hg19.fasta"
#dbsnp="/lgc/datasets/dbsnp/137/00-All.vcf"

dbsnp="/lgc/datasets/dbsnp/141/All.vcf"

gatk_dir="/lgc/programs/GenomeAnalysisTK-3.1-1"

command = """
      java -Xmx40g -Djava.io.tmpdir=/projects/tmp -jar %s/GenomeAnalysisTK.jar -T UnifiedGenotyper \
      -R %s \
      -I %s \
      -l INFO \
      --dbsnp %s \
      -A AlleleBalance \
      -stand_call_conf 50.0 \
      -stand_emit_conf 10.0 \
      -dcov 200 \
      -o %s \
      -log %s-UnifiedGenotyper.log \
      -L %s \
      -nt 16 \
      """ % (gatk_dir, reference, input_file, dbsnp, options.output, options.output, re.escape(target_array))
      

print command
os.system(command)    