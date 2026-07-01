from django.core.cache import cache
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

BLOG_PAGE_CACHE_KEY = "api:blog:page"
BLOG_PAGE_CACHE_TTL = 60 * 60


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        try:
            cached = cache.get(BLOG_PAGE_CACHE_KEY)
        except Exception:
            cached = None
        if cached is not None:
            return Response(cached)

        hero = BlogHero.active_objects.first()
        posts = BlogPost.active_objects.prefetch_related("tags", "content_blocks", "related_posts").all()
        cta = BlogCTA.active_objects.filter(is_blog_section=True).first()
        statistics = BlogStatistic.active_objects.all()

        data = {
            "hero": BlogHeroSerializer(hero).data if hero else None,
            "posts": BlogPostSerializer(posts, many=True).data,
            "cta": BlogCTASerializer(cta).data if cta else None,
            "statistics": BlogStatisticSerializer(statistics, many=True).data,
        }
        try:
            cache.set(BLOG_PAGE_CACHE_KEY, data, BLOG_PAGE_CACHE_TTL)
        except Exception:
            pass
        return Response(data)
