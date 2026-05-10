from common.api.serializers import DynamicFieldsModelSerializer

from home.models import TeamSection


class TeamSectionSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TeamSection
        fields = [
            'id',
            'subtitle',
            'title',
            'description',
            'credentials_label',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
