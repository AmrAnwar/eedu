from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_delete
from django.core.urlresolvers import reverse

import random
import string

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("users:profiles", kwargs={'id': self.id})


class UserProfile(models.Model):
    group = models.ForeignKey(Group)
    user = models.OneToOneField(User, default=1, related_name='profile')
    username = models.CharField(max_length=20, default="null")
    password = models.CharField(max_length=25)
    token = models.CharField(max_length=500)
    login = models.BooleanField(default=False)
    # class Meta:
    #     ordering = ["username"]

def create_profile(sender, instance, **kwargs):
    if kwargs['created']:
            password = generate(8)
            instance.password = password
            user = User(username=instance.username,)
            user.set_password(password)
            user.save()
            instance.user = user
            instance.save()


post_save.connect(create_profile, sender=UserProfile)



def delete_user(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()
post_delete.connect(delete_user, sender=UserProfile)


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
