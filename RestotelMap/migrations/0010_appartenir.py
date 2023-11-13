# Generated by Django 4.1.7 on 2023-11-11 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestotelMap', '0009_delete_appartenir'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appartenir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestotelMap.catego', verbose_name='Catégorie')),
                ('etab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestotelMap.etab', verbose_name='Etablissement')),
            ],
            options={
                'verbose_name_plural': 'Service',
            },
        ),
    ]