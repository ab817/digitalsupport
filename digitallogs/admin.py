# digitallogs/admin.py

from django.contrib import admin
from .models import Downtime, Serveraccess

admin.site.register(Downtime)
admin.site.register(Serveraccess)
