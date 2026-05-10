from django.core.management.base import BaseCommand
from blog.models import BlogHero, BlogSection, BlogPost, BlogCTA, BlogStatistic
from common.constants import BLOG_CATEGORIES
from datetime import date


class Command(BaseCommand):
    help = 'Seed blog app with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding blog data...')

        # Create Blog Hero
        blog_hero, created = BlogHero.objects.get_or_create(
            title='Tax Insights & Expert Resources',
            defaults={
                'subtitle': 'Stay informed with expert articles, practical guides, and the latest updates on Pakistani tax law and FBR compliance.',
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created BlogHero: {blog_hero.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'BlogHero already exists: {blog_hero.title}'))

        # Create Blog Statistics
        statistics_data = [
            {'number': '100+', 'label': 'Articles Published'},
            {'number': '15+', 'label': 'Expert Topics'},
            {'number': '50K+', 'label': 'Monthly Readers'},
            {'number': 'Weekly', 'label': 'New Content'},
        ]

        for stat_data in statistics_data:
            statistic, created = BlogStatistic.objects.get_or_create(
                number=stat_data['number'],
                label=stat_data['label'],
                defaults={
                    'is_active': True,
                    'is_deleted': False,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created BlogStatistic: {statistic.number} - {statistic.label}'))
            else:
                self.stdout.write(self.style.WARNING(f'BlogStatistic already exists: {statistic.number} - {statistic.label}'))

        # Create Blog Section
        blog_section, created = BlogSection.objects.get_or_create(
            title='Latest Tax Blogs',
            defaults={
                'subtitle': 'INSIGHTS & UPDATES',
                'description': 'Stay informed with expert insights on Pakistani tax laws, FBR updates, and compliance strategies',
                'categories': BLOG_CATEGORIES.all,
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created BlogSection: {blog_section.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'BlogSection already exists: {blog_section.title}'))

        # Create Blog Posts
        blog_posts_data = [
            {
                'title': 'Understanding FBR Tax Return Filing Process in Pakistan 2025',
                'excerpt': 'A comprehensive guide to filing your tax returns with the Federal Board of Revenue, including deadlines, requirements, and common mistakes to avoid.',
                'author': 'Advocate Asad Mahmood',
                'date': date(2026, 5, 8),
                'read_time': '5 min read',
                'category': 1,  # Tax Filing
                'image_url': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800&q=80',
                'slug': 'fbr-tax-return-filing-process-2025',
            },
            {
                'title': 'Tax Benefits for Startups and Small Businesses in Pakistan',
                'excerpt': 'Discover the tax incentives, exemptions, and benefits available for new businesses and startups under Pakistani tax law.',
                'author': 'Sadia Akhtar',
                'date': date(2026, 5, 5),
                'read_time': '7 min read',
                'category': 2,  # Business Tax
                'image_url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80',
                'slug': 'tax-benefits-startups-pakistan',
            },
            {
                'title': 'How to Become a Tax Filer: Complete Guide for Individuals',
                'excerpt': 'Step-by-step process to register as an active tax filer with FBR and enjoy the benefits of filer status in Pakistan.',
                'author': 'Kamran Ali',
                'date': date(2026, 5, 2),
                'read_time': '6 min read',
                'category': 3,  # Tax Planning
                'image_url': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=800&q=80',
                'slug': 'become-tax-filer-guide',
            },
            {
                'title': 'Sales Tax Registration: Requirements and Procedures',
                'excerpt': 'Everything you need to know about sales tax registration, compliance requirements, and filing obligations for businesses.',
                'author': 'Fatima Noor',
                'date': date(2026, 4, 28),
                'read_time': '8 min read',
                'category': 4,  # Sales Tax
                'image_url': 'https://images.unsplash.com/photo-1554224154-26032ffc0d07?w=800&q=80',
                'slug': 'sales-tax-registration-guide',
            },
            {
                'title': 'NRP Tax Guide: Filing Returns as a Non-Resident Pakistani',
                'excerpt': 'Comprehensive guide for Non-Resident Pakistanis on tax obligations, property tax, and investment income in Pakistan.',
                'author': 'Ahmed Raza',
                'date': date(2026, 4, 25),
                'read_time': '9 min read',
                'category': 5,  # NRP Tax
                'image_url': 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=800&q=80',
                'slug': 'nrp-tax-filing-guide',
            },
            {
                'title': 'Corporate Tax Planning Strategies for 2025',
                'excerpt': 'Advanced tax planning strategies for corporations to optimize tax liability while ensuring full compliance with FBR regulations.',
                'author': 'Ayesha Malik',
                'date': date(2026, 4, 22),
                'read_time': '10 min read',
                'category': 6,  # Corporate Tax
                'image_url': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800&q=80',
                'slug': 'corporate-tax-planning-2025',
            },
            {
                'title': 'Tax Deductions You Should Know About in Pakistan',
                'excerpt': 'Maximize your tax savings by understanding all available deductions and exemptions under Pakistani tax law.',
                'author': 'Advocate Asad Mahmood',
                'date': date(2026, 4, 18),
                'read_time': '6 min read',
                'category': 3,  # Tax Planning
                'image_url': 'https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=800&q=80',
                'slug': 'tax-deductions-pakistan',
            },
            {
                'title': 'Understanding Withholding Tax in Pakistan',
                'excerpt': 'Complete guide to withholding tax obligations, rates, and compliance requirements for businesses and individuals.',
                'author': 'Sadia Akhtar',
                'date': date(2026, 4, 15),
                'read_time': '7 min read',
                'category': 2,  # Business Tax
                'image_url': 'https://images.unsplash.com/photo-1554224154-26032ffc0d07?w=800&q=80',
                'slug': 'withholding-tax-pakistan',
            },
        ]

        for post_data in blog_posts_data:
            blog_post, created = BlogPost.objects.get_or_create(
                slug=post_data['slug'],
                defaults={
                    **post_data,
                    'is_active': True,
                    'is_deleted': False,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created BlogPost: {blog_post.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'BlogPost already exists: {blog_post.title}'))

        # Create Blog CTA
        blog_cta, created = BlogCTA.objects.get_or_create(
            button_text='View All Blogs',
            defaults={
                'button_link': '/blogs',
                'is_blog_section': True,
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created BlogCTA: {blog_cta.button_text}'))
        else:
            self.stdout.write(self.style.WARNING(f'BlogCTA already exists: {blog_cta.button_text}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded all blog data!'))
