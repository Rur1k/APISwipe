from django.db import models


class House(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    district = models.CharField(max_length=64, null=True, blank=True)
    microdistrict = models.CharField(max_length=64, null=True, blank=True)
    street = models.CharField(max_length=64, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    lcd_status = models.CharField(max_length=64, null=True, blank=True)
    type_house = models.CharField(max_length=64, null=True, blank=True)
    class_house = models.CharField(max_length=64, null=True, blank=True)
    technologies = models.CharField(max_length=64, null=True, blank=True)
    to_sea = models.CharField(max_length=64, null=True, blank=True)
    payments = models.CharField(max_length=64, null=True, blank=True)
    ceiling_height = models.CharField(max_length=64, null=True, blank=True)
    gas = models.CharField(max_length=64, null=True, blank=True)
    heating = models.CharField(max_length=64, null=True, blank=True)
    sewerage = models.CharField(max_length=64, null=True, blank=True)
    sales_dep_fullname = models.CharField(max_length=128, null=True, blank=True)
    sales_dep_phone = models.CharField(max_length=16, null=True, blank=True)
    sales_dep_email = models.CharField(max_length=64, null=True, blank=True)
    registration = models.TextField(null=True, blank=True)
    calculation_options = models.TextField(null=True, blank=True)
    appointment = models.TextField(max_length=64, null=True, blank=True)
    sum_in_contract = models.TextField(max_length=64, null=True, blank=True)
    state = models.CharField(max_length=64, null=True, blank=True)
    territory = models.CharField(max_length=64, null=True, blank=True)
    maps = models.TextField(null=True, blank=True)
    house_buildings = models.IntegerField(null=True, blank=True)
    sections = models.IntegerField(null=True, blank=True)
    floors = models.IntegerField(null=True, blank=True)
    risers = models.IntegerField(null=True, blank=True)


class Flat(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    number = models.IntegerField(null=True, blank=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    count_room = models.IntegerField(null=True, blank=True)
    square = models.FloatField(null=True, blank=True)
    price_per_meter = models.FloatField(null=True, blank=True)
    house_building = models.IntegerField(null=True, blank=True)
    section = models.IntegerField(null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    riser = models.IntegerField(null=True, blank=True)


class Notary(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)


