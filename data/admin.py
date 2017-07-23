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

admin.site.register(File, FileAdmin)
