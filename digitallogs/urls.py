# digitallogs/urls.py
from django.shortcuts import redirect
from django.urls import path
from . import views
from .views import export_technical_logs_csv, technical_log_list

urlpatterns = [
    path('', views.adminpanel, name='adminpanel'),
    path('downtimes/', views.downtime_list, name='downtime_list'),
    path('export_downtimes/', views.export_downtimes_csv, name='export_downtimes_csv'),
    path('export_serveraccess/', views.export_serveraccess_csv, name='export_serveraccess_csv'),
    path('serverlogs/', views.serverlog_list, name='serverlog_list'),
    path('technicallog/', technical_log_list, name='technical_log_list'),
    path('technicallog/export/', export_technical_logs_csv, name='export_technical_logs_csv'),
    #path('tasklog/', views.tasklog_list, name='tasklog_list'),
    path('tasklog/', views.redirect_to_overall, name='tasklog_default'),
    path('tasklog/list/', views.tasklog_list, name='tasklog_list'),
    path('serverip/', views.serverip, name='serverip'),
    path('export_serverdetails_csv',views.export_serverdetails_csv, name='export_serverdetails_csv'),
    #bulk feedback form - bulk-form.html
    path('bulk-form/', views.bulk_form, name='bulk_form'),
    path('bulk-form-admin/', views.bulk_form_admin, name='bulk_form_admin'),
    path('export_customer_form_csv/', views.export_customer_form_csv, name='export_customer_form_csv'),
]

