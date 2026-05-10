from django.urls import include, path
from rest_framework.routers import DefaultRouter

from contact.api.views import (
    ContactCTAViewSet,
    ContactFormViewSet,
    ContactHeroViewSet,
    ContactInfoViewSet,
    ContactMapViewSet,
    ContactStatisticViewSet,
    ContactViewSet,
)

router = DefaultRouter()
router.register(r"hero", ContactHeroViewSet, basename="contact-hero")
router.register(r"statistics", ContactStatisticViewSet, basename="contact-statistic")
router.register(r"contact-info", ContactInfoViewSet, basename="contact-info")
router.register(r"form", ContactFormViewSet, basename="contact-form")
router.register(r"map", ContactMapViewSet, basename="contact-map")
router.register(r"cta", ContactCTAViewSet, basename="contact-cta")
router.register(r"", ContactViewSet, basename="contact")

urlpatterns = [
    path("", include(router.urls)),
]
