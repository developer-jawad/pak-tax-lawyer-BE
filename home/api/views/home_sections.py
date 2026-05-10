from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from home.models import (
    HeroSection,
    TeamMember,
    TeamCTA,
    TeamSection,
    Testimonial,
    TestimonialCTA,
    TestimonialSection,
)
from home.api.serializers import (
    HeroSectionSerializer,
    TeamSectionSerializer,
    TeamMemberSerializer,
    TeamCTASerializer,
    TestimonialSectionSerializer,
    TestimonialSerializer,
    TestimonialCTASerializer,
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

from blog.models import (
    BlogPost,
    BlogCTA,
    BlogSection,
)
from blog.api.serializers import (
    BlogSectionSerializer,
    BlogPostSerializer,
    BlogCTASerializer,
)

from videos.models import (
    VideoSection,
    Video,
    VideoCTA,
)
from videos.api.serializers import (
    VideoSectionSerializer,
    VideoSerializer,
    VideoCTASerializer,
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
        
        # Testimonial Section
        testimonial_section = TestimonialSection.active_objects.first()
        testimonials = Testimonial.active_objects.all()
        testimonial_cta = TestimonialCTA.active_objects.filter(is_testimonial_section=True).first()
        
        # Blog Section
        blog_section = BlogSection.active_objects.first()
        blog_posts = BlogPost.active_objects.all()[:6]
        blog_cta = BlogCTA.active_objects.filter(is_blog_section=True).first()

        # Video Section
        video_section = VideoSection.active_objects.first()
        videos = Video.active_objects.all()[:6]
        video_cta = VideoCTA.active_objects.first()

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
            'testimonial_section': {
                'section': TestimonialSectionSerializer(testimonial_section).data if testimonial_section else None,
                'testimonials': TestimonialSerializer(testimonials, many=True).data,
                'cta': TestimonialCTASerializer(testimonial_cta).data if testimonial_cta else None,
            },
            'blog_section': {
                'section': BlogSectionSerializer(blog_section).data if blog_section else None,
                'blog_posts': BlogPostSerializer(blog_posts, many=True).data,
                'cta': BlogCTASerializer(blog_cta).data if blog_cta else None,
            },
            'video_section': {
                'section': VideoSectionSerializer(video_section).data if video_section else None,
                'videos': VideoSerializer(videos, many=True).data,
                'cta': VideoCTASerializer(video_cta).data if video_cta else None,
            },
        })
