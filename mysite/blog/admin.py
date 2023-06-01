from django.contrib import admin

# Register your models here.
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'updated',
    )

    search_fields = (
        'title',
    )

#Registers the 'Post' model in models.py
admin.site.register(models.Post, PostAdmin)