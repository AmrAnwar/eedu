# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from django.contrib.auth.models import User

choices_mcq = (
    ('a', 'choice_one'),
    ('b', 'choice_two'),
    ('c', 'choice_three'),
)
# Create your models here.


class Unit(models.Model):
    title = models.CharField(max_length=255)
    note = models.TextField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    wait = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return self.title


class Part(models.Model):
    title = models.CharField(max_length=255)
    unit = models.ForeignKey(Unit, related_name='unit')
    slug = models.SlugField(unique=True, null=True, blank=True)
    wait = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return "%s : %s"%(self.unit,self.title)


class Word(models.Model):
    name = models.CharField(max_length=150)
    translation = models.CharField(max_length=150)
    part = models.ForeignKey(Part, related_name='part')
    timestamp = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
    #                                related_name="comment_likes")
    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return self.name


class Test(models.Model):
    title = models.CharField(max_length=255)
    part = models.ForeignKey(Part, related_name='Test_Part')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]


class Choices(models.Model):
    question = models.TextField(null=False)
    choice_one = models.CharField(max_length=50, null=False)
    choice_two = models.CharField(max_length=50, null=False)
    choice_three = models.CharField(max_length=50, null=False)
    answer = models.CharField(choices=choices_mcq, max_length=3)
    test = models.ForeignKey(Test, related_name='Test_Choices')


class Complete(models.Model):
    description = models.TextField(null=False)
    answer = models.CharField(max_length=50, null=False)
    test = models.ForeignKey(Test, related_name='Test_Complete')


class Dialog(models.Model):
    description = models.TextField(null=False)
    first_speaker = models.CharField(max_length=50, null=False)
    second_speaker = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50, null=False)
    test = models.ForeignKey(Test, related_name='Test_Dialog')


class Mistake(models.Model):
    description = models.TextField(null=False)
    replace = models.CharField(max_length=50, null=False)
    answer = models.CharField(max_length=50, null=False)
    test = models.ForeignKey(Test, related_name='Test_Mistake')


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


pre_save.connect(pre_save_post_receiver, sender=Part)

pre_save.connect(pre_save_post_receiver, sender=Unit)
