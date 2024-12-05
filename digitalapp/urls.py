# blog/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path("faq/", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('category/<str:category_name>/', views.blog_category, name='blog_category'),
    path("search", views.search, name="search_all"),
    path("", views.portal, name='portal'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('faq_feedback/', views.faq_feedback, name='faq_feedback'),
    path('digitalproducts/', views.digital_products, name='digital_products'),
    path('digitalproducts/<int:product_id>/', views.digital_product_detail, name='digital_product_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('notices/', views.notices, name='notices'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)