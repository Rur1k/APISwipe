# Generated by Django 2.2.26 on 2022-01-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0007_userfilter'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfilter',
            name='state_house',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='userfilter',
            name='count_rooms',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
