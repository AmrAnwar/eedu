# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.utils.text import slugify
User = get_user_model()

# Create your models here.
def upload_location(instance, filename):
    if instance.id:
        new_id = instance.id
    else:
        try:
            new_id = File.objects.order_by("id").last().id + 1
        except:
            new_id = 1
    return "data/%s/%s" % (new_id, filename)

first_user = User.objects.all().first()
class File(models.Model):
    user = models.ForeignKey(User, default=first_user.id, null=False)
    title = models.CharField(null=False, max_length=50)
    note = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    file = models.FileField(null=False,
                            blank=False,
                            upload_to=upload_location)
    class Meta:
        ordering = ["-timestamp"]

    def __unicode__(self):
        return "%s" %(self.title)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = File.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=File)
