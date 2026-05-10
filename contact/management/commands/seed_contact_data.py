from django.core.management.base import BaseCommand
from contact.models import (
    ContactHero,
    ContactStatistic,
    ContactInfo,
    ContactForm,
    ContactMap,
    ContactCTA,
)


class Command(BaseCommand):
    help = 'Seed contact app with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding contact data...')

        # Create Contact Hero
        contact_hero, created = ContactHero.objects.get_or_create(
            title="Let's Discuss Your",
            defaults={
                'subtitle': 'Tax Consultation Needs',
                'description': 'Expert tax consultants ready to assist you with FBR compliance, tax filing, and personalized tax planning solutions.',
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created ContactHero: {contact_hero.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'ContactHero already exists: {contact_hero.title}'))

        # Create Contact Hero Statistics
        hero_statistics_data = [
            {'icon': 'Schedule', 'value': '24h', 'label': 'Response Time'},
            {'icon': 'Support', 'value': '10+', 'label': 'Years Experience'},
            {'icon': 'VerifiedUser', 'value': '100%', 'label': 'Confidential'},
            {'icon': 'CheckCircle', 'value': '500+', 'label': 'Clients Served'},
        ]

        for stat_data in hero_statistics_data:
            statistic, created = ContactStatistic.objects.get_or_create(
                icon=stat_data['icon'],
                value=stat_data['value'],
                label=stat_data['label'],
                defaults={
                    'is_active': True,
                    'is_deleted': False,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created ContactStatistic: {statistic.value} - {statistic.label}'))
            else:
                self.stdout.write(self.style.WARNING(f'ContactStatistic already exists: {statistic.value} - {statistic.label}'))

        # Create Contact Info
        contact_info_data = [
            {'icon': 'Phone', 'title': 'Phone', 'details': '+92 328 5007444', 'subtitle': 'Mon-Fri 9am to 6pm'},
            {'icon': 'Email', 'title': 'Email', 'details': 'info@paktaxlawyer.com', 'subtitle': 'Online support'},
            {'icon': 'LocationOn', 'title': 'Office', 'details': 'Islamabad, Pakistan', 'subtitle': 'Visit us'},
            {'icon': 'AccessTime', 'title': 'Working Hours', 'details': 'Mon - Fri: 9:00 AM - 6:00 PM', 'subtitle': 'Sat: 10:00 AM - 2:00 PM'},
        ]

        for info_data in contact_info_data:
            contact_info, created = ContactInfo.objects.get_or_create(
                title=info_data['title'],
                defaults={
                    **info_data,
                    'is_active': True,
                    'is_deleted': False,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created ContactInfo: {contact_info.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'ContactInfo already exists: {contact_info.title}'))

        # Create Contact Form
        contact_form, created = ContactForm.objects.get_or_create(
            title='Send us a Message',
            defaults={
                'description': 'Fill out the form below and we\'ll get back to you as soon as possible',
                'name_label': 'Full Name',
                'email_label': 'Email Address',
                'phone_label': 'Phone Number',
                'subject_label': 'Subject',
                'message_label': 'Message',
                'submit_button_text': 'Send Message',
                'loading_text': 'Sending...',
                'success_message': 'Thank you! Your message has been sent successfully. We will contact you soon.',
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created ContactForm: {contact_form.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'ContactForm already exists: {contact_form.title}'))

        # Create Contact Map
        contact_map, created = ContactMap.objects.get_or_create(
            title='Office Location',
            defaults={
                'iframe_url': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d212270.5667814695!2d72.8088599!3d33.6844202!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38dfbfd07891722f%3A0x6059515c3bdb02b6!2sIslamabad%2C%20Pakistan!5e0!3m2!1sen!2s!4v1234567890',
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created ContactMap: {contact_map.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'ContactMap already exists: {contact_map.title}'))

        # Create Contact CTA
        contact_cta, created = ContactCTA.objects.get_or_create(
            title='Why Choose Pakistan Tax Lawyer?',
            defaults={
                'icon': 'CheckCircle',
                'description': 'With over 10 years of experience in Pakistani tax law and FBR compliance, we provide expert guidance tailored to your specific needs. Our team of certified professionals ensures accurate, timely, and compliant tax solutions for individuals and businesses across Pakistan.',
                'is_active': True,
                'is_deleted': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created ContactCTA: {contact_cta.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'ContactCTA already exists: {contact_cta.title}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded all contact data!'))
