from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from blog.api.filters import BlogPostFilter
from blog.api.serializers import BlogPostSerializer
from blog.models import BlogPost


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.filter(is_active=True, is_deleted=False)
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BlogPostFilter
    search_fields = [
        "title",
    ]
    lookup_field = "slug"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-date", "-created_at")
