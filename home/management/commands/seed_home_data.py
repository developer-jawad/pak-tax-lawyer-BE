from django.core.management.base import BaseCommand

from home.models import (
    HeroSection,
    TeamCTA,
    TeamMember,
    TeamSection,
    Testimonial,
    TestimonialCTA,
    TestimonialSection,
)


class Command(BaseCommand):
    help = "Seed home app with initial data"

    def handle(self, *args, **options):
        self.stdout.write("Seeding home data...")

        # Create Hero Section
        hero_section, created = HeroSection.objects.get_or_create(
            title="Expert Tax Consultation Services",
            defaults={
                "subtitle": "Your Trusted Tax Partner in Pakistan",
                "description": "We provide comprehensive tax consulting, filing, and compliance services for individuals and businesses across Pakistan. Our expert team ensures 100% FBR compliance while maximizing your tax savings.",
                "button_text": "Get Started",
                "button_link": "/contact",
                "background_gradient": "linear-gradient(135deg, #000000 0%, #333333 100%)",
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created HeroSection: {hero_section.title}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"HeroSection already exists: {hero_section.title}")
            )

        # Create Team Section
        team_section, created = TeamSection.objects.get_or_create(
            title="Meet Our Tax Professionals",
            defaults={
                "subtitle": "OUR EXPERT TEAM",
                "description": "Experienced tax consultants and legal experts dedicated to providing exceptional service",
                "credentials_label": "Credentials:",
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created TeamSection: {team_section.title}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"TeamSection already exists: {team_section.title}")
            )

        # Create Team Members
        team_members_data = [
            {
                "name": "Advocate Asad Mahmood",
                "position": "Managing Partner",
                "specialization": "Tax Litigation & Corporate Tax",
                "bio": "Over 15 years of experience in tax law with expertise in complex tax litigation and corporate restructuring.",
                "credentials": ["LLB", "LLM (Tax Law)", "Advocate High Court"],
                "email": "asad.mahmood@example.com",
                "phone": "+92-300-1234567",
                "linkedin": "#",
                "featured": True,
                "featured_label": "SENIOR PARTNER",
            },
            {
                "name": "Sadia Akhtar",
                "position": "Senior Tax Consultant",
                "specialization": "FBR Compliance & Tax Planning",
                "bio": "Chartered accountant with 12+ years specializing in tax compliance, planning, and FBR regulatory matters.",
                "credentials": ["CA", "ACCA", "MBA (Finance)"],
                "email": "sadia.akhtar@example.com",
                "phone": "+92-300-2345678",
                "linkedin": "#",
                "featured": True,
                "featured_label": "SENIOR PARTNER",
            },
            {
                "name": "Advocate Kamran Ali",
                "position": "Partner",
                "specialization": "International Tax & Transfer Pricing",
                "bio": "Expert in international taxation, transfer pricing, and cross-border transactions with global firm experience.",
                "credentials": ["LLB", "LLM (International Tax)", "CTP"],
                "email": "kamran.ali@example.com",
                "phone": "+92-300-3456789",
                "linkedin": "#",
            },
            {
                "name": "Fatima Noor",
                "position": "Tax Manager",
                "specialization": "Sales Tax & Indirect Taxation",
                "bio": "Specialized in sales tax, federal excise, and customs matters with extensive FBR audit experience.",
                "credentials": ["CA", "B.Com"],
                "email": "fatima.noor@example.com",
                "phone": "+92-300-4567890",
            },
            {
                "name": "Ahmed Raza",
                "position": "Senior Associate",
                "specialization": "Tax Litigation & Appeals",
                "bio": "Experienced in representing clients before tax tribunals and appellate authorities across Pakistan.",
                "credentials": ["LLB", "Advocate District Court"],
                "email": "ahmed.raza@example.com",
                "phone": "+92-300-5678901",
            },
            {
                "name": "Ayesha Malik",
                "position": "Tax Consultant",
                "specialization": "NRP & Individual Tax Services",
                "bio": "Dedicated to helping non-resident Pakistanis and individuals with tax compliance and planning.",
                "credentials": ["CA", "M.Com"],
                "email": "ayesha.malik@example.com",
                "phone": "+92-300-6789012",
            },
        ]

        for member_data in team_members_data:
            team_member, created = TeamMember.objects.get_or_create(
                name=member_data["name"],
                defaults={
                    **member_data,
                    "is_active": True,
                    "is_deleted": False,
                },
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created TeamMember: {team_member.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"TeamMember already exists: {team_member.name}")
                )

        # Create Team CTA
        team_cta, created = TeamCTA.objects.get_or_create(
            title="Join Our Growing Team",
            defaults={
                "description": "We're always looking for talented tax professionals and legal experts to join our team. If you're passionate about tax law and client service, we'd love to hear from you.",
                "email": "careers@example.com",
                "is_team_section": True,
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Created TeamCTA: {team_cta.title}"))
        else:
            self.stdout.write(
                self.style.WARNING(f"TeamCTA already exists: {team_cta.title}")
            )

        # Create Testimonial Section
        testimonial_section, created = TestimonialSection.objects.get_or_create(
            title="What Our Clients Say",
            defaults={
                "subtitle": "CLIENT TESTIMONIALS",
                "description": "Trusted by businesses and individuals across Pakistan for expert tax consultation and FBR compliance services",
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Created TestimonialSection: {testimonial_section.title}"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f"TestimonialSection already exists: {testimonial_section.title}"
                )
            )

        # Create Testimonials
        testimonials_data = [
            {
                "name": "Ahmed Hassan",
                "role": "CEO",
                "company": "Hassan Textiles Ltd",
                "avatar": "AH",
                "rating": 5,
                "testimonial": "Outstanding service! They helped us navigate complex FBR regulations and saved our company significant tax liabilities. Their expertise in Pakistani tax law is unmatched.",
                "location": "Karachi",
                "featured": True,
            },
            {
                "name": "Fatima Khan",
                "role": "Business Owner",
                "company": "Khan Enterprises",
                "avatar": "FK",
                "rating": 5,
                "testimonial": "Professional, knowledgeable, and responsive. They handled our tax audit with exceptional skill and kept us informed throughout the entire process. Highly recommended!",
                "location": "Lahore",
                "featured": True,
            },
            {
                "name": "Muhammad Ali",
                "role": "Director",
                "company": "Ali Trading Co.",
                "avatar": "MA",
                "rating": 5,
                "testimonial": "Their tax planning strategies have been invaluable to our business growth. They understand the nuances of Pakistani tax law and provide practical, effective solutions.",
                "location": "Islamabad",
                "featured": True,
            },
            {
                "name": "Sarah Malik",
                "role": "NRP",
                "company": "Individual Taxpayer",
                "avatar": "SM",
                "rating": 5,
                "testimonial": "As a non-resident Pakistani, filing taxes was always confusing. They made the entire process smooth and stress-free. Excellent communication and timely service.",
                "location": "Dubai, UAE",
                "featured": True,
            },
            {
                "name": "Imran Siddiqui",
                "role": "CFO",
                "company": "Siddiqui Industries",
                "avatar": "IS",
                "rating": 5,
                "testimonial": "We have been working with them for over 3 years. Their deep understanding of tax compliance and proactive approach has been instrumental in our financial planning.",
                "location": "Faisalabad",
            },
            {
                "name": "Ayesha Rahman",
                "role": "Entrepreneur",
                "company": "Rahman Consulting",
                "avatar": "AR",
                "rating": 5,
                "testimonial": "Exceptional tax consultants! They helped me set up my business with proper tax structure from day one. Their advice has been crucial for my startup success.",
                "location": "Rawalpindi",
            },
        ]

        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                name=testimonial_data["name"],
                defaults={
                    **testimonial_data,
                    "is_active": True,
                    "is_deleted": False,
                },
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created Testimonial: {testimonial.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Testimonial already exists: {testimonial.name}"
                    )
                )

        # Create Testimonial CTA
        testimonial_cta, created = TestimonialCTA.objects.get_or_create(
            title="Join Our Satisfied Clients",
            defaults={
                "description": "Experience professional tax consultation services trusted by businesses across Pakistan",
                "button_text": "Get Started",
                "button_link": "/contact",
                "is_testimonial_section": True,
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created TestimonialCTA: {testimonial_cta.title}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f"TestimonialCTA already exists: {testimonial_cta.title}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded all home data!"))
