# Generated by Django 2.2.26 on 2022-01-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0009_auto_20220127_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='floor',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='flat',
            name='house_building',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='flat',
            name='riser',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='flat',
            name='section',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='house',
            name='floors',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='house',
            name='house_buildings',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='house',
            name='risers',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='house',
            name='sections',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
