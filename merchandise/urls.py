from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import AllMerchView, MerchandiseDetailView

urlpatterns = [
    path("all_merchandise/", AllMerchView.as_view(), name="all_merchandise"),
    path(
        "all_merchandise/<int:pk>/", MerchandiseDetailView.as_view(), name="merch_item"
    ),
    path("add/", views.add_merch, name="add_merch"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
