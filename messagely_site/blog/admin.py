"""creates post in admin webpage"""
from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    """blog post details"""
    list_display = (
        'title',
        'created',
        'updated',
    )

    search_fields = (
        'title',
    )

admin.site.register(models.Post, PostAdmin)
