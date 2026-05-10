from common.api.serializers import DynamicFieldsModelSerializer

from blog.models import BlogStatistic


class BlogStatisticSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = BlogStatistic
        fields = [
            'id',
            'number',
            'label',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
