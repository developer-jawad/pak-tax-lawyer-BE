from datetime import date
from django.utils.text import slugify

from django.core.management.base import BaseCommand

from blog.models import BlogCTA, BlogHero, BlogPost, BlogSection, BlogStatistic, Tag, ContentBlock
from common.constants import BLOG_CATEGORIES


class Command(BaseCommand):
    help = "Seed blog app with initial data"

    def handle(self, *args, **options):
        self.stdout.write("Seeding blog data...")

        # Create Blog Hero
        blog_hero, created = BlogHero.objects.get_or_create(
            title="Tax Insights & Expert Resources",
            defaults={
                "subtitle": "Stay informed with expert articles, practical guides, and the latest updates on Pakistani tax law and FBR compliance.",
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created BlogHero: {blog_hero.title}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"BlogHero already exists: {blog_hero.title}")
            )

        # Create Blog Statistics
        statistics_data = [
            {"number": "100+", "label": "Articles Published"},
            {"number": "15+", "label": "Expert Topics"},
            {"number": "50K+", "label": "Monthly Readers"},
            {"number": "Weekly", "label": "New Content"},
        ]

        for stat_data in statistics_data:
            statistic, created = BlogStatistic.objects.get_or_create(
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
                        f"Created BlogStatistic: {statistic.number} - {statistic.label}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"BlogStatistic already exists: {statistic.number} - {statistic.label}"
                    )
                )

        # Create Blog Section
        blog_section, created = BlogSection.objects.get_or_create(
            title="Latest Tax Blogs",
            defaults={
                "subtitle": "INSIGHTS & UPDATES",
                "description": "Stay informed with expert insights on Pakistani tax laws, FBR updates, and compliance strategies",
                "categories": BLOG_CATEGORIES.all,
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created BlogSection: {blog_section.title}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"BlogSection already exists: {blog_section.title}")
            )

        # Create Blog Posts
        blog_posts_data = [
            {
                "title": "Understanding FBR Tax Return Filing Process in Pakistan 2025",
                "excerpt": "A comprehensive guide to filing your tax returns with the Federal Board of Revenue, including deadlines, requirements, and common mistakes to avoid.",
                "author_name": "Advocate Asad Mahmood",
                "author_title": "Senior Tax Consultant & FBR Specialist",
                "author_avatar": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=150&q=80",
                "author_bio": "Advocate Asad Mahmood has over 15 years of experience in Pakistani tax law. He has represented clients before the Income Tax Appellate Tribunal and authored numerous publications on FBR compliance.",
                "date": date(2026, 5, 8),
                "read_time": "5 min read",
                "category": 1,  # Tax Filing
                "image_url": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800&q=80",
                "slug": "fbr-tax-return-filing-process-2025",
                "tags": ["FBR", "Tax Return", "IRIS", "Income Tax", "Pakistan"],
                "content": [
                    {
                        "type": "paragraph",
                        "content": "Filing your income tax return with the Federal Board of Revenue (FBR) is one of the most important financial obligations for Pakistani taxpayers. Whether you're a salaried employee, a freelancer, or a business owner, understanding the process can save you from penalties and help you claim valuable deductions."
                    },
                    {
                        "type": "heading",
                        "content": "Who Must File a Tax Return?"
                    },
                    {
                        "type": "paragraph",
                        "content": "Under the Income Tax Ordinance 2001, certain individuals are required to file tax returns regardless of whether they owe any tax. The filing obligation applies to:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Individuals whose annual income exceeds PKR 600,000",
                            "Owners of any immovable property valued over PKR 25 million",
                            "Registered motor vehicle owners (above a certain engine capacity)",
                            "Holders of professional licenses (doctors, lawyers, engineers, etc.)",
                            "Members of a chamber of commerce or professional association",
                            "All registered companies and AOPs",
                            "Individuals who received foreign income or held foreign assets"
                        ]
                    },
                    {
                        "type": "highlight",
                        "content": "💡 Pro Tip: Even if your income falls below the taxable threshold, filing a return keeps you on FBR's Active Taxpayers List (ATL), which entitles you to lower withholding tax rates on banking transactions, property sales, and vehicle purchases — saving thousands of rupees annually."
                    },
                    {
                        "type": "heading",
                        "content": "Important Deadlines for 2025"
                    },
                    {
                        "type": "paragraph",
                        "content": "Missing the tax return deadline results in penalties under Section 182 of the Income Tax Ordinance. Here are the key dates you need to mark in your calendar:"
                    },
                    {
                        "type": "ordered-list",
                        "content": [
                            "September 30, 2025 — Deadline for individual taxpayers and AOPs",
                            "December 31, 2025 — Deadline for companies with June 30 year-end",
                            "March 31, 2026 — Deadline for companies with September 30 year-end",
                            "June 30, 2026 — Deadline for companies with December 31 year-end"
                        ]
                    },
                    {
                        "type": "heading",
                        "content": "Step-by-Step Filing Process on FBR IRIS"
                    },
                    {
                        "type": "subheading",
                        "content": "Step 1: Register on IRIS"
                    },
                    {
                        "type": "paragraph",
                        "content": "If you're a first-time filer, you need to register on FBR's IRIS portal (iris.fbr.gov.pk). You'll need your CNIC number and a valid mobile phone number for the OTP verification. Once registered, your National Tax Number (NTN) is assigned automatically."
                    },
                    {
                        "type": "subheading",
                        "content": "Step 2: Complete the Income Tax Return Form"
                    },
                    {
                        "type": "paragraph",
                        "content": "Log into IRIS and navigate to \"Declaration\" > \"Income Tax Return.\" The form has multiple sections covering salary income, business income, rental income, capital gains, and foreign income. Fill each section that applies to your situation. For salaried employees, your employer should provide a tax certificate (Form-16) showing annual income and withholding."
                    },
                    {
                        "type": "subheading",
                        "content": "Step 3: Wealth Statement"
                    },
                    {
                        "type": "paragraph",
                        "content": "A wealth statement (statement of assets and liabilities) is required for individuals whose income exceeds PKR 500,000. This statement lists all your assets — property, vehicles, bank balances, investments, and business interests — along with your liabilities. The closing net worth should reconcile with your income for the year."
                    },
                    {
                        "type": "quote",
                        "content": "\"The wealth statement is equally important as the tax return itself. Unexplained increases in net worth are a major red flag for FBR and can trigger audit proceedings.\" — Advocate Asad Mahmood"
                    },
                    {
                        "type": "heading",
                        "content": "Common Mistakes to Avoid"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Forgetting to declare rental income from property you've rented out",
                            "Not including bank profit (interest/profit on savings) as income",
                            "Missing the deadline and then not requesting an extension",
                            "Incorrectly calculating business income by not separating capital and revenue expenditure",
                            "Failing to reconcile your wealth statement with your declared income",
                            "Not claiming all eligible deductions (medical, education, charitable donations)",
                            "Using incorrect income tax return form for your taxpayer category"
                        ]
                    },
                    {
                        "type": "heading",
                        "content": "Available Deductions and Tax Credits"
                    },
                    {
                        "type": "paragraph",
                        "content": "Pakistan's income tax law provides numerous deductions and credits that can significantly reduce your tax bill. Key ones include:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Education expenses: 25% credit on tuition fees up to PKR 200,000",
                            "Medical insurance premium: deductible up to PKR 150,000",
                            "Investment in Behbood Certificates or DSCs",
                            "Donations to approved charitable institutions (up to 30% of income)",
                            "Contribution to recognized provident/pension fund",
                            "Teachers'/researchers' tax credit (25% reduction)",
                            "First-time home buyer loan interest deduction"
                        ]
                    },
                    {
                        "type": "highlight",
                        "content": "⚠️ Important: Always keep supporting documentation for all deductions claimed. FBR may request proof during audit proceedings. Documents should be retained for at least 6 years from the filing date."
                    },
                    {
                        "type": "heading",
                        "content": "After Filing: What to Expect"
                    },
                    {
                        "type": "paragraph",
                        "content": "Once you submit your return, IRIS generates an acknowledgment receipt with a unique filing number. Your name appears on the Active Taxpayers List (ATL) within 24–48 hours. FBR may subsequently issue notices for clarification, additional information, or audit — usually within 5 years of filing under Section 122 of the Ordinance."
                    },
                    {
                        "type": "paragraph",
                        "content": "If you've overpaid tax through advance tax or withholding, you can claim a refund through IRIS. Refunds are typically processed within 45–60 days, though delays can occur during peak filing season."
                    }
                ],
                "related_slugs": ["tax-benefits-startups-pakistan", "become-tax-filer-guide", "tax-deductions-pakistan"]
            },
            {
                "title": "Tax Benefits for Startups and Small Businesses in Pakistan",
                "excerpt": "Discover the tax incentives, exemptions, and benefits available for new businesses and startups under Pakistani tax law.",
                "author_name": "Sadia Akhtar",
                "author_title": "Senior Tax Consultant",
                "author_avatar": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=150&q=80",
                "author_bio": "Sadia Akhtar is a Chartered Accountant with over 12 years of experience in tax consulting for startups and SMEs. She specializes in tax planning and compliance strategies for growing businesses.",
                "date": date(2026, 5, 5),
                "read_time": "7 min read",
                "category": 2,  # Business Tax
                "image_url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80",
                "slug": "tax-benefits-startups-pakistan",
                "tags": ["Startups", "Business Tax", "Tax Benefits", "SME", "Pakistan"],
                "content": [
                    {
                        "type": "paragraph",
                        "content": "Starting a new business in Pakistan comes with numerous challenges, but tax planning doesn't have to be one of them. The government has introduced various tax incentives to promote entrepreneurship and support small and medium enterprises (SMEs)."
                    },
                    {
                        "type": "heading",
                        "content": "Small Business Tax Exemptions"
                    },
                    {
                        "type": "paragraph",
                        "content": "Small businesses with annual turnover below PKR 10 million can opt for the Final Tax Regime under Section 99D of the Income Tax Ordinance 2001. Under this regime:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Fixed tax rate of 1% on turnover for certain sectors",
                            "No need to file detailed income tax returns",
                            "No wealth statement requirement",
                            "Simplified compliance procedures"
                        ]
                    },
                    {
                        "type": "highlight",
                        "content": "💡 Pro Tip: The Final Tax Regime can significantly reduce compliance costs for small businesses, but it may not always be the most tax-efficient option. Consult a tax professional to evaluate your specific situation."
                    },
                    {
                        "type": "heading",
                        "content": "Startup Tax Incentives"
                    },
                    {
                        "type": "paragraph",
                        "content": "New startups registered under the SECP may qualify for special tax benefits:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Tax holiday for IT and ITeS companies (subject to conditions)",
                            "Reduced tax rates for export-oriented businesses",
                            "Accelerated depreciation on plant and machinery",
                            "Research and development tax credits"
                        ]
                    },
                    {
                        "type": "heading",
                        "content": "Deductions Available to Businesses"
                    },
                    {
                        "type": "paragraph",
                        "content": "Businesses can claim various deductions to reduce taxable income:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Business expenses (rent, utilities, salaries, etc.)",
                            "Depreciation on fixed assets",
                            "Bad debt write-offs",
                            "Professional fees (legal, accounting, consulting)",
                            "Marketing and advertising expenses",
                            "Travel and entertainment (with proper documentation)"
                        ]
                    },
                    {
                        "type": "quote",
                        "content": "\"Proper documentation of business expenses is crucial. FBR closely scrutinizes expense claims, especially in the first few years of operation.\" — Sadia Akhtar"
                    },
                    {
                        "type": "heading",
                        "content": "Sales Tax Registration Benefits"
                    },
                    {
                        "type": "paragraph",
                        "content": "Registering for sales tax, while adding compliance requirements, offers advantages:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Input tax credit on purchases",
                            "Ability to sell to registered businesses",
                            "Enhanced business credibility",
                            "Access to government contracts"
                        ]
                    }
                ],
                "related_slugs": ["fbr-tax-return-filing-process-2025", "corporate-tax-planning-2025", "withholding-tax-pakistan"]
            },
            {
                "title": "How to Become a Tax Filer: Complete Guide for Individuals",
                "excerpt": "Step-by-step process to register as an active tax filer with FBR and enjoy the benefits of filer status in Pakistan.",
                "author_name": "Kamran Ali",
                "author_title": "Tax Compliance Specialist",
                "author_avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&q=80",
                "author_bio": "Kamran Ali specializes in individual tax compliance and FBR procedures. He has helped hundreds of individuals register as tax filers and navigate the IRIS platform.",
                "date": date(2026, 5, 2),
                "read_time": "6 min read",
                "category": 3,  # Tax Planning
                "image_url": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=800&q=80",
                "slug": "become-tax-filer-guide",
                "tags": ["Tax Filer", "FBR Registration", "NTN", "IRIS", "Individual Tax"],
                "content": [
                    {
                        "type": "paragraph",
                        "content": "Becoming an active tax filer in Pakistan is not just a legal obligation for many—it's also a smart financial decision. Tax filers enjoy numerous benefits including lower withholding tax rates and access to various government services."
                    },
                    {
                        "type": "heading",
                        "content": "Why Become a Tax Filer?"
                    },
                    {
                        "type": "paragraph",
                        "content": "The advantages of being on FBR's Active Taxpayers List (ATL) include:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Lower withholding tax on banking transactions (0.3% vs 0.6%)",
                            "Reduced property transfer tax (1% vs 2% for filers)",
                            "Lower vehicle registration tax",
                            "Access to government contracts and tenders",
                            "Better creditworthiness with financial institutions",
                            "Eligibility for various government schemes"
                        ]
                    },
                    {
                        "type": "highlight",
                        "content": "💡 Pro Tip: The tax savings from filer status alone can amount to hundreds of thousands of rupees annually for individuals with significant banking or property transactions."
                    },
                    {
                        "type": "heading",
                        "content": "Step-by-Step Registration Process"
                    },
                    {
                        "type": "subheading",
                        "content": "Step 1: Gather Required Documents"
                    },
                    {
                        "type": "paragraph",
                        "content": "Before starting the registration process, ensure you have:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Valid CNIC",
                            "Active mobile phone number for OTP verification",
                            "Email address",
                            "Proof of income (salary slip, business registration, etc.)",
                            "Bank account details"
                        ]
                    },
                    {
                        "type": "subheading",
                        "content": "Step 2: Online Registration via IRIS"
                    },
                    {
                        "type": "paragraph",
                        "content": "Visit iris.fbr.gov.pk and follow these steps:"
                    },
                    {
                        "type": "ordered-list",
                        "content": [
                            "Click on 'Unregistered Person' registration",
                            "Enter CNIC and mobile number",
                            "Verify OTP sent to your mobile",
                            "Create password and security questions",
                            "Complete profile information",
                            "Submit registration request"
                        ]
                    },
                    {
                        "type": "subheading",
                        "content": "Step 3: NTN Issuance"
                    },
                    {
                        "type": "paragraph",
                        "content": "After successful registration, your National Tax Number (NTN) will be issued. This typically takes 1-3 working days. You can check your NTN status on the FBR website using your CNIC."
                    },
                    {
                        "type": "heading",
                        "content": "Filing Your First Tax Return"
                    },
                    {
                        "type": "paragraph",
                        "content": "Once registered, you must file your first tax return to appear on the ATL:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Log into IRIS portal",
                            "Navigate to 'Declaration' section",
                            "Select 'Income Tax Return Form' applicable to your category",
                            "Fill in all required information",
                            "Submit and pay any tax due",
                            "Download acknowledgment receipt"
                        ]
                    },
                    {
                        "type": "quote",
                        "content": "\"Many individuals delay filing their first return due to complexity concerns. However, the IRIS platform has been significantly improved and now offers a user-friendly experience.\" — Kamran Ali"
                    },
                    {
                        "type": "heading",
                        "content": "Common Registration Issues"
                    },
                    {
                        "type": "paragraph",
                        "content": "If you encounter problems during registration:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Ensure your mobile number is registered in your name",
                            "Try using a different browser (Chrome recommended)",
                            "Contact FBR helpline at 111-777-777",
                            "Visit your nearest FBR facilitation center for in-person assistance"
                        ]
                    }
                ],
                "related_slugs": ["fbr-tax-return-filing-process-2025", "tax-deductions-pakistan", "nrp-tax-filing-guide"]
            },
            {
                "title": "Sales Tax Registration: Requirements and Procedures",
                "excerpt": "Everything you need to know about sales tax registration, compliance requirements, and filing obligations for businesses.",
                "author_name": "Fatima Noor",
                "author_title": "Sales Tax Consultant",
                "author_avatar": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=150&q=80",
                "author_bio": "Fatima Noor specializes in sales tax and federal excise matters. She has extensive experience helping businesses achieve sales tax compliance and handle audits.",
                "date": date(2026, 4, 28),
                "read_time": "8 min read",
                "category": 4,  # Sales Tax
                "image_url": "https://images.unsplash.com/photo-1554224154-26032ffc0d07?w=800&q=80",
                "slug": "sales-tax-registration-guide",
                "tags": ["Sales Tax", "Registration", "Compliance", "Business Tax", "FBR"],
                "content": [
                    {
                        "type": "paragraph",
                        "content": "Sales tax registration is a critical compliance requirement for many businesses in Pakistan. Understanding the registration process and ongoing obligations is essential for avoiding penalties and maintaining good standing with FBR."
                    },
                    {
                        "type": "heading",
                        "content": "Who Must Register for Sales Tax?"
                    },
                    {
                        "type": "paragraph",
                        "content": "Sales tax registration is mandatory for:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Businesses with annual turnover exceeding PKR 10 million",
                            "Manufacturers and importers (regardless of turnover)",
                            "Service providers in certain sectors",
                            "Exporters seeking input tax credit",
                            "Businesses supplying to other registered persons"
                        ]
                    },
                    {
                        "type": "highlight",
                        "content": "⚠️ Important: Voluntary registration is also available for businesses below the threshold who want to claim input tax credit or enhance their business credibility."
                    },
                    {
                        "type": "heading",
                        "content": "Registration Process"
                    },
                    {
                        "type": "subheading",
                        "content": "Online Registration"
                    },
                    {
                        "type": "paragraph",
                        "content": "The sales tax registration process is conducted online through the FBR portal:"
                    },
                    {
                        "type": "ordered-list",
                        "content": [
                            "Log into IRIS portal with your NTN credentials",
                            "Navigate to 'Registration' > 'Sales Tax Registration'",
                            "Complete the application form with business details",
                            "Upload required documents (CNIC, business registration, bank details)",
                            "Submit application for processing"
                        ]
                    },
                    {
                        "type": "subheading",
                        "content": "Required Documents"
                    },
                    {
                        "type": "paragraph",
                        "content": "Ensure you have the following documents ready:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "CNIC of proprietor/partners/directors",
                            "Business registration certificate (for companies)",
                            "Bank account details",
                            "Proof of business premises",
                            "NTN certificate",
                            "Electricity/gas bill for business address"
                        ]
                    },
                    {
                        "type": "heading",
                        "content": "Post-Registration Compliance"
                    },
                    {
                        "type": "paragraph",
                        "content": "After registration, you must comply with ongoing requirements:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "File monthly sales tax returns by the 15th of each month",
                            "Maintain proper records of all sales and purchases",
                            "Issue sales tax invoices to customers",
                            "Pay collected tax within prescribed deadlines",
                            "Respond to FBR notices and inquiries promptly"
                        ]
                    },
                    {
                        "type": "quote",
                        "content": "\"Sales tax compliance requires consistent attention. Missing a single monthly filing deadline can result in penalties and accumulated interest.\" — Fatima Noor"
                    },
                    {
                        "type": "heading",
                        "content": "Input Tax Credit"
                    },
                    {
                        "type": "paragraph",
                        "content": "One of the main benefits of sales tax registration is the ability to claim input tax credit:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Credit tax paid on purchases against tax collected on sales",
                            "Reduce overall sales tax liability",
                            "Carry forward excess credit to future periods",
                            "Claim refunds for accumulated input tax"
                        ]
                    }
                ],
                "related_slugs": ["fbr-tax-return-filing-process-2025", "withholding-tax-pakistan", "tax-benefits-startups-pakistan"]
            },
            {
                "title": "NRP Tax Guide: Filing Returns as a Non-Resident Pakistani",
                "excerpt": "Comprehensive guide for Non-Resident Pakistanis on tax obligations, property tax, and investment income in Pakistan.",
                "author_name": "Ahmed Raza",
                "author_title": "International Tax Specialist",
                "author_avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&q=80",
                "author_bio": "Ahmed Raza specializes in international taxation and NRP matters. He assists overseas Pakistanis with their tax compliance and investment planning.",
                "date": date(2026, 4, 25),
                "read_time": "9 min read",
                "category": 5,  # NRP Tax
                "image_url": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=800&q=80",
                "slug": "nrp-tax-filing-guide",
                "tags": ["NRP", "Non-Resident Pakistani", "Property Tax", "Investment Tax", "International Tax"],
                "content": [
                    {
                        "type": "paragraph",
                        "content": "Non-Resident Pakistanis (NRPs) have specific tax obligations and considerations when it comes to Pakistani tax law. Understanding these requirements is crucial for compliance and effective financial planning."
                    },
                    {
                        "type": "heading",
                        "content": "Who is a Non-Resident Pakistani?"
                    },
                    {
                        "type": "paragraph",
                        "content": "Under Pakistani tax law, you are considered a non-resident if:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "You are not present in Pakistan for more than 182 days during the tax year",
                            "You are an employee of the federal or provincial government posted abroad",
                            "You are a Pakistani citizen working abroad for a foreign employer"
                        ]
                    },
                    {
                        "type": "highlight",
                        "content": "💡 Pro Tip: Your tax residency status significantly impacts your tax liability. NRPs are generally only taxed on Pakistan-source income, while residents are taxed on worldwide income."
                    },
                    {
                        "type": "heading",
                        "content": "Tax Obligations for NRPs"
                    },
                    {
                        "type": "paragraph",
                        "content": "NRPs are required to pay tax on:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Rental income from Pakistani property",
                            "Capital gains on sale of Pakistani property",
                            "Dividend income from Pakistani companies",
                            "Interest income from Pakistani banks",
                            "Business income from Pakistani operations"
                        ]
                    },
                    {
                        "type": "heading",
                        "content": "Property Tax for NRPs"
                    },
                    {
                        "type": "subheading",
                        "content": "Withholding Tax on Property Transactions"
                    },
                    {
                        "type": "paragraph",
                        "content": "NRPs purchasing or selling property in Pakistan face withholding tax:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Filers: 1% withholding tax on property purchase",
                            "Non-filers: 2% withholding tax on property purchase",
                            "Capital gains tax applies on property sales (varies by holding period)"
                        ]
                    },
                    {
                        "type": "subheading",
                        "content": "Rental Income Taxation"
                    },
                    {
                        "type": "paragraph",
                        "content": "Rental income is taxed at progressive rates:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Up to PKR 600,000: 0%",
                            "PKR 600,001 - 1,200,000: 5%",
                            "PKR 1,200,001 - 2,400,000: 15%",
                            "PKR 2,400,001 - 3,600,000: 25%",
                            "Above PKR 3,600,000: 35%"
                        ]
                    },
                    {
                        "type": "quote",
                        "content": "\"Many NRPs are unaware that filing a tax return in Pakistan, even with zero tax liability, can save them significant withholding tax on property transactions.\" — Ahmed Raza"
                    },
                    {
                        "type": "heading",
                        "content": "Filing Tax Returns as an NRP"
                    },
                    {
                        "type": "paragraph",
                        "content": "NRPs can file tax returns online through IRIS:"
                    },
                    {
                        "type": "ordered-list",
                        "content": [
                            "Register on IRIS using CNIC and foreign mobile number",
                            "Select 'Non-Resident' status in your profile",
                            "Declare Pakistan-source income only",
                            "Claim foreign tax credits where applicable",
                            "File annual return by September 30th"
                        ]
                    },
                    {
                        "type": "heading",
                        "content": "Special Provisions for NRPs"
                    },
                    {
                        "type": "paragraph",
                        "content": "Several provisions benefit NRPs:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Foreign remittances through banking channels are tax-exempt",
                            "Special tax rates for certain foreign exchange earners",
                            "Exemptions on foreign income for specified periods",
                            "Deduction for foreign taxes paid on same income"
                        ]
                    }
                ],
                "related_slugs": ["fbr-tax-return-filing-process-2025", "become-tax-filer-guide", "tax-deductions-pakistan"]
            },
            {
                "title": "Corporate Tax Planning Strategies for 2025",
                "excerpt": "Advanced tax planning strategies for corporations to optimize tax liability while ensuring full compliance with FBR regulations.",
                "author_name": "Ayesha Malik",
                "author_title": "Corporate Tax Advisor",
                "author_avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=150&q=80",
                "author_bio": "Ayesha Malik is a corporate tax specialist with over 18 years of experience advising multinational corporations and large Pakistani businesses on tax optimization and compliance.",
                "date": date(2026, 4, 22),
                "read_time": "10 min read",
                "category": 6,  # Corporate Tax
                "image_url": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800&q=80",
                "slug": "corporate-tax-planning-2025",
                "tags": ["Corporate Tax", "Tax Planning", "Business Tax", "Tax Optimization", "FBR"],
                "content": [
                    {
                        "type": "paragraph",
                        "content": "Effective corporate tax planning is essential for businesses to minimize their tax burden while maintaining full compliance with Pakistani tax laws. Strategic planning throughout the fiscal year can result in significant tax savings."
                    },
                    {
                        "type": "heading",
                        "content": "Current Corporate Tax Rates (2025)"
                    },
                    {
                        "type": "paragraph",
                        "content": "Understanding the applicable tax rates is the foundation of tax planning:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Small companies: 29% (turnover up to PKR 250 million)",
                            "Large companies: 35% (turnover above PKR 250 million)",
                            "Banking companies: 39%",
                            "Export-oriented sectors: Special reduced rates available"
                        ]
                    },
                    {
                        "type": "highlight",
                        "content": "💡 Pro Tip: The classification as a small vs large company depends on turnover, not profit. Proper planning can help businesses stay within the small company threshold for lower tax rates."
                    },
                    {
                        "type": "heading",
                        "content": "Year-Round Tax Planning Strategies"
                    },
                    {
                        "type": "subheading",
                        "content": "Timing of Income and Expenses"
                    },
                    {
                        "type": "paragraph",
                        "content": "Strategic timing can significantly impact tax liability:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Accelerate deductible expenses into current tax year",
                            "Defer income recognition to next tax year where possible",
                            "Review year-end cutoff dates for major transactions",
                            "Consider the tax impact of bonus payments"
                        ]
                    },
                    {
                        "type": "subheading",
                        "content": "Depreciation Planning"
                    },
                    {
                        "type": "paragraph",
                        "content": "Optimize depreciation claims:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Review asset acquisition timing",
                            "Choose appropriate depreciation methods",
                            "Consider accelerated depreciation where available",
                            "Track fixed asset registers accurately"
                        ]
                    },
                    {
                        "type": "heading",
                        "content": "Industry-Specific Incentives"
                    },
                    {
                        "type": "paragraph",
                        "content": "Various sectors offer special tax incentives:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "IT/ITeS: Tax holidays and reduced rates",
                            "Export-oriented units: Special tax treatment",
                            "Manufacturing in certain zones: Tax exemptions",
                            "Green energy projects: Accelerated depreciation",
                            "Special Economic Zones: Multiple incentives"
                        ]
                    },
                    {
                        "type": "quote",
                        "content": "\"Corporate tax planning is not about evasion—it's about making smart, compliant decisions that optimize your tax position. The key is early and consistent planning throughout the year.\" — Ayesha Malik"
                    },
                    {
                        "type": "heading",
                        "content": "Group Tax Planning"
                    },
                    {
                        "type": "paragraph",
                        "content": "For corporate groups, consider:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Inter-group pricing optimization",
                            "Loss utilization across group companies",
                            "Dividend distribution planning",
                            "Restructuring for tax efficiency"
                        ]
                    },
                    {
                        "type": "heading",
                        "content": "Compliance and Documentation"
                    },
                    {
                        "type": "paragraph",
                        "content": "Proper documentation is essential for tax planning to withstand scrutiny:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Maintain transfer pricing documentation",
                            "Keep detailed records of all transactions",
                            "Document board decisions for tax-related matters",
                            "Regular tax health checks and reviews"
                        ]
                    }
                ],
                "related_slugs": ["tax-benefits-startups-pakistan", "withholding-tax-pakistan", "fbr-tax-return-filing-process-2025"]
            },
            {
                "title": "Tax Deductions You Should Know About in Pakistan",
                "excerpt": "Maximize your tax savings by understanding all available deductions and exemptions under Pakistani tax law.",
                "author_name": "Advocate Asad Mahmood",
                "author_title": "Senior Tax Consultant & FBR Specialist",
                "author_avatar": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=150&q=80",
                "author_bio": "Advocate Asad Mahmood has over 15 years of experience in Pakistani tax law. He has represented clients before the Income Tax Appellate Tribunal and authored numerous publications on FBR compliance.",
                "date": date(2026, 4, 18),
                "read_time": "6 min read",
                "category": 3,  # Tax Planning
                "image_url": "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=800&q=80",
                "slug": "tax-deductions-pakistan",
                "tags": ["Tax Deductions", "Tax Savings", "Income Tax", "Tax Credits", "Pakistan"],
                "content": [
                    {
                        "type": "paragraph",
                        "content": "Understanding available tax deductions is crucial for minimizing your tax liability legally. Pakistani tax law provides numerous deductions that individuals and businesses can claim to reduce their taxable income."
                    },
                    {
                        "type": "heading",
                        "content": "Individual Tax Deductions"
                    },
                    {
                        "type": "subheading",
                        "content": "Education Expenses"
                    },
                    {
                        "type": "paragraph",
                        "content": "Tax credits are available for education:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "25% credit on tuition fees up to PKR 200,000",
                            "Applies to education at recognized institutions",
                            "Includes fees for children's education",
                            "Requires fee receipts as documentation"
                        ]
                    },
                    {
                        "type": "subheading",
                        "content": "Medical Expenses"
                    },
                    {
                        "type": "paragraph",
                        "content": "Health-related deductions include:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Medical insurance premium deduction up to PKR 150,000",
                            "Medical expenses for self and family",
                            "Health insurance contributions to approved schemes",
                            "Requires proper medical receipts and certificates"
                        ]
                    },
                    {
                        "type": "subheading",
                        "content": "Charitable Donations"
                    },
                    {
                        "type": "paragraph",
                        "content": "Donations to approved organizations are deductible:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Up to 30% of taxable income can be donated",
                            "Must be to FBR-approved charitable institutions",
                            "Requires donation certificates",
                            "Includes donations to hospitals, schools, and NGOs"
                        ]
                    },
                    {
                        "type": "highlight",
                        "content": "💡 Pro Tip: Keep all donation receipts organized. FBR may request proof during audit proceedings, and without proper documentation, deductions may be disallowed."
                    },
                    {
                        "type": "heading",
                        "content": "Business Deductions"
                    },
                    {
                        "type": "paragraph",
                        "content": "Businesses can claim various operating expenses:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Salaries and wages of employees",
                            "Rent and utilities for business premises",
                            "Professional fees (legal, accounting, consulting)",
                            "Marketing and advertising expenses",
                            "Travel and entertainment (with proper documentation)",
                            "Depreciation on fixed assets",
                            "Bad debt write-offs"
                        ]
                    },
                    {
                        "type": "heading",
                        "content": "Special Tax Credits"
                    },
                    {
                        "type": "paragraph",
                        "content": "Additional tax benefits for specific categories:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Teachers and researchers: 25% tax credit",
                            "Senior citizens: Additional exemptions",
                            "Persons with disabilities: Special deductions",
                            "First-time homebuyers: Interest deduction",
                            "Investment in government securities: Tax-exempt income"
                        ]
                    },
                    {
                        "type": "quote",
                        "content": "\"Many taxpayers fail to claim all eligible deductions simply because they're unaware of them. Professional tax planning can help identify and maximize all available deductions.\" — Advocate Asad Mahmood"
                    },
                    {
                        "type": "heading",
                        "content": "Documentation Requirements"
                    },
                    {
                        "type": "paragraph",
                        "content": "To claim deductions successfully:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Maintain proper receipts and invoices",
                            "Keep records for at least 6 years",
                            "Organize documents by category",
                            "Use digital record-keeping where possible",
                            "Obtain certificates for charitable donations"
                        ]
                    }
                ],
                "related_slugs": ["fbr-tax-return-filing-process-2025", "become-tax-filer-guide", "tax-benefits-startups-pakistan"]
            },
            {
                "title": "Understanding Withholding Tax in Pakistan",
                "excerpt": "Complete guide to withholding tax obligations, rates, and compliance requirements for businesses and individuals.",
                "author_name": "Sadia Akhtar",
                "author_title": "Senior Tax Consultant",
                "author_avatar": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=150&q=80",
                "author_bio": "Sadia Akhtar is a Chartered Accountant with over 12 years of experience in tax consulting for startups and SMEs. She specializes in tax planning and compliance strategies for growing businesses.",
                "date": date(2026, 4, 15),
                "read_time": "7 min read",
                "category": 2,  # Business Tax
                "image_url": "https://images.unsplash.com/photo-1554224154-26032ffc0d07?w=800&q=80",
                "slug": "withholding-tax-pakistan",
                "tags": ["Withholding Tax", "Tax Compliance", "Business Tax", "FBR", "Pakistan"],
                "content": [
                    {
                        "type": "paragraph",
                        "content": "Withholding tax is one of the most common forms of tax collection in Pakistan. It's deducted at source by various entities and can significantly impact your cash flow if not properly managed."
                    },
                    {
                        "type": "heading",
                        "content": "What is Withholding Tax?"
                    },
                    {
                        "type": "paragraph",
                        "content": "Withholding tax is an amount deducted by a payer before making payment to the payee. It's essentially a tax collected at source and then deposited with FBR by the withholding agent."
                    },
                    {
                        "type": "heading",
                        "content": "Common Withholding Tax Scenarios"
                    },
                    {
                        "type": "subheading",
                        "content": "Banking Transactions"
                    },
                    {
                        "type": "paragraph",
                        "content": "Cash withdrawals and transactions attract withholding tax:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Filers: 0.3% on cash withdrawals above PKR 50,000",
                            "Non-filers: 0.6% on cash withdrawals above PKR 50,000",
                            "Non-filers: Higher rates on banking transactions"
                        ]
                    },
                    {
                        "type": "subheading",
                        "content": "Property Transactions"
                    },
                    {
                        "type": "paragraph",
                        "content": "Property purchase and sale involve withholding tax:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Property purchase: 1% for filers, 2% for non-filers",
                            "Property sale: Capital gains tax varies by holding period",
                            "Immovable property: Different rates for filers vs non-filers"
                        ]
                    },
                    {
                        "type": "subheading",
                        "content": "Salary Withholding"
                    },
                    {
                        "type": "paragraph",
                        "content": "Employers withhold tax on salaries:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Progressive rates based on annual salary",
                            "Employers must issue Form-16 to employees",
                            "Withheld tax can be claimed as credit in annual return"
                        ]
                    },
                    {
                        "type": "highlight",
                        "content": "💡 Pro Tip: Being a filer significantly reduces withholding tax rates across all categories. The tax savings alone often justify the effort of filing annual returns."
                    },
                    {
                        "type": "heading",
                        "content": "Claiming Withholding Tax Credit"
                    },
                    {
                        "type": "paragraph",
                        "content": "Tax withheld can be claimed as credit:"
                    },
                    {
                        "type": "ordered-list",
                        "content": [
                            "Ensure withholding agent deposits tax with FBR",
                            "Obtain withholding tax certificates",
                            "Declare withheld tax in your annual return",
                            "Claim credit against your tax liability",
                            "Claim refund if tax paid exceeds liability"
                        ]
                    },
                    {
                        "type": "heading",
                        "content": "Business Withholding Obligations"
                    },
                    {
                        "type": "paragraph",
                        "content": "Businesses must withhold tax on:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Payments to suppliers (above threshold)",
                            "Professional fees paid",
                            "Contract payments",
                            "Dividends distributed",
                            "Rent payments to non-filers"
                        ]
                    },
                    {
                        "type": "quote",
                        "content": "\"Businesses must be careful to properly classify payments and apply correct withholding rates. Failure to withhold or deposit tax can result in penalties and interest.\" — Sadia Akhtar"
                    },
                    {
                        "type": "heading",
                        "content": "Compliance Requirements"
                    },
                    {
                        "type": "paragraph",
                        "content": "To ensure proper withholding tax compliance:"
                    },
                    {
                        "type": "list",
                        "content": [
                            "Verify filer status of payees before payment",
                            "Apply correct withholding rates",
                            "Deposit withheld tax by the 15th of following month",
                            "File monthly withholding statements",
                            "Maintain proper records for at least 6 years"
                        ]
                    }
                ],
                "related_slugs": ["fbr-tax-return-filing-process-2025", "tax-benefits-startups-pakistan", "corporate-tax-planning-2025"]
            }
        ]

        # First, create all blog posts without relations
        blog_posts = {}
        for post_data in blog_posts_data:
            # Extract tags, content, and related_slugs for later
            tags_data = post_data.pop("tags", [])
            content_data = post_data.pop("content", [])
            related_slugs = post_data.pop("related_slugs", [])
            
            blog_post, created = BlogPost.objects.get_or_create(
                slug=post_data["slug"],
                defaults={
                    **post_data,
                    "is_active": True,
                    "is_deleted": False,
                },
            )
            blog_posts[blog_post.slug] = {
                "post": blog_post,
                "tags": tags_data,
                "content": content_data,
                "related_slugs": related_slugs,
            }
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created BlogPost: {blog_post.title}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"BlogPost already exists: {blog_post.title}")
                )
        
        # Create Tag objects
        all_tags = set()
        for slug, data in blog_posts.items():
            all_tags.update(data["tags"])
        
        for tag_name in all_tags:
            tag_slug = slugify(tag_name)
            Tag.objects.get_or_create(
                slug=tag_slug,
                defaults={
                    "name": tag_name,
                    "is_active": True,
                    "is_deleted": False,
                }
            )
        
        # Create ContentBlock objects and link tags and content to posts
        for slug, data in blog_posts.items():
            post = data["post"]
            
            # Link tags
            for tag_name in data["tags"]:
                tag_slug = slugify(tag_name)
                tag = Tag.objects.get(slug=tag_slug)
                post.tags.add(tag)
            
            # Create and link content blocks
            for idx, content_item in enumerate(data["content"]):
                content_type = content_item.get("type", "paragraph")
                content = content_item.get("content")
                
                content_block = ContentBlock.objects.create(
                    content_type=content_type,
                    content=content,
                    order=idx,
                    is_active=True,
                    is_deleted=False,
                )
                post.content_blocks.add(content_block)
        
        # Link related posts
        for slug, data in blog_posts.items():
            post = data["post"]
            for related_slug in data["related_slugs"]:
                if related_slug in blog_posts:
                    related_post = blog_posts[related_slug]["post"]
                    post.related_posts.add(related_post)

        # Create Blog CTA
        blog_cta, created = BlogCTA.objects.get_or_create(
            button_text="View All Blogs",
            defaults={
                "button_link": "/blogs",
                "is_blog_section": True,
                "is_active": True,
                "is_deleted": False,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created BlogCTA: {blog_cta.button_text}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"BlogCTA already exists: {blog_cta.button_text}")
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded all blog data!"))
