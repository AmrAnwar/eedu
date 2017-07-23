# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post
# Register your models here.

from django.contrib import admin
from django.contrib.auth.models import User
# from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
#
# admin.site.unregister(User)
admin.site.unregister(Group)
# # admin.site.unregister(Site)
# ---------------------------------------------------#


class PostModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'type', 'wait', 'image', 'file')
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
