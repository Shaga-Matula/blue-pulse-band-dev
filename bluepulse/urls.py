""" Blue Pulse URL Configuration """


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("", include("musicapp.urls")),
    path("", include("merchandise.urls")),
    path("checkout/", include("checkout.urls")),
    path("", include("bag.urls")),
    path("profile/", include("profiles.urls")),
    path('newsletter/', include('newsletter.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
