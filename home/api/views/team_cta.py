from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from home.models import TeamCTA
from home.api.serializers import TeamCTASerializer


class TeamCTAViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamCTA.objects.filter(is_active=True, is_deleted=False)
    serializer_class = TeamCTASerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')
