from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from about.api.serializers import WhoWeAreSerializer
from about.models import WhoWeAre


class WhoWeAreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WhoWeAre.objects.all()
    serializer_class = WhoWeAreSerializer
    permission_classes = [AllowAny]
