from common.api.serializers import DynamicFieldsModelSerializer
from home.models import TeamCTA


class TeamCTASerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TeamCTA
        fields = [
            "id",
            "title",
            "description",
            "email",
            "is_team_section",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
