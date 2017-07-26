# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Ask
from django.contrib import admin

# Register your models here.
class AskAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('question', 'image_sender', 'file_sender')
        }),
        ('Advanced options', {
            'classes': ('collapse'),
            'fields': ('wait', 'replay', 'image_staff', 'file_staff'),
        }),
    )

admin.site.register(Ask, AskAdmin)
