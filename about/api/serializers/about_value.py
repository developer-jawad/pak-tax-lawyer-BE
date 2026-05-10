from common.api.serializers import DynamicFieldsModelSerializer

from about.models import AboutValue


class AboutValueSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = AboutValue
        fields = [
            'id',
            'icon',
            'title',
            'description',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
