from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.api.views import (
    BlogCTAViewSet,
    BlogHeroViewSet,
    BlogPostViewSet,
    BlogSectionViewSet,
    BlogStatisticViewSet,
    BlogViewSet,
)

router = DefaultRouter()
router.register(r"hero", BlogHeroViewSet, basename="blog-hero")
router.register(r"posts", BlogPostViewSet, basename="blog-post")
router.register(r"sections", BlogSectionViewSet, basename="blog-section")
router.register(r"cta", BlogCTAViewSet, basename="blog-cta")
router.register(r"statistics", BlogStatisticViewSet, basename="blog-statistic")
router.register(r"", BlogViewSet, basename="blogs")

urlpatterns = [
    path("", include(router.urls)),
]
