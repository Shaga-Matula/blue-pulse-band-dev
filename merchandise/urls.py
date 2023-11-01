from django.urls import path
from .views import AllMerchView, merchandiseDetailView


urlpatterns = [
    path('all_merchandise/', AllMerchView.as_view(), name='all_merchandise'),
    path('all_merchandise/<int:pk>/', merchandiseDetailView.as_view(), name='merch_item')
]
