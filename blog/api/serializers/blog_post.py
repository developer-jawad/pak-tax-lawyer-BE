from rest_framework import serializers

from blog.models import BlogPost, ContentBlock, Tag
from common.api.serializers import DynamicFieldsModelSerializer
from common.constants import BLOG_CATEGORIES


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]
        read_only_fields = ["id"]


class ContentBlockSerializer(serializers.ModelSerializer):
    content_type_display = serializers.CharField(
        source="get_content_type_display", read_only=True
    )

    class Meta:
        model = ContentBlock
        fields = ["id", "content_type", "content_type_display", "content", "order"]
        read_only_fields = ["id"]


class BlogPostSerializer(DynamicFieldsModelSerializer):
    category_display = serializers.CharField(
        source="get_category_display", read_only=True
    )
    author = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    content_blocks = ContentBlockSerializer(many=True, read_only=True)
    related_posts = serializers.SerializerMethodField()

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
            "tags",
            "content_blocks",
            "related_posts",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_author(self, obj):
        return {
            "name": obj.author_name,
            "title": obj.author_title,
            "avatar": obj.author_avatar,
            "bio": obj.author_bio,
        }

    def get_related_posts(self, obj):
        related_posts = obj.related_posts.filter(is_active=True, is_deleted=False)
        # Use a simple serializer to avoid recursion
        return [
            {
                "id": post.id,
                "title": post.title,
                "slug": post.slug,
                "excerpt": post.excerpt,
                "image_url": post.image_url,
                "date": post.date,
                "read_time": post.read_time,
            }
            for post in related_posts
        ]
