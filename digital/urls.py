from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
admin.site.site_header='Digital Support Admin'


urlpatterns = [
    #path('', include('admin_material.urls')),
    path('admin/', admin.site.urls),
    path("", include("digitalapp.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path("", include("digitalcontact.urls")),
    path("digitallogs/", include("digitallogs.urls")),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)