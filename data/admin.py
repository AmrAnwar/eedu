# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import File
from django.contrib import admin

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'note', 'file',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug',),
        }),
    )
    list_display = ['title', 'file', 'timestamp']
    list_display_links = ['timestamp']
    list_editable = ['title']

admin.site.register(File, FileAdmin)
