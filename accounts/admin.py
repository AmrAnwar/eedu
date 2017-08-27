# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile, Group


class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ["username"]
    list_display = ['username', 'password', 'group']

    fieldsets = (
        (None, {
            'fields': ('username', 'group', 'login')
        }),
    )
    list_filter = ('group',)
    class Meta:
		model = UserProfile

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
