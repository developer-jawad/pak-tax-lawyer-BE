from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.constants import APP_NAME

app_name = APP_NAME

router = DefaultRouter()

urlpatterns = [
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("", include(router.urls)),
]
