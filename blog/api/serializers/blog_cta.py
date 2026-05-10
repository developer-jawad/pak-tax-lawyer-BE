from common.api.serializers import DynamicFieldsModelSerializer

from blog.models import BlogCTA


class BlogCTASerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = BlogCTA
        fields = [
            'id',
            'button_text',
            'button_link',
            'is_blog_section',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
