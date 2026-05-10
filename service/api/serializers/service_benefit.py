from common.api.serializers import DynamicFieldsModelSerializer

from service.models import ServiceBenefit


class ServiceBenefitSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ServiceBenefit
        fields = [
            'id',
            'icon',
            'text',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
