from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contact_list, name='contact_list'),
    path('telephone-lines/', views.telephone_lines, name='telephone_lines'),
    path('contact-cards/', views.contact_card_view, name='contact_cards'),
]
