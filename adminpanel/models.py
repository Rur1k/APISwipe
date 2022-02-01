from django.db import models

from account.models import User


class House(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=64, unique=True, blank=True)
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
    builder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Flat(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    number = models.IntegerField(null=True, blank=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
    count_room = models.IntegerField(null=True, blank=True)
    square = models.FloatField(null=True, blank=True)
    price_per_meter = models.FloatField(null=True, blank=True)
    house_building = models.IntegerField(null=True, blank=True)
    section = models.IntegerField(null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    riser = models.IntegerField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    reserved = models.BooleanField(default=False, blank=True)


class Notary(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)


class Announcement(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
    founding_documents = models.CharField(max_length=64, null=True, blank=True)
    purpose = models.CharField(max_length=64, null=True, blank=True)
    count_rooms = models.CharField(max_length=64, null=True, blank=True)
    layout = models.CharField(max_length=64, null=True, blank=True)
    residential_condition = models.CharField(max_length=64, null=True, blank=True)
    all_square = models.FloatField(default=0, null=True, blank=True)
    balcony = models.BooleanField(default=False, null=True, blank=True)
    heating_type = models.CharField(max_length=64, null=True, blank=True)
    commission_to_agent = models.FloatField(default=0, null=True, blank=True)
    connection_type = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    calculation_option = models.CharField(max_length=64, null=True, blank=True)
    maps = models.TextField(null=True, blank=True)
    pub_status = models.BooleanField(default=False, null=True, blank=True)


class UserFilter(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name_filter = models.CharField(max_length=64, null=True, blank=True)
    state_house = models.CharField(max_length=64, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    district = models.CharField(max_length=64, null=True, blank=True)
    microdistrict = models.CharField(max_length=64, null=True, blank=True)
    count_rooms = models.CharField(max_length=64, null=True, blank=True)
    price_first = models.FloatField(null=True, blank=True)
    price_last = models.FloatField(null=True, blank=True)
    square_first = models.FloatField(null=True, blank=True)
    square_last = models.FloatField(null=True, blank=True)
    purpose = models.CharField(max_length=64, null=True, blank=True)
    calculation_option = models.CharField(max_length=64, null=True, blank=True)
    residential_condition = models.CharField(max_length=64, null=True, blank=True)


class Favorite(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, null=True, blank=True)
