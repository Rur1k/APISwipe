# Generated by Django 2.2.26 on 2022-01-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0005_auto_20220126_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(blank=True, max_length=64, unique=True),
        ),
    ]
