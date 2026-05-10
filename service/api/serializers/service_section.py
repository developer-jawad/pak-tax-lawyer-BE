from common.api.serializers import DynamicFieldsModelSerializer

from service.models import ServiceSection


class ServiceSectionSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ServiceSection
        fields = [
            'id',
            'subtitle',
            'title',
            'description',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
