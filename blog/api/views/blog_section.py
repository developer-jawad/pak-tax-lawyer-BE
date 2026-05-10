from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from blog.models import (
    BlogPost,
    BlogCTA,
    BlogSection,
)
from blog.api.serializers import (
    BlogSectionSerializer,
    BlogPostSerializer,
    BlogCTASerializer,
)


class BlogSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogSection.objects.all()
    serializer_class = BlogSectionSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        blog_section = BlogSection.active_objects.first()
        blog_posts = BlogPost.active_objects.all()
        cta = BlogCTA.active_objects.filter(is_blog_section=True).first()

        return Response({
            'blog_section': BlogSectionSerializer(blog_section).data if blog_section else None,
            'blog_posts': BlogPostSerializer(blog_posts, many=True).data,
            'cta': BlogCTASerializer(cta).data if cta else None,
        })
