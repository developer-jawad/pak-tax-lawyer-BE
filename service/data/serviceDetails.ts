export interface IProcessStep {
  step: number;
  title: string;
  description: string;
  icon: string;
}

export interface IFaqItem {
  question: string;
  answer: string;
}

export interface IServiceDetailBenefit {
  icon: string;
  title: string;
  description: string;
}

export interface IServiceDetail {
  slug: string;
  title: string;
  icon: string;
  color: string;
  tagline: string;
  overview: string[];
  requirements: string[];
  process: IProcessStep[];
  benefits: IServiceDetailBenefit[];
  faqs: IFaqItem[];
  relatedSlugs: string[];
  image: string;
  badge?: string;
}

const SERVICE_DETAILS: IServiceDetail[] = [
  {
    slug: 'tax-return-filing',
    title: 'Tax Return Filing',
    icon: 'Description',
    color: '#EE1C27',
    tagline: 'File your taxes accurately and on time — every time.',
    image:
      'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=1200&q=80',
    overview: [
      "Filing income tax returns in Pakistan is a legal obligation for every earning individual and business entity. Whether you're a salaried professional, a self-employed consultant, or a business owner, the Federal Board of Revenue (FBR) requires timely and accurate tax return submissions.",
      "Our expert team handles every step of the process — from gathering your income details to submitting the final return on IRIS, the FBR's e-filing portal. We ensure all available deductions and credits are applied to minimize your tax liability while keeping you fully compliant.",
      'With over 15 years of experience, we have successfully filed thousands of returns for clients across all sectors, including salaried employees, freelancers, small businesses, and high-net-worth individuals.',
    ],
    requirements: [
      'CNIC / Passport copy',
      'Salary slips or bank statements',
      'Property ownership documents (if applicable)',
      'Business income records',
      'Foreign income details for NRPs',
      'Investment and savings certificates',
      'Previous year tax return (if applicable)',
    ],
    process: [
      {
        step: 1,
        title: 'Initial Consultation',
        description:
          'We begin with a free consultation to understand your income sources, assets, and tax history.',
        icon: 'Chat',
      },
      {
        step: 2,
        title: 'Document Collection',
        description:
          'We guide you in collecting all required documents and financial records securely.',
        icon: 'FolderOpen',
      },
      {
        step: 3,
        title: 'Tax Computation',
        description:
          'Our experts calculate your taxable income, applicable deductions, and total tax liability.',
        icon: 'Calculate',
      },
      {
        step: 4,
        title: 'Return Preparation',
        description:
          'We prepare your return in FBR-compliant format, applying all eligible exemptions and credits.',
        icon: 'Article',
      },
      {
        step: 5,
        title: 'E-Filing & Confirmation',
        description:
          'Your return is filed on IRIS and you receive an official acknowledgment receipt.',
        icon: 'CheckCircle',
      },
    ],
    benefits: [
      {
        icon: 'Speed',
        title: 'Fast Turnaround',
        description:
          'Most returns are filed within 48–72 hours of receiving all documents.',
      },
      {
        icon: 'Security',
        title: 'Fully Compliant',
        description:
          'Every return adheres to the latest FBR guidelines and Income Tax Ordinance.',
      },
      {
        icon: 'TrendingDown',
        title: 'Maximize Deductions',
        description:
          'We identify every legal deduction to reduce your overall tax burden.',
      },
      {
        icon: 'Support',
        title: 'Year-Round Support',
        description:
          'Post-filing support for notices, amendments, and FBR queries included.',
      },
    ],
    faqs: [
      {
        question: 'Who is required to file an income tax return in Pakistan?',
        answer:
          'Every individual whose annual income exceeds the taxable threshold (PKR 600,000 for the tax year 2024–25) must file a tax return. Additionally, owners of immovable property, motor vehicle owners, and holders of professional licenses must file regardless of income level.',
      },
      {
        question: 'What is the deadline for filing tax returns in Pakistan?',
        answer:
          'The standard deadline for individual tax returns is September 30 each year for the previous tax year (July–June). For companies, the deadline is December 31. Extensions can be requested from the FBR Commissioner.',
      },
      {
        question: 'What happens if I miss the tax return filing deadline?',
        answer:
          'Late filing attracts penalties under Section 182 of the Income Tax Ordinance 2001. The penalty is PKR 2,500 per month for individuals and higher amounts for companies. It also affects your filer status, resulting in higher withholding tax rates.',
      },
      {
        question:
          'Can I file my own tax return without a consultant?',
        answer:
          'Yes, individuals can self-file through FBR\'s IRIS portal. However, consulting a professional ensures accuracy, maximizes deductions, and minimizes the risk of notices or penalties — which ultimately saves more than the consultation fee.',
      },
      {
        question: 'How do I know if my tax return has been accepted?',
        answer:
          'Upon successful submission, FBR IRIS generates an acknowledgment receipt with a unique tracking number. Your filing status also becomes visible on the FBR Active Taxpayers List (ATL) within 24 hours.',
      },
    ],
    relatedSlugs: [
      'fbr-compliance',
      'tax-planning',
      'personal-tax-advisory',
    ],
  },
  {
    slug: 'fbr-compliance',
    title: 'FBR Compliance',
    icon: 'AccountBalance',
    color: '#000000',
    tagline:
      'Stay fully compliant with FBR regulations — registrations to filings.',
    image:
      'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&q=80',
    overview: [
      "The Federal Board of Revenue (FBR) manages Pakistan's tax system through a complex regulatory framework. Non-compliance can result in heavy penalties, business disruptions, and legal action. Our FBR compliance services cover every registration and filing obligation your business may have.",
      'Whether you need an NTN, STRN, or guidance on monthly/quarterly filing obligations, our team handles the entire process end-to-end. We stay up-to-date with every FBR notification and regulatory change to keep you ahead of the curve.',
      'From new business registrations to handling compliance audits, we act as your dedicated compliance partner — ensuring your relationship with FBR is always in good standing.',
    ],
    requirements: [
      'CNIC / Company registration documents',
      'Business address and lease agreement',
      'Bank account details',
      'Nature of business description',
      'Existing NTN/STRN (for amendments)',
      'Utility bills for business address',
    ],
    process: [
      {
        step: 1,
        title: 'Compliance Audit',
        description:
          "We assess your current compliance status and identify any gaps or pending obligations.",
        icon: 'Search',
      },
      {
        step: 2,
        title: 'Registration',
        description:
          "We handle NTN, STRN, and all FBR registrations through IRIS on your behalf.",
        icon: 'AppRegistration',
      },
      {
        step: 3,
        title: 'Filing Calendar Setup',
        description:
          'We set up a compliance calendar for all your periodic filing deadlines.',
        icon: 'CalendarMonth',
      },
      {
        step: 4,
        title: 'Ongoing Filings',
        description:
          'Monthly sales tax returns, withholding statements, and income tax returns are filed timely.',
        icon: 'UploadFile',
      },
      {
        step: 5,
        title: 'Notice Management',
        description:
          'Any FBR notices or audit queries are handled promptly by our legal team.',
        icon: 'MarkEmailRead',
      },
    ],
    benefits: [
      {
        icon: 'VerifiedUser',
        title: 'Zero Penalty Risk',
        description:
          'Timely filings ensure you never face late penalty charges from FBR.',
      },
      {
        icon: 'Business',
        title: 'Business Continuity',
        description:
          'Maintaining compliance protects your business from suspension or blacklisting.',
      },
      {
        icon: 'AccountBalance',
        title: 'Government Tenders',
        description:
          'Filer status is required for government contracts and regulatory approvals.',
      },
      {
        icon: 'NotificationsActive',
        title: 'Proactive Alerts',
        description:
          'We notify you of regulatory changes and upcoming FBR deadlines in advance.',
      },
    ],
    faqs: [
      {
        question: 'What is an NTN and who needs it?',
        answer:
          "A National Tax Number (NTN) is a unique identifier assigned by FBR to taxpayers. Every individual, company, or association of persons engaged in business or profession must obtain an NTN. It is also required for opening a business bank account, importing/exporting goods, and participating in government tenders.",
      },
      {
        question: 'What is STRN and when is it required?',
        answer:
          'A Sales Tax Registration Number (STRN) is required for businesses that are registered persons under the Sales Tax Act 1990. If your taxable supplies exceed the exemption threshold, you must register for sales tax and file monthly returns.',
      },
      {
        question:
          'How often do I need to file FBR returns as a registered business?',
        answer:
          'Registered sales taxpayers file monthly sales tax returns by the 15th of the following month. Withholding agents file monthly statements by the 15th. Annual income tax returns are due by December 31 for companies and September 30 for individuals.',
      },
      {
        question: 'What happens if my business is blacklisted by FBR?',
        answer:
          'Blacklisting prevents you from claiming input tax credit on purchases, severely impacting your business. We can help rectify the compliance issues, file required returns, and apply for removal from the blacklist with supporting documentation.',
      },
    ],
    relatedSlugs: ['tax-return-filing', 'corporate-tax-services', 'tax-planning'],
  },
  {
    slug: 'tax-planning',
    title: 'Tax Planning',
    icon: 'Assessment',
    color: '#EE1C27',
    tagline: 'Plan strategically today to save significantly tomorrow.',
    image:
      'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80',
    overview: [
      'Tax planning is the art of legally minimizing your tax liability through strategic financial decisions made throughout the year — not just at year-end. Our proactive approach helps individuals and businesses structure their finances to reduce their tax burden while remaining fully compliant.',
      'We analyze your income streams, investments, business structure, and expenses to identify legitimate tax-saving opportunities. From investment allowances and depreciation strategies to timing of income and deductions, every element is optimized.',
      "Whether you're an individual seeking to maximize savings from salary, rental income, and investments, or a business looking to optimize corporate structure and transfer pricing — our tailored planning strategies deliver measurable results.",
    ],
    requirements: [
      'Current year income details',
      'Investment portfolio summary',
      'Business financial statements',
      'Property and asset details',
      'Previous year tax returns',
      'Future income/investment plans',
    ],
    process: [
      {
        step: 1,
        title: 'Financial Review',
        description:
          'We comprehensively review your current financial position and income sources.',
        icon: 'Analytics',
      },
      {
        step: 2,
        title: 'Tax Gap Analysis',
        description:
          'We identify areas where you may be overpaying or missing tax-saving opportunities.',
        icon: 'FindInPage',
      },
      {
        step: 3,
        title: 'Strategy Development',
        description:
          'A customized tax optimization plan is developed based on your financial goals.',
        icon: 'Lightbulb',
      },
      {
        step: 4,
        title: 'Implementation',
        description:
          'We guide you through executing the strategy, including restructuring and timing decisions.',
        icon: 'PlayArrow',
      },
      {
        step: 5,
        title: 'Monitoring & Review',
        description:
          'Regular check-ins throughout the year to adjust the plan as your circumstances change.',
        icon: 'Loop',
      },
    ],
    benefits: [
      {
        icon: 'Savings',
        title: 'Maximize Savings',
        description:
          'Legally reduce your tax liability by leveraging all available deductions and credits.',
      },
      {
        icon: 'Timeline',
        title: 'Long-term Strategy',
        description:
          'We plan across multiple years to align tax efficiency with your financial goals.',
      },
      {
        icon: 'Balance',
        title: 'Risk Management',
        description:
          'Avoid aggressive strategies that could trigger FBR scrutiny while maximizing benefits.',
      },
      {
        icon: 'Groups',
        title: 'Family Tax Planning',
        description:
          'Optimize the overall tax position of family-owned businesses and joint assets.',
      },
    ],
    faqs: [
      {
        question: 'What is the difference between tax planning and tax evasion?',
        answer:
          "Tax planning involves legally minimizing your tax liability using provisions within the tax law — such as deductions, exemptions, and tax credits. Tax evasion, on the other hand, involves illegally concealing income or falsifying records. All our strategies are strictly within the bounds of Pakistan's Income Tax Ordinance 2001.",
      },
      {
        question: 'What are some common tax-saving options for individuals in Pakistan?',
        answer:
          'Key deductions include: investment in Behbood Saving Certificates, National Savings Schemes, and approved pension funds; donations to approved charitable organizations; education expenses; medical expenses and health insurance; and contributions to approved provident funds.',
      },
      {
        question: 'Can a business reduce its tax through corporate restructuring?',
        answer:
          'Yes, choosing the right corporate structure (sole proprietorship vs. partnership vs. private limited company) can significantly impact the effective tax rate. Additionally, inter-company pricing, holding company structures, and investment in priority sectors with tax incentives can reduce overall corporate tax.',
      },
      {
        question: 'How early should I start tax planning for the year?',
        answer:
          'The earlier the better. Ideally, planning should begin at the start of the tax year (July 1) so you can make optimal financial decisions throughout the year. Last-minute planning limits your options. We offer year-round retainer packages for ongoing tax advisory.',
      },
    ],
    relatedSlugs: ['tax-return-filing', 'corporate-tax-services', 'personal-tax-advisory'],
  },
  {
    slug: 'tax-litigation',
    title: 'Tax Litigation',
    icon: 'Gavel',
    color: '#000000',
    tagline: 'Expert legal defense in tax disputes, appeals, and court proceedings.',
    image:
      'https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1200&q=80',
    overview: [
      "Tax disputes with FBR can be stressful, time-consuming, and financially damaging if not handled properly. Our experienced tax litigation team represents clients at every level — from departmental proceedings to the Income Tax Appellate Tribunal (ITAT) and Superior Courts.",
      'We specialize in challenging illegal assessments, unlawful attachments, excessive penalties, and wrongful recoveries. Our attorneys combine deep knowledge of tax law with extensive courtroom experience to build strong cases for our clients.',
      'From the moment you receive an FBR notice to the final resolution, we take full ownership of your case — preparing arguments, submitting evidence, attending hearings, and negotiating settlements where appropriate.',
    ],
    requirements: [
      'FBR notice or assessment order',
      'Previous correspondence with FBR',
      'Tax returns for relevant years',
      'Business/financial records',
      'Any prior proceedings documentation',
      'Bank statements and transaction records',
    ],
    process: [
      {
        step: 1,
        title: 'Notice Analysis',
        description:
          'We carefully review the FBR notice or assessment order to identify legal and factual grounds for challenge.',
        icon: 'Search',
      },
      {
        step: 2,
        title: 'Legal Strategy',
        description:
          'Our attorneys develop a comprehensive legal strategy tailored to your specific case.',
        icon: 'AccountTree',
      },
      {
        step: 3,
        title: 'Response Filing',
        description:
          'Detailed written responses and supporting documentation are filed within statutory deadlines.',
        icon: 'Send',
      },
      {
        step: 4,
        title: 'Hearings & Representation',
        description:
          'We appear on your behalf at all departmental hearings, ITAT, and court proceedings.',
        icon: 'RecordVoiceOver',
      },
      {
        step: 5,
        title: 'Resolution',
        description:
          'We pursue the most favorable outcome — whether through a court order, settlement, or appeal.',
        icon: 'EmojiEvents',
      },
    ],
    benefits: [
      {
        icon: 'Gavel',
        title: 'Experienced Advocates',
        description:
          'Our team includes senior advocates with decades of tax litigation experience.',
      },
      {
        icon: 'Shield',
        title: 'Asset Protection',
        description:
          'We act swiftly to prevent unlawful attachment or freezing of your assets.',
      },
      {
        icon: 'Grading',
        title: 'Strong Track Record',
        description:
          'We have successfully overturned hundreds of arbitrary assessments and penalties.',
      },
      {
        icon: 'Handshake',
        title: 'Settlement Expertise',
        description:
          'When favorable, we negotiate settlements that save time and cost while protecting your interests.',
      },
    ],
    faqs: [
      {
        question: 'What should I do if I receive a tax notice from FBR?',
        answer:
          'Do not ignore it. FBR notices have strict response deadlines. Contact us immediately — even if you believe the notice is incorrect. We will analyze the notice, advise on your rights, and prepare the appropriate response within the required timeframe.',
      },
      {
        question: 'What is the appeal process for a tax assessment in Pakistan?',
        answer:
          'The appeal process follows this hierarchy: (1) Commissioner Inland Revenue (Appeals) [CIR(A)], (2) Income Tax Appellate Tribunal (ITAT), (3) High Court on questions of law, (4) Supreme Court. Each level has specific timelines and procedural requirements.',
      },
      {
        question: 'Can FBR freeze my bank accounts?',
        answer:
          'Yes, FBR has powers under the Income Tax Ordinance 2001 to attach and sell property, and to issue recovery notices to banks. However, such actions can be challenged if procedural requirements were not followed. We can apply for stay orders to immediately halt such actions.',
      },
      {
        question: 'How long does tax litigation typically take?',
        answer:
          'Timeline varies significantly. A departmental appeal to CIR(A) may take 3–12 months. ITAT proceedings can take 1–3 years. Higher court matters may take several years. We always pursue the fastest resolution that protects your interests.',
      },
    ],
    relatedSlugs: ['fbr-compliance', 'corporate-tax-services', 'tax-return-filing'],
  },
  {
    slug: 'corporate-tax-services',
    title: 'Corporate Tax Services',
    icon: 'Business',
    color: '#EE1C27',
    tagline:
      'End-to-end tax solutions for businesses of every size and structure.',
    image:
      'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=1200&q=80',
    overview: [
      'Corporate taxation in Pakistan involves multiple layers of compliance — from monthly withholding obligations to annual corporate returns, from advance tax payments to transfer pricing documentation. Our corporate tax practice covers every aspect of your business tax needs.',
      'We work with private limited companies, public companies, partnerships, and multinational corporations operating in Pakistan. Our team stays current with every Finance Act amendment and FBR SRO to ensure your business benefits from all available incentives.',
      'Beyond compliance, we provide strategic advisory services including corporate structure optimization, M&A tax due diligence, and cross-border tax planning for businesses with international operations.',
    ],
    requirements: [
      'Company incorporation documents',
      'Audited financial statements',
      'Trial balance and ledger accounts',
      'Withholding tax deduction registers',
      'Employee payroll records',
      'Import/export records (if applicable)',
      'Related party transactions summary',
    ],
    process: [
      {
        step: 1,
        title: 'Tax Health Check',
        description:
          'Comprehensive review of your existing tax compliance status and identifying any exposures.',
        icon: 'HealthAndSafety',
      },
      {
        step: 2,
        title: 'Compliance Structuring',
        description:
          'Setting up systems and processes for ongoing tax compliance across all obligations.',
        icon: 'AccountTree',
      },
      {
        step: 3,
        title: 'Withholding Management',
        description:
          'Ensuring all withholding obligations on payments to employees, vendors, and others are met.',
        icon: 'Receipt',
      },
      {
        step: 4,
        title: 'Advance Tax Planning',
        description:
          'Managing quarterly advance tax payments to avoid underpayment penalties.',
        icon: 'Payments',
      },
      {
        step: 5,
        title: 'Annual Return Filing',
        description:
          'Preparation and filing of corporate income tax return with full supporting documentation.',
        icon: 'AssignmentTurnedIn',
      },
    ],
    benefits: [
      {
        icon: 'CorporateFare',
        title: 'Full Cycle Management',
        description:
          'From incorporation to annual returns — we manage your entire tax compliance calendar.',
      },
      {
        icon: 'TrendingDown',
        title: 'Tax Optimization',
        description:
          'We leverage applicable tax incentives, SEZ benefits, and IT company reliefs.',
      },
      {
        icon: 'IntegrationInstructions',
        title: 'ERP Integration',
        description:
          'We integrate with your accounting systems to streamline withholding and filing workflows.',
      },
      {
        icon: 'BarChart',
        title: 'Tax Reporting',
        description:
          'Detailed tax position reports and effective tax rate analysis for management boards.',
      },
    ],
    faqs: [
      {
        question: 'What is the corporate income tax rate in Pakistan?',
        answer:
          'The standard corporate income tax rate for companies is 29% (for tax year 2024–25). Banking companies are taxed at 39%. Small companies (turnover up to PKR 250 million, meeting specific conditions) are taxed at 20%. Special economic zone companies and IT companies may qualify for significantly reduced rates.',
      },
      {
        question: 'What are withholding tax obligations for businesses?',
        answer:
          'Businesses must deduct withholding tax on salaries (as per tax slabs), payments to contractors (7.5%), rent (15%), dividends (15%), and many other payment types. These deductions must be deposited with FBR and monthly statements filed by the 15th of the following month.',
      },
      {
        question: "What are Pakistan's transfer pricing rules?",
        answer:
          "Pakistan's transfer pricing rules require related-party transactions to be conducted at arm's length prices. Section 108 of the Income Tax Ordinance 2001 and the Transfer Pricing Rules 2012 govern these transactions. Non-compliance can result in deemed income adjustments and penalties.",
      },
      {
        question: 'Does a newly formed company need to pay advance tax?',
        answer:
          'Companies are required to pay quarterly advance tax installments if their tax liability exceeds PKR 500,000 in the previous year. New companies in their first year may not be required to pay advance tax if they have no prior year tax. We help forecast and plan advance tax payments accurately.',
      },
    ],
    relatedSlugs: ['fbr-compliance', 'tax-planning', 'tax-litigation'],
  },
  {
    slug: 'personal-tax-advisory',
    title: 'Personal Tax Advisory',
    icon: 'PersonOutline',
    color: '#000000',
    tagline: 'Bespoke tax guidance tailored to your personal financial journey.',
    image:
      'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=1200&q=80',
    overview: [
      'High-income individuals, professionals, business owners, and Non-Resident Pakistanis (NRPs) face complex personal tax scenarios that require specialized expertise. Our personal tax advisory service provides dedicated guidance tailored to your unique financial profile.',
      'We help you navigate wealth management decisions from a tax perspective — including property transactions, capital gains, foreign income, inheritance, and gift planning. Every recommendation is grounded in the current Income Tax Ordinance and applicable case law.',
      'Our advisors work discreetly and confidentially, understanding the sensitivity of personal financial matters while delivering proactive strategies that protect and grow your wealth over time.',
    ],
    requirements: [
      'Personal income details (all sources)',
      'Property ownership and rental income records',
      'Investment portfolio details',
      'Foreign assets and income (for NRPs)',
      'Bank and savings account statements',
      'Business ownership interests',
      'Gift and inheritance documentation',
    ],
    process: [
      {
        step: 1,
        title: 'Wealth Profile Assessment',
        description:
          'We map your complete financial picture — income, assets, liabilities, and tax history.',
        icon: 'AccountCircle',
      },
      {
        step: 2,
        title: 'Tax Exposure Review',
        description:
          'We identify any current or potential tax risks in your personal portfolio.',
        icon: 'Policy',
      },
      {
        step: 3,
        title: 'Personalized Strategy',
        description:
          'A bespoke tax strategy is crafted aligning with your lifestyle and financial goals.',
        icon: 'Star',
      },
      {
        step: 4,
        title: 'Execution Support',
        description:
          'We assist with property transactions, investment decisions, and documentation from a tax angle.',
        icon: 'Handyman',
      },
      {
        step: 5,
        title: 'Annual Review',
        description:
          'Yearly comprehensive review to adjust strategy based on changes in income, assets, or law.',
        icon: 'Autorenew',
      },
    ],
    benefits: [
      {
        icon: 'Person',
        title: 'Dedicated Advisor',
        description:
          'A single point of contact who understands your entire financial picture year-round.',
      },
      {
        icon: 'Lock',
        title: 'Complete Confidentiality',
        description:
          'All personal financial information is handled with the utmost discretion and security.',
      },
      {
        icon: 'HomeWork',
        title: 'Property Tax Expertise',
        description:
          'Expert guidance on CGT, deemed rent, and property tax for residential and commercial assets.',
      },
      {
        icon: 'Public',
        title: 'NRP Specialization',
        description:
          'Specialized services for overseas Pakistanis managing assets and income in Pakistan.',
      },
    ],
    faqs: [
      {
        question: 'How are capital gains on property taxed in Pakistan?',
        answer:
          'Capital gains tax (CGT) applies to gains from disposal of immovable property. For properties held less than 1 year, CGT is 15%. For 1–2 years, it is 12.5%. For 2–3 years, it is 10%. For 3–4 years, it is 7.5%. For 4–5 years, it is 5%. For 5–6 years, it is 2.5%. No CGT applies after 6 years of holding.',
      },
      {
        question: 'How is rental income taxed in Pakistan?',
        answer:
          "Rental income is subject to income tax. For individuals, rental income up to PKR 300,000 annually is exempt. Beyond this, it is taxed at graduated rates. Additionally, if property is held but not rented, FBR may deem 5% of the fair market value as imputed rent under Section 155 of the Income Tax Ordinance.",
      },
      {
        question: 'What are the tax implications of receiving gifts or inheritance?',
        answer:
          'Under the current tax law, gifts received from non-relatives are taxable as income. Gifts from blood relatives (parents, siblings, children, and spouse) are generally exempt. Inheritance is not subject to income tax in Pakistan (estate/inheritance tax was abolished). However, the recipient may need to disclose inherited assets in their wealth statement.',
      },
      {
        question:
          'As an overseas Pakistani, am I required to file tax returns in Pakistan?',
        answer:
          'Non-Resident Pakistanis are generally only taxed on Pakistan-source income. However, if you own immovable property, a business, or have investments in Pakistan, you may have filing obligations. NRPs who wish to remit funds or make property transactions also benefit significantly from maintaining active filer status.',
      },
    ],
    relatedSlugs: ['tax-return-filing', 'tax-planning', 'fbr-compliance'],
  },
];

export const getServiceBySlug = (slug: string): IServiceDetail | undefined => {
  return SERVICE_DETAILS.find(s => s.slug === slug);
};

export const getAllServiceSlugs = (): string[] => {
  return SERVICE_DETAILS.map(s => s.slug);
};

export const getRelatedServices = (
  relatedSlugs: string[]
): IServiceDetail[] => {
  return SERVICE_DETAILS.filter(s => relatedSlugs.includes(s.slug));
};

export default SERVICE_DETAILS;
