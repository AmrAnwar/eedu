# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models


class WordInline(admin.TabularInline):
    model = models.Word


class WordAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'description']


class UnitAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'wait', 'user')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug',),
        }),
    )
    inlines = [WordInline]


admin.site.register(models.Unit, UnitAdmin)
admin.site.register(models.Word, WordAdmin)
