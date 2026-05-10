from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from home.models import (
    HeroSection,
    TeamMember,
    TeamCTA,
    TeamSection,
)
from home.api.serializers import (
    HeroSectionSerializer,
    TeamSectionSerializer,
    TeamMemberSerializer,
    TeamCTASerializer,
)

from service.models import (
    Service,
    ServiceCTA,
    ServiceSection,
)
from service.api.serializers import (
    ServiceSectionSerializer,
    ServiceSerializer,
    ServiceCTASerializer,
)


class HomeSectionsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        # Hero Section
        hero_section = HeroSection.objects.filter(is_active=True, is_deleted=False).first()
        
        # Service Section
        service_section = ServiceSection.active_objects.first()
        services = Service.active_objects.all()
        service_cta = ServiceCTA.active_objects.filter(is_service_section=True).first()
        
        # Team Section
        team_section = TeamSection.active_objects.first()
        team_members = TeamMember.active_objects.all()
        team_cta = TeamCTA.active_objects.filter(is_team_section=True).first()

        return Response({
            'hero_section': HeroSectionSerializer(hero_section).data if hero_section else None,
            'service_section': {
                'section': ServiceSectionSerializer(service_section).data if service_section else None,
                'services': ServiceSerializer(services, many=True).data,
                'cta': ServiceCTASerializer(service_cta).data if service_cta else None,
            },
            'team_section': {
                'section': TeamSectionSerializer(team_section).data if team_section else None,
                'team_members': TeamMemberSerializer(team_members, many=True).data,
                'cta': TeamCTASerializer(team_cta).data if team_cta else None,
            },
        })
