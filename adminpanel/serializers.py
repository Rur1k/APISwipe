from rest_framework import serializers

from .models import House, Notary, Flat, Announcement, Favorite, GalleryAnnouncement

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()

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

    def create(self, validated_data):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
            if user:
                validated_data['builder'] = user
        return House.objects.create(**validated_data)


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


class FlatSerializer(serializers.ModelSerializer):
    house = serializers.StringRelatedField()
    creator = serializers.StringRelatedField()

    class Meta:
        model = Flat
        fields = '__all__'

    def create(self, validated_data):
        errors = []
        if 'house_building' in validated_data:
            if validated_data['house_building'] > validated_data['house'].house_buildings:
                errors.append('В выбраном доме нет указанного корпуса')
        if 'section' in validated_data:
            if validated_data['section'] > validated_data['house'].sections:
                errors.append('В выбраном доме нет указанной секции')
        if 'floor' in validated_data:
            if validated_data['floor'] > validated_data['house'].floors:
                errors.append('В выбраном доме нет указанного этажа')
        if 'riser' in validated_data:
            if validated_data['riser'] > validated_data['house'].risers:
                errors.append('В выбраном доме нет указанного стояка')

        if errors:
            raise serializers.ValidationError(errors)

        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
            validated_data['creator'] = user

        return Flat.objects.create(**validated_data)


class GalleryAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryAnnouncement
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    house = serializers.StringRelatedField()
    images = GalleryAnnouncementSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = '__all__'


class AnnouncementRestrictedSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    house = serializers.StringRelatedField()
    images = GalleryAnnouncementSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = [
            'user',
            'house',
            'founding_documents',
            'purpose',
            'count_rooms',
            'layout',
            'residential_condition',
            'all_square',
            'balcony',
            'heating_type',
            'commission_to_agent',
            'connection_type',
            'description',
            'price',
            'calculation_option',
            'maps',
            'pub_status',
            'images',
        ]


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

    def create(self, validated_data):
        user = None
        request = self.context.get('request')
        print(request.data)
        if request and hasattr(request, 'user'):
            user = request.user
            validated_data['user'] = user
        return Favorite.objects.create(**validated_data)


