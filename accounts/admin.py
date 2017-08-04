# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, Group


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'group']
    fieldsets = (
        (None, {
            'fields': ('username', 'group')
        }),
    )

class UserAdmin(admin.TabularInline):
    fieldsets = (
        (None, {
            'fields': ('username',)
        }),
    )
    model = UserProfile
    extra = 0

class GroupAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),

    )
    inlines = [UserAdmin]

admin.site.register(Group, GroupAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
# Register your models here.
