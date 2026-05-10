from django.urls import include, path
from rest_framework.routers import DefaultRouter

from home.views import HeroSectionViewSet

router = DefaultRouter()
router.register(r'hero-sections', HeroSectionViewSet, basename='hero-section')

urlpatterns = [
    path('', include(router.urls)),
]
