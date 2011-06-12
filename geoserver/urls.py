from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

	url(r'^map$', 'geoserver.views.map', name='map'),
	url(r'^layers$', 'geoserver.views.shapes', name='shapes'),
	url(r'^layers/add$', 'geoserver.views.add_layer', name='add_layer'),
	url(r'^layer/(?P<shape>[\w-]*)$', 'geoserver.views.get', name='get'),
	url(r'^layer/(?P<shape>[\w-]*).shp$', 'geoserver.views.get', {'format':'shp'},name='get_shp'),
	url(r'^layer/(?P<shape>[\w-]*).json$', 'geoserver.views.get', {'format':'json'},name='get_json'),
	url(r'^layer/(?P<shape>[\w-]*).gml$', 'geoserver.views.get', {'format':'gml'},name='get_gml'),
	url(r'^layer/(?P<shape>[\w-]*).kml$', 'geoserver.views.get', {'format':'kml'},name='get_kml'),
	url(r'^layer/(?P<shape>[\w-]*).kmz$', 'geoserver.views.get', {'format':'kmz'},name='get_kmz'),
	url(r'^layer/(?P<shape>[\w-]*).mif$', 'geoserver.views.get', {'format':'mif'},name='get_mif'),
	
	
)
