from django.urls import path
from .import views
from .views import MerchandiseView

urlpatterns = [
    path('all_goods/', views.MerchandiseView.as_view(), name='all_goods'),
]
