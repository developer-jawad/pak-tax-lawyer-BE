from blog.models import BlogSection
from common.api.serializers import DynamicFieldsModelSerializer


class BlogSectionSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = BlogSection
        fields = [
            "id",
            "subtitle",
            "title",
            "description",
            "categories",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
