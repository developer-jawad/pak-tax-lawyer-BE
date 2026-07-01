from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from blog.api.filters import BlogPostFilter
from blog.api.serializers import BlogPostSerializer
from blog.models import BlogPost


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.active_objects.prefetch_related(
        "tags", "content_blocks", "related_posts"
    )
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

    def get_serializer(self, *args, **kwargs):
        # Exclude detailed fields on list view
        if self.action == "list":
            kwargs.setdefault("exclude", []).extend(
                ["tags", "content_blocks", "related_posts"]
            )
        return super().get_serializer(*args, **kwargs)
