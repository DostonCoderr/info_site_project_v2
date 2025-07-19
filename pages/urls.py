# pages/urls.py
from django.urls import path
from . import views
from .views import home
urlpatterns = [
    path('',home.as_view(), name='home'),
    path('ochiq_malumotlar/', views.ochiq_malumotlar, name='ochiq_malumotlar'),
    path('manzil/', views.manzil, name='manzil'),
    path('aloqa/', views.aloqa, name='aloqa'),
    path('biz_haqimizda/', views.biz_haqimizda, name='biz_haqimizda'),
]