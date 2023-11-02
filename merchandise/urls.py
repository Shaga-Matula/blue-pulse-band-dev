from django.urls import path
from .views import AllMerchView, MerchandiseDetailView


urlpatterns = [
    path('all_merchandise/', AllMerchView.as_view(), name='all_merchandise'),
    path('all_merchandise/<int:pk>/', MerchandiseDetailView.as_view(), name='merch_item')
]
