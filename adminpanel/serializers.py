from rest_framework import serializers

from .models import House, Notary, Flat


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