from django.contrib.gis.db import models
#from django.db import models


class Catego(models.Model):
    libelle = models.CharField(verbose_name ="Libellé",null = False, unique=True, max_length=100)

    class Meta: 
     verbose_name_plural = "Catégories"
    
    def __str__(self):
        return self.libelle

class Local(models.Model):
    ville = models.CharField(verbose_name ="Ville",null=True,blank=True, max_length=100, unique=True)
    commune = models.CharField(verbose_name ="Commune",null=True,blank=True, max_length=100, unique=True,)
    quartier = models.CharField(verbose_name ="Quartier",null=True,blank=True, max_length=100)

    class Meta: 
     verbose_name_plural = "Localisation"
    
    def __str__(self):
        return self.ville


class Etab(models.Model):
    nom = models.CharField(verbose_name ="Nom", max_length=100, null= False)
    catego = models.ForeignKey(Catego, verbose_name="Catégorie", on_delete=models.CASCADE,  null= False)
    telephone = models.CharField(verbose_name ="Téléphone",null=True,blank=True, max_length=100)
    local = models.ForeignKey(Local, verbose_name="Localisation", null=True,blank=True, on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name ="Latitude", null= False)  
    longitude = models.FloatField(verbose_name ="Longitude", null= False) 
    geom = models.MultiPointField(srid=4326) 

    #def save(self, *args, **kwargs):
    #    # Avant de sauvegarder, mettez à jour la géométrie PointField
    #    self.geom = MultiPoint(self.longitude, self.latitude)
    #    super(Etablissement, self).save(*args, **kwargs)
    
    class Meta: 
     verbose_name_plural = "Etablissement"
    
    def __str__(self):
        return self.nom

class Appartenir(models.Model):
    etab =  models.ForeignKey(Etab, verbose_name= "Etablissement", on_delete=models.CASCADE)
    catego =  models.ForeignKey(Catego, verbose_name= "Catégorie", on_delete=models.CASCADE)
   
    class Meta: 
     verbose_name_plural = "Service"
    
    def __str__(self):
        return self.etab
    
