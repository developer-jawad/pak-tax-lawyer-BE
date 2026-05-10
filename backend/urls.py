from allauth.account.views import PasswordResetView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

from common.constants import SITE_NAME


def empty_view(request):
    return HttpResponse("")


admin_paths = [
    path("admin/", admin.site.urls),
]

app_paths = [
    path("django-rq/", include("django_rq.urls")),
    path("users/", include("users.urls"), name="users"),
    path("account/", include("allauth.account.urls")),
    path("api/home/", include("home.urls"), name="home"),
    path("api/", include("service.urls"), name="service"),
    path("api/", include("blog.urls"), name="blog"),
    path("api/", include("about.urls")),
    path("api/", include("videos.urls")),
]

other_paths = [
    # Custom password reset confirmation URL - needed to handle the token-based password reset flow from allauth.
    path(
        "password-reset/<str:uidb64>/<str:token>/",
        PasswordResetView.as_view(),
        name="password_reset_confirm",
    ),
]

urlpatterns = admin_paths + app_paths + other_paths

# Use the settings object to get the MEDIA_ROOT and MEDIA_URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# TODO: Yet to be implemented
# handler404 = Error404View.as_view()
# handler500 = Error500View.as_view()
# handler403 = Error403View.as_view()
# handler400 = Error400View.as_view()

admin.site.site_title = f"{SITE_NAME} Administration"
admin.site.site_header = f"{SITE_NAME} Administration"
admin.site.index_title = f"{SITE_NAME} Administration"
