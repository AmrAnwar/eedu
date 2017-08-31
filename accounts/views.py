# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserProfile, Group
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@staff_member_required()
def group_list(request):
    qs = Group.objects.all()
    context = {
        'groups': qs
    }
    return render(request, "groups.html", context=context)

@staff_member_required()
def profiles(request, id=None):
    group = get_object_or_404(Group, id=id)
    qs = UserProfile.objects.filter(group=group)
    if request.GET.get('search'):
        search_id = request.GET.get('search')
        qs = qs.filter(id=search_id)
    context = {
        'group': group,
        'profiles': qs
    }
    return render(request, "profiles.html", context=context)
