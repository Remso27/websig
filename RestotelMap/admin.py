from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from RestotelMap.models import *

# Register your models here.
class CategorieAdmin(LeafletGeoAdmin):
    list_display= ['libelle']
    ordering= ['libelle']
    search_fields= ['libelle']

class LocalisationAdmin(LeafletGeoAdmin):
    list_display= ['ville', 'commune', 'quartier']
    ordering= ['ville']
    search_fields= ['ville']

class EtablissementAdmin(LeafletGeoAdmin):
    list_display= ['nom', 'catego', 'telephone', 'local', 'latitude', 'longitude', 'geom']
    ordering= ['nom']
    search_fields= ['nom']


admin.site.register(Catego, CategorieAdmin)
admin.site.register(Local, LocalisationAdmin)
admin.site.register(Etab, EtablissementAdmin)