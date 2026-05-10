from common.api.serializers import DynamicFieldsModelSerializer

from about.models import AboutHero


class AboutHeroSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = AboutHero
        fields = [
            'id',
            'title',
            'subtitle',
            'description',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
