from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from datetime import datetime

class UserGroup(models.Model):
    name = models.CharField(max_length=600)
    members = models.ManyToManyField(User, editable=True, related_name="members", blank=True, null=True)
    def __unicode__(self):
        return self.name

class Individual(models.Model):
    def get_upload_path(self, filename):
        string = "%s/genomes/%s/%s/%s" % (settings.BASE_DIR, slugify(self.user.username), self.id, filename)#.replace(' ', '_')
        return string 
    user = models.ForeignKey(User, editable=False)

    shared_with_users = models.ManyToManyField(User, editable=True, related_name="shared_with_users", blank=True, null=True)
    shared_with_groups = models.ManyToManyField(UserGroup, editable=True, related_name="shared_with_groups", blank=True, null=True)

    name = models.CharField(max_length=600)
    is_featured = models.BooleanField(default=True)
    is_public = models.BooleanField(default=False)
    vcf_file = models.FileField(upload_to=get_upload_path, blank=True, help_text="File Format: VCF",max_length=600)
    vcf_header = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, blank=True, editable=False)
    n_variants = models.IntegerField(null=True, blank=True, editable=False)
    n_lines = models.IntegerField(null=True, blank=True, editable=False)

    creation_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    modified_date = models.DateTimeField(null=True, blank=True)

    annotation_time = models.CharField(max_length=200, null=True, blank=True)
    insertion_time = models.CharField(max_length=200, null=True, blank=True)
    insertion_time_mongo = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
	return self.name
    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(Individual, self).save(*args, **kwargs)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Individual)
    
    def __unicode__(self):
        return self.name

class ControlGroup(models.Model):
    name = models.CharField(max_length=600)
    vcf_file = models.FileField(upload_to=get_upload_path, blank=True, help_text="File Format: VCF",max_length=600)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(ControlGroup, self).save(*args, **kwargs)
        PopulateControls.delay(self.id)

    def get_upload_path(self, filename):
        string = "upload/controls/%s/%s" % (self.id, filename)#.replace(' ', '_')
        return string

class ControlVariant(models.Model):
    controlgroup = models.ForeignKey(ControlGroup)
    index = models.TextField(db_index=True)#ex. 1-2387623-G-T