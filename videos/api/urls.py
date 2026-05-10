from django.urls import include, path
from rest_framework.routers import DefaultRouter

from videos.api.views import (
    VideoCTAViewSet,
    VideoHeroViewSet,
    VideoSectionViewSet,
    VideoStatisticViewSet,
    VideosViewSet,
    VideoViewSet,
)

router = DefaultRouter()
router.register(r"hero", VideoHeroViewSet, basename="video-hero")
router.register(r"statistics", VideoStatisticViewSet, basename="video-statistic")
router.register(r"videos", VideoViewSet, basename="video")
router.register(r"section", VideoSectionViewSet, basename="video-section")
router.register(r"cta", VideoCTAViewSet, basename="video-cta")
router.register(r"", VideosViewSet, basename="videos")

urlpatterns = [
    path("", include(router.urls)),
]
