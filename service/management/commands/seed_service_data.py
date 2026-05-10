import json
import os
from django.core.management.base import BaseCommand

from service.models import (
    Service,
    ServiceBenefit,
    ServiceCTA,
    ServiceHero,
    ServiceSection,
    ServiceStatistic,
)


class Command(BaseCommand):
    help = 'Seed service data from services.json file'

    def handle(self, *args, **kwargs):
        # Load JSON data
        json_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'data',
            'services.json'
        )
        
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        # Create or get ServiceSection
        service_section, created = ServiceSection.objects.get_or_create(
            title='Our Services',
            defaults={
                'subtitle': 'WHAT WE OFFER',
                'description': 'Comprehensive tax consultation and FBR compliance services tailored to your needs',
                'cta_title': 'Need Expert Tax Consultation?',
                'cta_description': 'Get professional tax advice from experienced consultants specializing in Pakistani tax law and FBR compliance',
                'primary_button': 'Schedule Consultation',
                'secondary_button': 'View All Services',
                'features_label': 'Key Features:'
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created ServiceSection: {service_section.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'ServiceSection already exists: {service_section.title}'))
        
        # Seed Hero
        hero_data = data.get('hero', {})
        hero, created = ServiceHero.objects.get_or_create(
            title=hero_data.get('title'),
            defaults={
                'subtitle': hero_data.get('subtitle')
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created ServiceHero: {hero.title}'))
        
        # Seed Statistics
        ServiceStatistic.objects.all().delete()
        for stat_data in data.get('statistics', []):
            statistic = ServiceStatistic.objects.create(
                number=stat_data.get('number'),
                label=stat_data.get('label')
            )
            self.stdout.write(self.style.SUCCESS(f'Created ServiceStatistic: {statistic.number} - {statistic.label}'))
        
        # Seed Benefits
        ServiceBenefit.objects.all().delete()
        for benefit_data in data.get('benefits', []):
            benefit = ServiceBenefit.objects.create(
                icon=benefit_data.get('icon'),
                text=benefit_data.get('text')
            )
            self.stdout.write(self.style.SUCCESS(f'Created ServiceBenefit: {benefit.text}'))
        
        # Seed Services
        Service.objects.filter(service_section=service_section).delete()
        for service_data in data.get('services', []):
            service = Service.objects.create(
                service_section=service_section,
                icon=service_data.get('icon'),
                title=service_data.get('title'),
                description=service_data.get('description'),
                features=service_data.get('features', []),
                color=service_data.get('color'),
                button_text=service_data.get('buttonText'),
                popular=service_data.get('popular', False)
            )
            self.stdout.write(self.style.SUCCESS(f'Created Service: {service.title}'))
        
        # Seed CTA
        cta_data = data.get('cta', {})
        cta, created = ServiceCTA.objects.get_or_create(
            title=cta_data.get('title'),
            defaults={
                'description': cta_data.get('description'),
                'button_text': cta_data.get('buttonText'),
                'button_link': cta_data.get('buttonLink', ''),
                'is_service_section': cta_data.get('isServiceSection', False)
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created ServiceCTA: {cta.title}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded all service data!'))
