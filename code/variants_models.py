from django.db import models
from individuals.models import *

class Variant(models.Model):
    individual = models.ForeignKey(Individual)
    
    index = models.TextField(db_index=True)#ex. 1-2387623-G-T
    pos_index = models.TextField(db_index=True)#ex. 1-326754756

    #First save all 9 VCF columns
    chr = models.CharField(db_index=True, max_length=100, verbose_name="Chr")
    pos = models.IntegerField(db_index=True)
    variant_id = models.CharField(db_index=True, max_length=100, verbose_name="ID")    
    ref = models.TextField(null=True, blank=True)
    alt = models.TextField(null=True, blank=True)
    qual = models.FloatField(db_index=True)
    filter = models.CharField(db_index=True, max_length=100)
    info = models.TextField(null=True, blank=True)
    format = models.TextField(null=True, blank=True)
    
    genotype_col = models.TextField(null=True, blank=True)
    genotype = models.CharField(db_index=True, max_length=100)

    #metrics from genotype_info DP field
    read_depth = models.IntegerField(db_index=True)

    gene = models.TextField(db_index=True, null=True, blank=True)
    mutation_type = models.CharField(db_index=True, null=True, max_length=100)    
    vartype = models.CharField(db_index=True, null=True, max_length=100)

    #Annotation From 1000genomes 
    genomes1k_maf = models.FloatField(db_index=True, null=True, blank=True, verbose_name="1000 Genomes Frequency")
    dbsnp_maf = models.FloatField(db_index=True, null=True, blank=True, verbose_name="dbSNP Frequency")
    esp_maf = models.FloatField(db_index=True, null=True, blank=True, verbose_name="ESP6500 Frequency")
    
    #dbsnp
    # dbsnp_pm = models.TextField(db_index=True, null=True, blank=True)
    # dbsnp_clnsig = models.TextField(db_index=True, null=True, blank=True)
    dbsnp_build = models.IntegerField(db_index=True,null=True)
    
    #VEP
    sift = models.FloatField(db_index=True, null=True, blank=True)
    sift_pred = models.TextField(db_index=True, null=True, blank=True)

    polyphen2 = models.FloatField(db_index=True, null=True, blank=True)
    polyphen2_pred = models.TextField(db_index=True, null=True, blank=True)

    condel = models.FloatField(db_index=True, null=True, blank=True)
    condel_pred = models.TextField(db_index=True, null=True, blank=True)

    vest = models.FloatField(db_index=True, null=True, blank=True)
    cadd = models.FloatField(db_index=True, null=True, blank=True)

    cadd = models.FloatField(db_index=True, null=True, blank=True)
    rf_score = models.FloatField(db_index=True, null=True, blank=True)
    ada_score = models.FloatField(db_index=True, null=True, blank=True)

    #hi_index
    # hi_index_str = models.TextField(null=True, blank=True)
    # hi_index = models.FloatField(db_index=True, null=True, blank=True)
    # hi_index_perc = models.FloatField(db_index=True, null=True, blank=True)

    #OMIM
    is_at_omim = models.BooleanField(default=False)

    #HGMD
    is_at_hgmd = models.BooleanField(default=False)
    hgmd_entries = models.TextField(null=True, blank=True)

    #snpeff annotation
    snpeff_effect = models.TextField(db_index=True, null=True, blank=True)
    snpeff_impact = models.TextField(db_index=True, null=True, blank=True)
    snpeff_func_class = models.TextField(db_index=True, null=True, blank=True)
    snpeff_codon_change = models.TextField(db_index=True, null=True, blank=True)
    snpeff_aa_change = models.TextField(db_index=True, null=True, blank=True)
    # snpeff_aa_len = models.TextField(db_index=True, null=True, blank=True)
    snpeff_gene_name = models.TextField(db_index=True, null=True, blank=True)
    snpeff_biotype = models.TextField(db_index=True, null=True, blank=True)
    snpeff_gene_coding = models.TextField(db_index=True, null=True, blank=True)
    snpeff_transcript_id = models.TextField(db_index=True, null=True, blank=True)
    snpeff_exon_rank = models.TextField(db_index=True, null=True, blank=True)
    # snpeff_genotype_number = models.TextField(db_index=True, null=True, blank=True)

    #vep annotation
    vep_allele = models.TextField(db_index=True, null=True, blank=True)
    vep_gene = models.TextField(db_index=True, null=True, blank=True)
    vep_feature = models.TextField(db_index=True, null=True, blank=True)
    vep_feature_type = models.TextField(db_index=True, null=True, blank=True)
    vep_consequence = models.TextField(db_index=True, null=True, blank=True)
    vep_cdna_position = models.TextField(db_index=True, null=True, blank=True)
    vep_cds_position = models.TextField(db_index=True, null=True, blank=True)
    vep_protein_position = models.TextField(db_index=True, null=True, blank=True)
    vep_amino_acids = models.TextField(db_index=True, null=True, blank=True)
    vep_codons = models.TextField(db_index=True, null=True, blank=True)
    vep_existing_variation = models.TextField(db_index=True, null=True, blank=True)
    vep_distance = models.TextField(db_index=True, null=True, blank=True)
    vep_strand = models.TextField(db_index=True, null=True, blank=True)
    vep_symbol = models.TextField(db_index=True, null=True, blank=True)
    vep_symbol_source = models.TextField(db_index=True, null=True, blank=True)
    vep_sift = models.TextField(db_index=True, null=True, blank=True)
    vep_polyphen = models.TextField(db_index=True, null=True, blank=True)
    vep_condel = models.TextField(db_index=True, null=True, blank=True)


    def get_fields(self):
    	return [(field.name, field.verbose_name.title().replace('_', ' ')) for field in Variant._meta.fields]
