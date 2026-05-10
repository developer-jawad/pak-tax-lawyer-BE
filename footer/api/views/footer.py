from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from footer.models import (
    FooterBrand,
    FooterSocialLink,
    FooterQuickLink,
    FooterServiceLink,
    FooterContact,
    FooterBottomSection,
    FooterLegalLink,
)
from footer.api.serializers import (
    FooterBrandSerializer,
    FooterSocialLinkSerializer,
    FooterQuickLinkSerializer,
    FooterServiceLinkSerializer,
    FooterContactSerializer,
    FooterBottomSectionSerializer,
    FooterLegalLinkSerializer,
)


class FooterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterBrand.objects.all()
    serializer_class = FooterBrandSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        brand = FooterBrand.active_objects.first()
        social_links = FooterSocialLink.active_objects.all()
        quick_links = FooterQuickLink.active_objects.all()
        service_links = FooterServiceLink.active_objects.all()
        contact = FooterContact.active_objects.first()
        bottom_section = FooterBottomSection.active_objects.first()
        legal_links = FooterLegalLink.active_objects.all()

        return Response({
            'brand': FooterBrandSerializer(brand).data if brand else None,
            'social_links': FooterSocialLinkSerializer(social_links, many=True).data,
            'quick_links': {
                'title': 'Quick Links',
                'links': FooterQuickLinkSerializer(quick_links, many=True).data,
            },
            'services': {
                'title': 'Our Services',
                'links': FooterServiceLinkSerializer(service_links, many=True).data,
            },
            'contact': FooterContactSerializer(contact).data if contact else None,
            'bottom_section': {
                'copyright': FooterBottomSectionSerializer(bottom_section).data if bottom_section else None,
                'legal_links': FooterLegalLinkSerializer(legal_links, many=True).data,
            },
        })
