from django.urls import include, path
from rest_framework.routers import DefaultRouter

from footer.api.views import (
    FooterBrandViewSet,
    FooterSocialLinkViewSet,
    FooterQuickLinkViewSet,
    FooterServiceLinkViewSet,
    FooterContactViewSet,
    FooterBottomSectionViewSet,
    FooterLegalLinkViewSet,
    FooterViewSet,
)

router = DefaultRouter()
router.register(r'brand', FooterBrandViewSet, basename='footer-brand')
router.register(r'social-links', FooterSocialLinkViewSet, basename='footer-social-link')
router.register(r'quick-links', FooterQuickLinkViewSet, basename='footer-quick-link')
router.register(r'service-links', FooterServiceLinkViewSet, basename='footer-service-link')
router.register(r'contact', FooterContactViewSet, basename='footer-contact')
router.register(r'bottom-section', FooterBottomSectionViewSet, basename='footer-bottom-section')
router.register(r'legal-links', FooterLegalLinkViewSet, basename='footer-legal-link')
router.register(r'', FooterViewSet, basename='footer')

urlpatterns = [
    path('', include(router.urls)),
]
