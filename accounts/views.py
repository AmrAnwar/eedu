# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserProfile, Group
from django.shortcuts import get_object_or_404
# Create your views here.


def group_list(request):
    qs = Group.objects.all()
    context = {
        'groups': qs
    }
    return render(request, "groups.html", context=context)


def profiles(request, id=None):
    group = get_object_or_404(Group, id=id)
    qs = UserProfile.objects.filter(group=group)
    print qs
    context = {
        'group': group,
        'profiles': qs
    }
    return render(request, "profiles.html", context=context)
