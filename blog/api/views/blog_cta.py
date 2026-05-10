from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from blog.models import BlogCTA
from blog.api.serializers import BlogCTASerializer


class BlogCTAViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogCTA.objects.filter(is_active=True, is_deleted=False)
    serializer_class = BlogCTASerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')
