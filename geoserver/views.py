from geoserver.models import *
from django.shortcuts import render_to_response 
from django.http import *
from django.core.urlresolvers import reverse

try:
	import json
exept:
	import simplejson as json

def get(request, shape, format="base"):
	
	if ShapeFile.objects.filter(slug = shape).count() < 1:
		return render_to_response ("error.html")
	s = ShapeFile.objects.get(slug = shape)
	layer = {
		'layer_name':s.name,
		'srs':s.srs,
		'fields':[a.name for a in Column.objects.filter(instance__shapefile = s).distinct()]
		'feats':[],
		'feats_dict':{}
	}
	for instance in s.instances:
		feat = {}
		feat['fid'] = instance.fid
		feat['position'] = instance.position
		feat['feats'] = []
		for feature in instance.columns:
			col = {}
			col['name'] = feature.name
			col['value'] = feature.value
			col['type'] = feature.type
			feat['feats'].append(col)
			feats_dict[feature.name] = feature.value
		layer['feats'].append(feat)

	if format == "base":
		return render_json(layer)
	elif format == "shp":
		return render_shp(layer)

def render_json(layer):
	data = {
		'type':'FeatureCollection',
		'features':[{
			"type": "Feature",
			'geometry' : json.loads(feat['position'].json),
			'properties':feat['feats_dict']
		} for feat in layer['feats']]
	}

	reurn HttpResponse(json.dumps(data), mimetype = "text/json")

def shapes(request):
	shps = [{
		"name" : shape.name,
		"json" : reverse('get_json', kwargs={"schema" : shape.slug}),
		"kml" : reverse('get_kml', kwargs={"schema" : shape.slug}),
		"kmz" : reverse('get_kmz', kwargs={"schema" : shape.slug}),
		"shp" : reverse('get_shp', kwargs={"schema" : shape.slug}),
		"mif" : reverse('get_mif', kwargs={"schema" : shape.slug}),
		"gml" : reverse('get_gml', kwargs={"schema" : shape.slug}),
	} for shape in ShapeFile.objects.all()]
	return HttpResponse(json.dumps(shps), mimetype = "test/json")	

def map(request):
	return render_to_response('map.html')