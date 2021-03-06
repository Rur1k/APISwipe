# Generated by Django 2.2.26 on 2022-01-21 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('district', models.CharField(blank=True, max_length=64, null=True)),
                ('microdistrict', models.CharField(blank=True, max_length=64, null=True)),
                ('street', models.CharField(blank=True, max_length=64, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('lcd_status', models.CharField(blank=True, max_length=64, null=True)),
                ('type', models.CharField(blank=True, max_length=64, null=True)),
                ('class_house', models.CharField(blank=True, max_length=64, null=True)),
                ('technologies', models.CharField(blank=True, max_length=64, null=True)),
                ('to_sea', models.CharField(blank=True, max_length=64, null=True)),
                ('payments', models.CharField(blank=True, max_length=64, null=True)),
                ('ceiling_height', models.CharField(blank=True, max_length=64, null=True)),
                ('gas', models.CharField(blank=True, max_length=64, null=True)),
                ('heating', models.CharField(blank=True, max_length=64, null=True)),
                ('sewerage', models.CharField(blank=True, max_length=64, null=True)),
                ('sales_dep_fullname', models.CharField(blank=True, max_length=128, null=True)),
                ('sales_dep_phone', models.CharField(blank=True, max_length=16, null=True)),
                ('sales_dep_email', models.CharField(blank=True, max_length=64, null=True)),
                ('registration', models.TextField(blank=True, null=True)),
                ('calculation_options', models.TextField(blank=True, null=True)),
                ('appointment', models.TextField(blank=True, max_length=64, null=True)),
                ('sum_in_contract', models.TextField(blank=True, max_length=64, null=True)),
                ('state', models.CharField(blank=True, max_length=64, null=True)),
                ('territory', models.CharField(blank=True, max_length=64, null=True)),
                ('maps', models.TextField(blank=True, null=True)),
                ('house_buildings', models.IntegerField(blank=True, null=True)),
                ('sections', models.IntegerField(blank=True, null=True)),
                ('floors', models.IntegerField(blank=True, null=True)),
                ('risers', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FLat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('count_room', models.IntegerField(blank=True, null=True)),
                ('square', models.FloatField(blank=True, null=True)),
                ('price_per_meter', models.FloatField(blank=True, null=True)),
                ('house_building', models.IntegerField(blank=True, null=True)),
                ('section', models.IntegerField(blank=True, null=True)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('riser', models.IntegerField(blank=True, null=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.House')),
            ],
        ),
    ]
