from common.api.serializers import DynamicFieldsModelSerializer

from about.models import AboutStatisticSection


class AboutStatisticSectionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = AboutStatisticSection
        fields = [
            'id',
            'title',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
