from django.urls import include, path

urlpatterns = [
    path("video/", include("videos.api.urls")),
]
