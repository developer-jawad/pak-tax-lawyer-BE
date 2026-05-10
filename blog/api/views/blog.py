from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from blog.api.serializers import (
    BlogCTASerializer,
    BlogHeroSerializer,
    BlogPostSerializer,
    BlogStatisticSerializer,
)
from blog.models import BlogCTA, BlogHero, BlogPost, BlogStatistic


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        hero = BlogHero.active_objects.first()
        posts = BlogPost.active_objects.all()
        cta = BlogCTA.active_objects.filter(is_blog_section=True).first()
        statistics = BlogStatistic.active_objects.all()

        return Response(
            {
                "hero": BlogHeroSerializer(hero).data if hero else None,
                "posts": BlogPostSerializer(posts, many=True).data,
                "cta": BlogCTASerializer(cta).data if cta else None,
                "statistics": BlogStatisticSerializer(statistics, many=True).data,
            }
        )
