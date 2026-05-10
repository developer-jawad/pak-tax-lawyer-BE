from collections import namedtuple

APP_NAME = "common"

SITE_NAME = "DRF Boilerplate"

BLOG_CATEGORIES = namedtuple(
    "BLOG_CATEGORIES",
    "all tax_filing business_tax tax_planning sales_tax nrp_tax corporate_tax property_tax",
)._make(range(8))

BLOG_CATEGORY_CHOICES = [
    (BLOG_CATEGORIES.all, 'All'),
    (BLOG_CATEGORIES.tax_filing, 'Tax Filing'),
    (BLOG_CATEGORIES.business_tax, 'Business Tax'),
    (BLOG_CATEGORIES.tax_planning, 'Tax Planning'),
    (BLOG_CATEGORIES.sales_tax, 'Sales Tax'),
    (BLOG_CATEGORIES.nrp_tax, 'NRP Tax'),
    (BLOG_CATEGORIES.corporate_tax, 'Corporate Tax'),
    (BLOG_CATEGORIES.property_tax, 'Property Tax'),
]
