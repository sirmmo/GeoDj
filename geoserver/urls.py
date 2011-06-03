from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'(?P<shape>[\w-]*)$', 'geoserver.views.get', name='get'),
	url(r'(?P<shape>[\w-]*).shp$', 'geoserver.views.get', {'format':'shp'},name='get_shp'),
	url(r'(?P<shape>[\w-]*).gml$', 'geoserver.views.get', {'format':'gml'},name='get_gml'),
	url(r'(?P<shape>[\w-]*).kml$', 'geoserver.views.get', {'format':'kml'},name='get_kml'),
	url(r'(?P<shape>[\w-]*).kmz$', 'geoserver.views.get', {'format':'kmz'},name='get_kmz'),
	url(r'(?P<shape>[\w-]*).mif$', 'geoserver.views.get', {'format':'mif'},name='get_mif'),
)
