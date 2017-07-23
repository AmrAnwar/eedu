# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Ask(models.Model):
    user = models.ForeignKey(User, null=False, default=1, related_name="sender")
    question = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    replay = models.TextField(null=True, blank=True)
    wait = models.BooleanField(default=True)

    class Meta:
        ordering = ["-timestamp"]

    def __unicode__(self):
        return "From: %s, Question num: %s" %(self.user, self.id)
