import geopandas as gpd
from .models import *
from django.contrib.gis.geos import MultiPoint, Point

def load_data(shapefile_path):
    # Charger les données depuis le fichier Shapefile
    gdf = gpd.read_file(shapefile_path)

    # Parcourir les lignes du GeoDataFrame et enregistrer les objets dans la base de données
    for index, row in gdf.iterrows():
        # Récupérer l'objet Catego associé
        catego_instance = Catego.objects.get(id=row['catego_id'])
        
        # Récupérer l'objet Local associé
        local_instance = Local.objects.get(id=row['local_id'])
        
        # Créer un point à partir des coordonnées
        point = Point(row['longitude'], row['latitude'])

        etab = Etab(
            nom=row['nom'],
            catego=catego_instance,
            telephone=row['telephone'],
            local=local_instance,
            latitude=row['latitude'],
            longitude=row['longitude'],
            geom=MultiPoint(point)
        )
        etab.save()
