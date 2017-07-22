from django.contrib import admin

# Register your models here.
from .models import Comment


class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'timestamp', 'content_type']
    list_display_links = ['timestamp']
    list_filter = (

                ('content_type'),
    )


admin.site.register(Comment, admin_class=AnswerModelAdmin)

