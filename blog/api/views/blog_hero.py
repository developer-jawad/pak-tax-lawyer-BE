from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from blog.models import BlogHero
from blog.api.serializers import BlogHeroSerializer


class BlogHeroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogHero.objects.filter(is_active=True, is_deleted=False)
    serializer_class = BlogHeroSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')
