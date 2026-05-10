from rest_framework import serializers
from common.api.serializers import DynamicFieldsModelSerializer
from common.constants import BLOG_CATEGORIES

from videos.models import Video


class VideoSerializer(DynamicFieldsModelSerializer):
    category_display = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'description',
            'thumbnail',
            'duration',
            'views',
            'category',
            'category_display',
            'video_url',
            'trending',
            'new',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_category_display(self, obj):
        category_map = {
            BLOG_CATEGORIES.all: 'All',
            BLOG_CATEGORIES.tax_filing: 'Tax Filing',
            BLOG_CATEGORIES.business_tax: 'Business Tax',
            BLOG_CATEGORIES.tax_planning: 'Tax Planning',
            BLOG_CATEGORIES.sales_tax: 'Sales Tax',
            BLOG_CATEGORIES.nrp_tax: 'NRP Tax',
            BLOG_CATEGORIES.corporate_tax: 'Corporate Tax',
            BLOG_CATEGORIES.property_tax: 'Property Tax',
        }
        return category_map.get(obj.category, 'All')
