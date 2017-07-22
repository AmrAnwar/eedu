# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post


# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'wait', 'image', 'file')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug', 'height_field_image', 'width_field_image'),
        }),
    )
    list_display = ['title', 'timestamp', 'type']
    list_display_links = ['timestamp']
    list_editable = ['title']
    list_filter = ['user', 'timestamp']


admin.site.register(Post, admin_class=PostModelAdmin)
