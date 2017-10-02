# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse,redirect
from django.contrib.auth.models import User
from django_sites import reverse as sites_reverse

choices_mcq = (
    ('a', 'choice_one'),
    ('b', 'choice_two'),
    ('c', 'choice_three'),
)
# Create your models here.



class Exam(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return "exam: %s" % self.title


class Exercise(models.Model):
    TYPE = (
        (1, "Situations"),
        (2, "Dialog"),
        (3, "Choices"),
        (4, "Find the Mistake"),
        (5, "Article"),  # can't remember the real name
        (6, "Story"),
        (7, "Translation"),
        (8, "Paragraph"),
    )
    exam = models.ForeignKey(Exam, default=1)
    question = models.TextField()
    answer = models.TextField()
    type = models.IntegerField(choices=TYPE)
    users = models.ManyToManyField(User, related_name="exercise")


    def __str__(self):
        return "%s" % self.question


class WordBank(models.Model):
    user = models.ForeignKey(User, related_name="word_bank")
    name = models.CharField(max_length=150)
    translation = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.name


class Unit(models.Model):
    title = models.CharField(max_length=255)
    note = models.TextField(max_length=255,null = True, blank = True)
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
        return "%s : %s"%(self.unit, self.title)

    def get_url_words(self):
        return sites_reverse("study-api:part-words", kwargs={"id": self.id})

    def get_url_tests(self):
        return sites_reverse("study-api:part-tests", kwargs={"id": self.id})


class Word(models.Model):
    name = models.CharField(max_length=150)
    translation = models.CharField(max_length=150)
    part = models.ForeignKey(Part, related_name='part')
    timestamp = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
    #                                related_name="comment_likes")
    users = models.ManyToManyField(User, related_name="words")


    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return self.name

class Test(models.Model):
    TYPE = (
        (1, "GENERAL"),
        (2, "MCQ"),
    )
    title = models.CharField(max_length=255)
    part = models.ForeignKey(Part, related_name='Test_Part', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    type = models.IntegerField(choices=TYPE, default=1)

    def __str__(self):
        return "test: %s" % self.title

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


def create_slug_unit(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Unit.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_unit(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver_unit(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_unit(instance)

def create_slug_part(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Part.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_part(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver_part(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_part(instance)

pre_save.connect(pre_save_post_receiver_part, sender=Part)

pre_save.connect(pre_save_post_receiver_unit, sender=Unit)
