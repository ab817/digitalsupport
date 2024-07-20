# digitallogs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.downtime_list, name='downtime_list'),
    path('export/', views.export_downtimes_csv, name='export_downtimes_csv'),
]
