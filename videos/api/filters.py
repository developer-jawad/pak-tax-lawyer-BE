from django_filters import rest_framework as filters
from videos.models import Video


class VideoFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name='category', help_text="Filter by category ID")

    class Meta:
        model = Video
        fields = ['category']
