from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.api.urls')),
]
