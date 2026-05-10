from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from home.models import (
    TeamMember,
    TeamCTA,
    TeamSection,
)
from home.api.serializers import (
    TeamSectionSerializer,
    TeamMemberSerializer,
    TeamCTASerializer,
)


class TeamSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamSection.objects.all()
    serializer_class = TeamSectionSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        team_section = TeamSection.active_objects.first()
        team_members = TeamMember.active_objects.all()
        cta = TeamCTA.active_objects.filter(is_team_section=True).first()

        return Response({
            'team_section': TeamSectionSerializer(team_section).data if team_section else None,
            'team_members': TeamMemberSerializer(team_members, many=True).data,
            'cta': TeamCTASerializer(cta).data if cta else None,
        })
