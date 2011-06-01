from django.db import models
from uuid import uuid4
from django.contrib.gis.gdal import *
from django.contrib.gis.db import models as geomodels

# Create your models here.

class ShapeFile(models.Model):
	name = models.TextField()
	srs = models.TextField()

class Instance(models.Model):
	name = models.CharField(primary_key=True, max_length=64, editable=False, blank=True, default=uuid4)
	fid = models.IntegerField()
	shapefile = models.ForeignKey(ShapeFile)
	position = geomodels.GeometryField()
	objects = models.GeoManager()
	
	def save(self, *args, **kwargs):
		if SpatialReference(self.shapefile.srs) != SpatialReference(4326):
			ct = CoordTransform(SpatialReference(self.shapefile.srs), SpatialReference('WGS84'))
			self.position.transform(ct)

class Column(models.Model):
	name = models.CharField(max_length=256)
	value = models.TextField()
	type = models.TextField()
