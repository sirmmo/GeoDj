from django.db import models
from uuid import uuid4
from django.contrib.gis.gdal import *
from django.contrib.gis.db import models as geomodels
from django.template.defaultfilters import slugify

# Create your models here.

class ShapeFile(models.Model):
	name = models.TextField()
	slug = models.TextField(blank=True, editable= False)
	srs = models.TextField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(ShapeFile, self).save(*args, **kwargs)
	def __unicode__(self):
		return self.name

class Instance(models.Model):
	name = models.CharField(primary_key=True, max_length=64, editable=False, blank=True, default=uuid4)
	fid = models.IntegerField()
	shapefile = models.ForeignKey(ShapeFile, related_name = "instances")
	position = geomodels.GeometryField()
	objects = models.GeoManager()
	
	def save(self, *args, **kwargs):
		if SpatialReference(self.shapefile.srs) != SpatialReference(4326):
			ct = CoordTransform(SpatialReference(self.shapefile.srs), SpatialReference('WGS84'))
			self.position.transform(ct)
		super(Instance, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.shapefile + " - " + str(self.fid)

class Column(models.Model):
	instance = models.ForeignKey(Instance, related_name = "columns")
	name = models.CharField(max_length=256)
	value = models.TextField()
	type = models.TextField()

	def __unicode__(self):
		return str(self.instance) + " - " + self.name + ": " + self.value
