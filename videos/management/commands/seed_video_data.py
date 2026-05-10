from django.core.management.base import BaseCommand
from videos.models import (
    VideoHero,
    VideoStatistic,
    Video,
    VideoSection,
    VideoCTA,
)
from common.constants import BLOG_CATEGORIES


class Command(BaseCommand):
    help = 'Seed videos app with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding videos data...')

        # Create Video Hero
        video_hero, created = VideoHero.objects.get_or_create(
            title='Master Pakistani Tax Laws',
            defaults={
                'subtitle': 'Through Expert Videos',
                'description': 'Comprehensive video tutorials on FBR compliance, tax filing, and planning strategies. Learn from certified tax professionals with real-world examples.',
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created VideoHero: {video_hero.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'VideoHero already exists: {video_hero.title}'))

        # Create Video Hero Statistics
        hero_statistics_data = [
            {'number': '50+', 'label': 'Video Tutorials'},
            {'number': '10+', 'label': 'Expert Topics'},
            {'number': '5K+', 'label': 'Students Helped'},
            {'number': '4.9', 'label': 'Average Rating'},
        ]

        for stat_data in hero_statistics_data:
            statistic, created = VideoStatistic.objects.get_or_create(
                number=stat_data['number'],
                label=stat_data['label'],
                defaults={
                    'is_active': True,
                    'is_deleted': False,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created VideoStatistic: {statistic.number} - {statistic.label}'))
            else:
                self.stdout.write(self.style.WARNING(f'VideoStatistic already exists: {statistic.number} - {statistic.label}'))

        # Create Videos
        videos_data = [
            {
                'title': 'How to File Income Tax Returns in Pakistan',
                'description': 'Complete step-by-step guide on filing your income tax returns with FBR online portal.',
                'thumbnail': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800&h=450&fit=crop',
                'duration': '12:45',
                'views': '15.2K',
                'category': BLOG_CATEGORIES.tax_filing,
                'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
                'trending': True,
            },
            {
                'title': 'Understanding Sales Tax in Pakistan',
                'description': 'Learn about sales tax registration, filing, and compliance requirements for businesses.',
                'thumbnail': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=450&fit=crop',
                'duration': '18:30',
                'views': '12.8K',
                'category': BLOG_CATEGORIES.sales_tax,
                'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
                'new': True,
            },
            {
                'title': 'Tax Planning Strategies for Businesses',
                'description': 'Expert tips on optimizing your business tax position while staying compliant with FBR.',
                'thumbnail': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=450&fit=crop',
                'duration': '22:15',
                'views': '18.5K',
                'category': BLOG_CATEGORIES.tax_planning,
                'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
                'trending': True,
            },
            {
                'title': 'NRP Tax Guide - Non-Resident Pakistanis',
                'description': 'Everything NRPs need to know about tax obligations, property tax, and remittances.',
                'thumbnail': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=800&h=450&fit=crop',
                'duration': '15:20',
                'views': '9.3K',
                'category': BLOG_CATEGORIES.nrp_tax,
                'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
                'new': True,
            },
            {
                'title': 'Dealing with FBR Tax Audits',
                'description': 'How to prepare for and handle FBR tax audits with confidence and proper documentation.',
                'thumbnail': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800&h=450&fit=crop',
                'duration': '20:10',
                'views': '11.7K',
                'category': BLOG_CATEGORIES.tax_filing,
                'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
            },
            {
                'title': 'Withholding Tax Explained',
                'description': 'Understanding withholding tax obligations, rates, and filing requirements in Pakistan.',
                'thumbnail': 'https://images.unsplash.com/photo-1434626881859-194d67b2b86f?w=800&h=450&fit=crop',
                'duration': '14:55',
                'views': '8.9K',
                'category': BLOG_CATEGORIES.tax_filing,
                'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
            },
        ]

        for video_data in videos_data:
            video, created = Video.objects.get_or_create(
                title=video_data['title'],
                defaults={
                    **video_data,
                    'is_active': True,
                    'is_deleted': False,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Video: {video.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Video already exists: {video.title}'))

        # Create Video Section
        video_section, created = VideoSection.objects.get_or_create(
            title='Tax Related Video',
            defaults={
                'subtitle': 'EDUCATIONAL CONTENT',
                'description': 'Learn about Pakistani tax laws, FBR procedures, and compliance requirements through our expert video tutorials',
                'search_placeholder': 'Search videos...',
                'no_results': 'No videos found',
                'try_adjusting': 'Try adjusting your search or filters',
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created VideoSection: {video_section.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'VideoSection already exists: {video_section.title}'))

        # Create Video CTA
        video_cta, created = VideoCTA.objects.get_or_create(
            title='Subscribe to Our YouTube Channel',
            defaults={
                'description': 'Stay updated with the latest tax tips, FBR updates, and compliance guidelines. New videos every week!',
                'video_count': '100+',
                'video_count_label': 'Educational Videos',
                'button_text': 'Subscribe Now',
                'button_link': 'https://youtube.com',
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created VideoCTA: {video_cta.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'VideoCTA already exists: {video_cta.title}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded all videos data!'))
