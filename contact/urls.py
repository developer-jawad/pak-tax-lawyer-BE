from django.urls import include, path

urlpatterns = [
    path('contact/', include('contact.api.urls')),
]
