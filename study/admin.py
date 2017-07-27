# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models


class WordInline(admin.TabularInline):
    model = models.Word


class WordAdmin(admin.ModelAdmin):
    list_display = ['name', 'translation', 'part', ]

# class WordLikeAdmin(admin.ModelAdmin):
#     list_display = ['name', 'translation', 'part', ]


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


class ChoicesInline(admin.TabularInline):
    model = models.Choices
    extra = 0


class CompleteInline(admin.TabularInline):
    model = models.Complete
    extra = 0


class DialogInline(admin.TabularInline):
    model = models.Dialog
    extra = 0


class MistakeInline(admin.TabularInline):
    model = models.Mistake
    extra = 0


class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'part', ]
    fieldsets = (
        (None,{
            'fields':('title', 'part',)
        }),
    )
    inlines = [ChoicesInline, DialogInline, CompleteInline, MistakeInline]

admin.site.register(models.Unit, UnitAdmin)

admin.site.register(models.Part, PartAdmin)

# admin.site.register(models.Word, WordAdmin)

admin.site.register(models.Test, TestAdmin)