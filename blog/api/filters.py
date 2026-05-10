from django_filters import rest_framework as filters

from blog.models import BlogPost


class BlogPostFilter(filters.FilterSet):
    category = filters.NumberFilter(
        field_name="category", help_text="Filter by category ID"
    )

    class Meta:
        model = BlogPost
        fields = ["category"]
