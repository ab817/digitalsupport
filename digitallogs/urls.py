# digitallogs/urls.py

from django.urls import path
from . import views
from .views import export_technical_logs_csv, technical_log_list

urlpatterns = [
    path('', views.downtime_list, name='downtime_list'),
    path('export_downtimes/', views.export_downtimes_csv, name='export_downtimes_csv'),
    path('export_serveraccess/', views.export_serveraccess_csv, name='export_serveraccess_csv'),
    path('serverlogs/', views.serverlog_list, name='serverlog_list'),
    path('technicallog/', technical_log_list, name='technical_log_list'),
    path('technicallog/export/', export_technical_logs_csv, name='export_technical_logs_csv'),
]

