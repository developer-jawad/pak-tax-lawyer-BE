from blog.models import BlogHero
from common.api.serializers import DynamicFieldsModelSerializer


class BlogHeroSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = BlogHero
        fields = [
            "id",
            "title",
            "subtitle",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
