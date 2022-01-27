from rest_framework import serializers

from .models import House, Notary, Flat, Announcement, UserFilter

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

    def create(self, validated_data):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
            if user.role.id == 2:
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
    class Meta:
        model = Flat
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
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


class UserFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFilter
        fields = '__all__'

    def create(self, validated_data):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
            validated_data['user'] = user
        return UserFilter.objects.create(**validated_data)