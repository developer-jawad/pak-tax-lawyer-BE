from django_filters import rest_framework as filters
from blog.models import BlogPost


class BlogPostFilter(filters.FilterSet):
    q = filters.CharFilter(method='search_filter', help_text="Search in title, excerpt, author")
    category = filters.NumberFilter(field_name='category', help_text="Filter by category ID")

    class Meta:
        model = BlogPost
        fields = ['category']

    def search_filter(self, queryset, name, value):
        if value:
            return queryset.filter(
                title__icontains=value
            ) | queryset.filter(
                excerpt__icontains=value
            ) | queryset.filter(
                author__icontains=value
            )
        return queryset
