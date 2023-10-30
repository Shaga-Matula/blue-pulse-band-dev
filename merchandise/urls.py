from django.urls import path
from .views import AllMerchView, MerchendiseDetailView


urlpatterns = [
    path('all_merchandise/', AllMerchView.as_view(), name='all_merchandise'),
    path('all_merchandise/<int:pk>/', MerchendiseDetailView.as_view(), name='merch_item')
]
