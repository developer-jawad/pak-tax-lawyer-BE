from common.api.serializers import DynamicFieldsModelSerializer

from service.models import Service, ServiceSection
from service.models.service_cta import ServiceCTA


class ServiceForSectionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'icon', 'title', 'description', 'features', 'popular']


class ServiceCTAForSectionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ServiceCTA
        fields = ['title', 'description', 'button_text']


class ServiceSectionSerializer(DynamicFieldsModelSerializer):
    services = ServiceForSectionSerializer(many=True, read_only=True)
    cta = ServiceCTAForSectionSerializer(read_only=True)

    class Meta:
        model = ServiceSection
        fields = [
            'subtitle',
            'title',
            'description',
            'services',
            'cta',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Get all services
        services = Service.objects.all().order_by('id')
        data['services'] = ServiceForSectionSerializer(services, many=True).data
        
        # Construct CTA from ServiceSection fields
        data['cta'] = {
            'title': instance.cta_title,
            'description': instance.cta_description,
            'primaryButton': instance.primary_button,
            'secondaryButton': instance.secondary_button,
        }
        
        return data
