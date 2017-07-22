# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Answer


# Register your models here.
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'type']
    list_display_links = ['timestamp']
    list_editable = ['title']
    list_filter = ['user', 'timestamp']


admin.site.register(Answer, admin_class=AnswerModelAdmin)