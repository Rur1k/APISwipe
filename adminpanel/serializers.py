from rest_framework import serializers

from .models import House


class HouseSerializer(serializers.ModelSerializer):
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