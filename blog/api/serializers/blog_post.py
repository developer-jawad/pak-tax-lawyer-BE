from rest_framework import serializers

from blog.models import BlogPost
from common.api.serializers import DynamicFieldsModelSerializer


class BlogPostSerializer(DynamicFieldsModelSerializer):
    category_display = serializers.CharField(
        source="get_category_display", read_only=True
    )

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "excerpt",
            "author",
            "date",
            "read_time",
            "category",
            "category_display",
            "image_url",
            "image",
            "slug",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
