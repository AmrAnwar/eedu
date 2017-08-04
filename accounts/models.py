from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
import random
import string


class Group(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    group = models.ForeignKey(Group)
    user = models.OneToOneField(User, default=1)
    username = models.CharField(max_length=20, default="null")
    password = models.CharField(max_length=25)
    token = models.CharField(max_length=500)


def create_profile(sender, instance, **kwargs):
    if kwargs['created']:
            password = generate(8)
            instance.password = password
            user = User.objects.create(username=instance.username, password=password)
            user.save()
            instance.user = user
            instance.save()
    else:
        user = instance.user
        print instance.username
        user.username = instance.username
        user.save()


post_save.connect(create_profile, sender=UserProfile)
def generate(word_size):
    """
    return a string of len = (length) and each word in len random.randint(1,word_size)
    """
    word = ''
    for i in range(1, word_size + 1):
        if i % 2:
            data = string.ascii_lowercase
        else:
            if i % 3:
                data = string.ascii_uppercase
            else:
                data = "1234567890"
        word += data[random.randint(0, len(data) - 1)]
    return word
