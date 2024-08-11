# digitallogs/admin.py

from django.contrib import admin
from .models import Downtime, Serveraccess, TechnicalSupportLog, TaskLog

admin.site.register(Downtime)
admin.site.register(Serveraccess)
admin.site.register(TechnicalSupportLog)
admin.site.register(TaskLog)
