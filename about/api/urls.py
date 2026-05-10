from django.urls import include, path
from rest_framework.routers import DefaultRouter

from about.api.views import (
    AboutAchievementViewSet,
    AboutCTAViewSet,
    AboutHeroViewSet,
    AboutStatisticItemViewSet,
    AboutStatisticSectionViewSet,
    AboutStatisticViewSet,
    AboutValueViewSet,
    AboutViewSet,
    WhoWeAreViewSet,
)

router = DefaultRouter()
router.register(r"hero", AboutHeroViewSet, basename="about-hero")
router.register(r"statistics", AboutStatisticViewSet, basename="about-statistic")
router.register(r"who-we-are", WhoWeAreViewSet, basename="who-we-are")
router.register(
    r"statistic-section",
    AboutStatisticSectionViewSet,
    basename="about-statistic-section",
)
router.register(
    r"statistic-items", AboutStatisticItemViewSet, basename="about-statistic-item"
)
router.register(r"values", AboutValueViewSet, basename="about-value")
router.register(r"achievements", AboutAchievementViewSet, basename="about-achievement")
router.register(r"cta", AboutCTAViewSet, basename="about-cta")
router.register(r"", AboutViewSet, basename="about")

urlpatterns = [
    path("", include(router.urls)),
]
