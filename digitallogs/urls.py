# digitallogs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.downtime_list, name='downtime_list'),
]
