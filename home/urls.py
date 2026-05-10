from django.urls import include, path
from rest_framework.routers import DefaultRouter

from home.api.views import (
    HeroSectionViewSet,
    TeamMemberViewSet,
    TeamSectionViewSet,
    TeamCTAViewSet,
    HomeSectionsViewSet,
)

router = DefaultRouter()
router.register(r'hero-sections', HeroSectionViewSet, basename='hero-section')
router.register(r'team-members', TeamMemberViewSet, basename='team-member')
router.register(r'team-sections', TeamSectionViewSet, basename='team-section')
router.register(r'team-cta', TeamCTAViewSet, basename='team-cta')
router.register(r'sections', HomeSectionsViewSet, basename='home-sections')

urlpatterns = [
    path('', include(router.urls)),
]
