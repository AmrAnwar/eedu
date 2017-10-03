# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PIL import Image as Img
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile


from django.db import models
from django.contrib.auth import get_user_model
import requests
import json

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
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ["-updated", "-timestamp"]

    def __unicode__(self):
        return "From: %s, Question num: %s" %(self.user, self.id)

    def save(self, *args, **kwargs):
        if self.wait:
            if self.image_sender:
                image = Img.open(StringIO.StringIO(self.image_sender.read()))
                output = StringIO.StringIO()
                image.save(output, format='JPEG', quality=30)
                output.seek(0)
                self.image_sender = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image_sender.name, 'image/jpeg',
                                                  output.len, None)

        else:
            if self.image_staff:
                image = Img.open(StringIO.StringIO(self.image_staff.read()))
                output = StringIO.StringIO()
                image.save(output, format='JPEG', quality=30)
                output.seek(0)
                self.image_staff = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image_staff.name, 'image/jpeg',
                                                  output.len, None)
            if self.public:
                url = 'https://fcm.googleapis.com/fcm/send'
                data = {'to': '/topics/public_question',
                        'data': {
                            'message_title': 'New Public Question Was Answered',
                            'message_body': '',
                            'where': 'public_question'
                        }
                        }
                headers = {
                    'Authorization': 'key=AIzaSyC6PljgOsaTz2fULnW8uIY0sYIJ0MrDWDA',
                    'Content-Type': 'application/json',
                }

                r = requests.post(url, data=json.dumps(data), headers=(headers))

        super(Ask, self).save(*args, **kwargs)
