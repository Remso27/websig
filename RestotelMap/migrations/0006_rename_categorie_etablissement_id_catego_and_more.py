# Generated by Django 4.1.7 on 2023-11-11 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestotelMap', '0005_alter_localisation_commune_alter_localisation_ville'),
    ]

    operations = [
        migrations.RenameField(
            model_name='etablissement',
            old_name='categorie',
            new_name='id_catego',
        ),
        migrations.RenameField(
            model_name='etablissement',
            old_name='situa_geo',
            new_name='id_local',
        ),
    ]
