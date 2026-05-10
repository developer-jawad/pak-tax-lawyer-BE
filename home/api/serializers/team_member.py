from rest_framework import serializers
from common.api.serializers import DynamicFieldsModelSerializer

from home.models import TeamMember


class TeamMemberSerializer(DynamicFieldsModelSerializer):
    avatar = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = TeamMember
        fields = [
            'id',
            'name',
            'position',
            'specialization',
            'avatar',
            'bio',
            'credentials',
            'email',
            'phone',
            'linkedin',
            'featured',
            'featured_label',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
