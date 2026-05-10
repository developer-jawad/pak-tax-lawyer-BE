from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from blog.models import BlogStatistic
from blog.api.serializers import BlogStatisticSerializer


class BlogStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogStatistic.objects.all()
    serializer_class = BlogStatisticSerializer
    permission_classes = [AllowAny]
