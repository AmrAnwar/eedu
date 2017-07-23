# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models


class WordInline(admin.TabularInline):
    model = models.Word


class WordAdmin(admin.ModelAdmin):
    list_display = ['name', 'translation', 'part', ]


class UnitAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'wait', 'note',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug',),
        }),
    )


class PartAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'wait','unit')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug',),
        }),
    )
    inlines = [WordInline]


admin.site.register(models.Unit, UnitAdmin)

admin.site.register(models.Part, PartAdmin)

admin.site.register(models.Word, WordAdmin)
