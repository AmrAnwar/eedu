# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from django.contrib.auth.models import User

# Create your models here.


class Unit(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='users')
    slug = models.SlugField(unique=True, null=True, blank=True)
    wait = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Word(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    unit = models.ForeignKey(Unit, related_name='units')

    def __str__(self):
        return self.name


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Unit.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Unit)