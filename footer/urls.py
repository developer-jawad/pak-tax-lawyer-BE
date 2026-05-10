from django.urls import include, path

urlpatterns = [
    path("footer/", include("footer.api.urls")),
]
