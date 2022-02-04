from django_filters import rest_framework as filters

from .models import Announcement


class AnnouncementFilter(filters.FilterSet):
    price = filters.RangeFilter()
    all_square = filters.RangeFilter()

    class Meta:
        model = Announcement
        fields = [
            'house__type_house',
            'house__district',
            'house__microdistrict',
            'house__state',
            'count_rooms',
            'price',
            'all_square',
            'purpose',
            'calculation_option',
            'residential_condition',
        ]
