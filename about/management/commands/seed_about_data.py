from django.core.management.base import BaseCommand

from about.models import (
    AboutAchievement,
    AboutCTA,
    AboutHero,
    AboutStatistic,
    AboutStatisticItem,
    AboutStatisticSection,
    AboutValue,
    WhoWeAre,
)


class Command(BaseCommand):
    help = "Seed about app with initial data"

    def handle(self, *args, **options):
        self.stdout.write("Seeding about data...")

        # Create About Hero
        about_hero, created = AboutHero.objects.get_or_create(
            title="Leading Tax Consultants",
            defaults={
                "subtitle": "in Pakistan",
                "description": "Your trusted partner in navigating Pakistani tax laws and FBR compliance. Delivering expert solutions with integrity and professionalism.",
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created AboutHero: {about_hero.title}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"AboutHero already exists: {about_hero.title}")
            )

        # Create About Hero Statistics
        hero_statistics_data = [
            {"number": "10+", "label": "Years Experience"},
            {"number": "500+", "label": "Happy Clients"},
            {"number": "100%", "label": "Success Rate"},
            {"number": "1000+", "label": "Cases Handled"},
        ]

        for stat_data in hero_statistics_data:
            statistic, created = AboutStatistic.objects.get_or_create(
                number=stat_data["number"],
                label=stat_data["label"],
                defaults={
                    "is_active": True,
                    "is_deleted": False,
                },
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created AboutStatistic: {statistic.number} - {statistic.label}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"AboutStatistic already exists: {statistic.number} - {statistic.label}"
                    )
                )

        # Create Who We Are
        who_we_are, created = WhoWeAre.objects.get_or_create(
            title="Leading Tax Consultants in Pakistan",
            defaults={
                "subtitle": "WHO WE ARE",
                "paragraphs": [
                    "Pakistan Tax Lawyer is a premier tax consultation firm specializing in Pakistani tax law and Federal Board of Revenue (FBR) compliance. With over a decade of experience, we have established ourselves as trusted advisors to individuals, businesses, and corporations across Pakistan.",
                    "Our team of highly qualified tax professionals brings deep expertise in tax planning, compliance, litigation, and advisory services. We are committed to helping our clients navigate the complex landscape of Pakistani tax laws while ensuring full compliance with FBR regulations.",
                    "Whether you're an individual taxpayer, a startup, or a large corporation, we provide tailored solutions that optimize your tax position while maintaining the highest standards of integrity and professionalism.",
                ],
                "image_overlay_title": "Professional Excellence",
                "image_overlay_description": "Delivering expert tax solutions since 2014",
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created WhoWeAre: {who_we_are.title}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"WhoWeAre already exists: {who_we_are.title}")
            )

        # Create About Statistic Section
        statistic_section, created = AboutStatisticSection.objects.get_or_create(
            title="Our Impact in Numbers",
            defaults={
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Created AboutStatisticSection: {statistic_section.title}"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f"AboutStatisticSection already exists: {statistic_section.title}"
                )
            )

        # Create About Statistic Items
        statistic_items_data = [
            {
                "icon": "People",
                "value": "500+",
                "label": "Happy Clients",
                "color": "#EE1C27",
            },
            {
                "icon": "TrendingUp",
                "value": "10+",
                "label": "Years Experience",
                "color": "#EE1C27",
            },
            {
                "icon": "Verified",
                "value": "100%",
                "label": "Success Rate",
                "color": "#EE1C27",
            },
            {
                "icon": "Gavel",
                "value": "1000+",
                "label": "Cases Handled",
                "color": "#EE1C27",
            },
        ]

        for item_data in statistic_items_data:
            item, created = AboutStatisticItem.objects.get_or_create(
                value=item_data["value"],
                label=item_data["label"],
                defaults={
                    **item_data,
                    "is_active": True,
                    "is_deleted": False,
                },
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created AboutStatisticItem: {item.value} - {item.label}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"AboutStatisticItem already exists: {item.value} - {item.label}"
                    )
                )

        # Create About Values
        values_data = [
            {
                "icon": "Verified",
                "title": "Integrity",
                "description": "We uphold the highest standards of integrity in all our actions and maintain transparency with our clients.",
            },
            {
                "icon": "WorkspacePremium",
                "title": "Excellence",
                "description": "We strive for excellence in every service we provide, ensuring the best outcomes for our clients.",
            },
            {
                "icon": "People",
                "title": "Client-Focused",
                "description": "Our clients are at the heart of everything we do. We prioritize their needs and work tirelessly for their success.",
            },
            {
                "icon": "School",
                "title": "Expertise",
                "description": "Our team comprises highly qualified tax professionals with deep knowledge of Pakistani tax laws and FBR regulations.",
            },
        ]

        for value_data in values_data:
            value, created = AboutValue.objects.get_or_create(
                title=value_data["title"],
                defaults={
                    **value_data,
                    "is_active": True,
                    "is_deleted": False,
                },
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created AboutValue: {value.title}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"AboutValue already exists: {value.title}")
                )

        # Create About Achievements
        achievements_data = [
            {
                "icon": "EmojiEvents",
                "title": "FBR Certified Consultants",
                "description": "Officially recognized by the Federal Board of Revenue",
            },
            {
                "icon": "WorkspacePremium",
                "title": "Award-Winning Service",
                "description": "Recognized for excellence in tax consultation services",
            },
            {
                "icon": "Verified",
                "title": "100% Compliance Record",
                "description": "Perfect track record with FBR compliance",
            },
        ]

        for achievement_data in achievements_data:
            achievement, created = AboutAchievement.objects.get_or_create(
                title=achievement_data["title"],
                defaults={
                    **achievement_data,
                    "is_active": True,
                    "is_deleted": False,
                },
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created AboutAchievement: {achievement.title}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"AboutAchievement already exists: {achievement.title}"
                    )
                )

        # Create About CTA
        about_cta, created = AboutCTA.objects.get_or_create(
            title="Ready to Work with Us?",
            defaults={
                "description": "Let our experienced team help you navigate Pakistani tax laws and achieve full FBR compliance",
                "phone": "+92 328 5007444",
                "email": "info@paktaxlawyer.com",
                "button_text": "Schedule Consultation",
                "button_link": "/contact",
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created AboutCTA: {about_cta.title}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"AboutCTA already exists: {about_cta.title}")
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded all about data!"))
