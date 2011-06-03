from geoserver.models import *
from django.shortcuts import render_to_response 
from django.http import *
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