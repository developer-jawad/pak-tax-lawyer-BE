from django.urls import include, path

urlpatterns = [
    path("about/", include("about.api.urls")),
]
