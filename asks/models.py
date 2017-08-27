# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

def upload_location(instance, filename):
    # if re.search(r'\w+.(\w+)', "python.png"):
    #     pass
    # else:
    #     raise ValueError("enter photo")
    if instance.id:
        new_id = instance.id
    else:
        try:
            new_id = Ask.objects.order_by("id").last().id + 1
        except:
            new_id = 1
    return "asks/%s/%s" % (new_id, filename)

try:
    first_user = User.objects.all().first()
    first_user = first_user.id
except:
    first_user = 1
    # Create your models here.


class Ask(models.Model):
    user = models.ForeignKey(User, null=False, default=1, related_name="sender")
    question = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    replay = models.TextField(null=True, blank=True)
    image_sender = models.ImageField(
        upload_to=upload_location,
        null=True, blank=True,
        height_field='height_field_image',
        width_field='width_field_image',)
    image_staff = models.ImageField(
        upload_to=upload_location,
        null=True, blank=True,
        height_field='height_field_image',
        width_field='width_field_image',)
    file_sender = models.FileField(null=True,
                                 blank=True,
                                 upload_to=upload_location)
    file_staff = models.FileField(null=True,
                                 blank=True,
                                 upload_to=upload_location)
    height_field_image = models.IntegerField(default=0,null=True)
    width_field_image = models.IntegerField(default=0, null=True)
    wait = models.BooleanField(default=True)

    class Meta:
        ordering = ["-updated", "-timestamp"]

    def __unicode__(self):
        return "From: %s, Question num: %s" %(self.user, self.id)
