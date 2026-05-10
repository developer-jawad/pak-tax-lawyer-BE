from django.urls import include, path
from rest_framework.routers import DefaultRouter

from service.api.views import (
    ServiceBenefitViewSet,
    ServiceCTAViewSet,
    ServiceHeroViewSet,
    ServiceSectionViewSet,
    ServiceStatisticViewSet,
    ServiceViewSet,
)

router = DefaultRouter()
router.register(r'hero', ServiceHeroViewSet, basename='service-hero')
router.register(r'statistics', ServiceStatisticViewSet, basename='service-statistic')
router.register(r'benefits', ServiceBenefitViewSet, basename='service-benefit')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'service-sections', ServiceSectionViewSet, basename='service-section')
router.register(r'cta', ServiceCTAViewSet, basename='service-cta')

urlpatterns = [
    path('', include(router.urls)),
]
