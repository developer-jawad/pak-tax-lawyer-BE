from django.core.management.base import BaseCommand
from datetime import datetime
from footer.models import (
    FooterBrand,
    FooterSocialLink,
    FooterQuickLink,
    FooterServiceLink,
    FooterContact,
    FooterBottomSection,
    FooterLegalLink,
)


class Command(BaseCommand):
    help = 'Seed footer app with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding footer data...')

        # Create Footer Brand
        brand, created = FooterBrand.objects.get_or_create(
            name="Pakistan Tax Lawyer",
            defaults={
                'description': 'Professional tax consultation services specializing in Pakistani tax law and FBR compliance. Expert guidance for individuals, businesses, and corporations across Pakistan.',
                'logo_alt': 'Pakistan Tax Lawyer Logo',
                'follow_us': 'Follow Us',
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created FooterBrand: {brand.name}'))
        else:
            self.stdout.write(self.style.WARNING(f'FooterBrand already exists: {brand.name}'))

        # Create Social Links
        social_links_data = [
            {'platform': 'Facebook', 'url': 'https://www.facebook.com/profile.php?id=61555804476159'},
            {'platform': 'Instagram', 'url': 'https://www.instagram.com'},
            {'platform': 'YouTube', 'url': 'https://www.youtube.com/@PakTaxLawyer/videos'},
            {'platform': 'LinkedIn', 'url': 'https://www.linkedin.com'},
            {'platform': 'Twitter', 'url': 'https://www.twitter.com'},
        ]

        for social_data in social_links_data:
            social_link, created = FooterSocialLink.objects.get_or_create(
                platform=social_data['platform'],
                defaults={
                    'url': social_data['url'],
                    'is_active': True,
                    'is_deleted': False,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created FooterSocialLink: {social_link.platform}'))
            else:
                self.stdout.write(self.style.WARNING(f'FooterSocialLink already exists: {social_link.platform}'))

        # Create Quick Links
        quick_links_data = [
            {'label': 'Home', 'url': '/'},
            {'label': 'About Us', 'url': '/about'},
            {'label': 'Services', 'url': '/services'},
            {'label': 'Resources', 'url': '/resources'},
            {'label': 'Videos', 'url': '/videos'},
            {'label': 'Contact', 'url': '/contact'},
        ]

        for quick_data in quick_links_data:
            quick_link, created = FooterQuickLink.objects.get_or_create(
                label=quick_data['label'],
                defaults={
                    'url': quick_data['url'],
                    'is_active': True,
                    'is_deleted': False,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created FooterQuickLink: {quick_link.label}'))
            else:
                self.stdout.write(self.style.WARNING(f'FooterQuickLink already exists: {quick_link.label}'))

        # Create Service Links
        service_links_data = [
            {'label': 'Tax Return Filing', 'url': '/services'},
            {'label': 'Tax Litigation', 'url': '/services'},
            {'label': 'Tax Planning', 'url': '/services'},
            {'label': 'Compliance Advisory', 'url': '/services'},
            {'label': 'Corporate Tax Services', 'url': '/services'},
            {'label': 'NRP Tax Services', 'url': '/services'},
        ]

        for service_data in service_links_data:
            service_link, created = FooterServiceLink.objects.get_or_create(
                label=service_data['label'],
                defaults={
                    'url': service_data['url'],
                    'is_active': True,
                    'is_deleted': False,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created FooterServiceLink: {service_link.label}'))
            else:
                self.stdout.write(self.style.WARNING(f'FooterServiceLink already exists: {service_link.label}'))

        # Create Footer Contact
        contact, created = FooterContact.objects.get_or_create(
            title='Contact Us',
            defaults={
                'address_label': 'Office Address',
                'address_value': 'First Floor Easypaisa Bank, Main Jaranwala Road Sharqpur, Sheikhupura, Punjab, Pakistan',
                'phone_label': 'Phone',
                'phone_value': '+92 328 5007444',
                'email_label': 'Email',
                'email_value': 'info@paktaxlawyer.com',
                'business_hours_label': 'Business Hours',
                'business_hours_value': 'Mon - Sat: 9:00 AM - 6:00 PM',
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created FooterContact: {contact.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'FooterContact already exists: {contact.title}'))

        # Create Bottom Section
        current_year = datetime.now().year
        bottom_section, created = FooterBottomSection.objects.get_or_create(
            copyright=f'© {current_year} Pakistan Tax Lawyer. All rights reserved. | Designed & Developed with ❤️',
            defaults={
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created FooterBottomSection'))
        else:
            self.stdout.write(self.style.WARNING(f'FooterBottomSection already exists'))

        # Create Legal Links
        legal_links_data = [
            {'label': 'Privacy Policy', 'url': '/privacy'},
            {'label': 'Terms of Service', 'url': '/terms'},
            {'label': 'Disclaimer', 'url': '/disclaimer'},
        ]

        for legal_data in legal_links_data:
            legal_link, created = FooterLegalLink.objects.get_or_create(
                label=legal_data['label'],
                defaults={
                    'url': legal_data['url'],
                    'is_active': True,
                    'is_deleted': False,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created FooterLegalLink: {legal_link.label}'))
            else:
                self.stdout.write(self.style.WARNING(f'FooterLegalLink already exists: {legal_link.label}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded all footer data!'))
