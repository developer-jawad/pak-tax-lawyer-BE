from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from home.api.serializers import TeamMemberSerializer
from home.models import TeamMember


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamMember.objects.filter(is_active=True, is_deleted=False)
    serializer_class = TeamMemberSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-featured", "name")
