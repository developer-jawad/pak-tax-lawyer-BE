from django.urls import include, path

urlpatterns = [
    path('service/', include('service.api.urls')),
]
