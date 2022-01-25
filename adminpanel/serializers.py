from rest_framework import serializers

from .models import House, Notary, Flat

from account.models import User



class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = [
            'id',
            'name',
            'district',
            'microdistrict',
            'street',
            'number',
            'description',
            'lcd_status',
            'type_house',
            'class_house',
            'technologies',
            'to_sea',
            'payments',
            'ceiling_height',
            'gas',
            'heating',
            'sewerage',
            'sales_dep_fullname',
            'sales_dep_phone',
            'sales_dep_email',
            'registration',
            'calculation_options',
            'appointment',
            'sum_in_contract',
            'state',
            'territory',
            'maps',
            'house_buildings',
            'sections',
            'floors',
            'risers',
        ]


class HouseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = [
            'name',
            'district',
            'microdistrict',
            'street',
            'number',
            'description',
            'lcd_status',
            'type_house',
            'class_house',
            'technologies',
            'to_sea',
            'payments',
            'ceiling_height',
            'gas',
            'heating',
            'sewerage',
            'sales_dep_fullname',
            'sales_dep_phone',
            'sales_dep_email',
            'registration',
            'calculation_options',
            'appointment',
            'sum_in_contract',
            'state',
            'territory',
            'maps',
            'house_buildings',
            'sections',
            'floors',
            'risers',
        ]

    def create(self, validated_data):
        return House.objects.create(**validated_data)


class NotaryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notary
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
        ]

    def create(self, validated_data):
        return Notary.objects.create(**validated_data)


class NotarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Notary
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
        ]


class FlatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = [
            'number',
            'house',
            'count_room',
            'square',
            'price_per_meter',
            'house_building',
            'section',
            'floor',
            'riser',
        ]

    def create(self, validated_data):
        errors = []
        if validated_data['house_building'] > validated_data['house'].house_buildings:
            errors.append('В выбраном доме нет указанного корпуса')
        if validated_data['section'] > validated_data['house'].sections:
            errors.append('В выбраном доме нет указанной секции')
        if validated_data['floor'] > validated_data['house'].floors:
            errors.append('В выбраном доме нет указанного этажа')
        if validated_data['riser'] > validated_data['house'].risers:
            errors.append('В выбраном доме нет указанного стояка')

        if errors:
            raise serializers.ValidationError(errors)

        return Flat.objects.create(**validated_data)


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = [
            'number',
            'house',
            'count_room',
            'square',
            'price_per_meter',
            'house_building',
            'section',
            'floor',
            'riser',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'first_name',
            'last_name',
            'email',
            'phone',
            'role',
            'is_blacklist',
        ]
