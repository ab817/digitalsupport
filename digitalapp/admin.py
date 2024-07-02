# blog/admin.py
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models

from .models import Category, Comment, Post, PortalSetting


class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

class CommentAdmin(admin.ModelAdmin):
    pass

class PortalSettingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PortalSetting, PortalSettingAdmin)