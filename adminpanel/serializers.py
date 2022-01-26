from rest_framework import serializers

from .models import House, Notary, Flat, Announcement

from account.models import User


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


class HouseSerializer(serializers.ModelSerializer):
    builder = serializers.StringRelatedField()

    class Meta:
        model = House
        fields = '__all__'


class HouseCreateSerializer(serializers.ModelSerializer):
    builder = serializers.StringRelatedField()

    class Meta:
        model = House
        fields = '__all__'

    def create(self, validated_data):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
            if user.role.id == 2:
                validated_data['builder'] = user
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


class AnnouncementCreateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    house = serializers.StringRelatedField()

    class Meta:
        model = Announcement
        fields = '__all__'

    def create(self, validated_data):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
            validated_data['user'] = user
        return Announcement.objects.create(**validated_data)


class AnnouncementSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    house = serializers.StringRelatedField()

    class Meta:
        model = Announcement
        fields = '__all__'
