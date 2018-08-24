# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import  render,render_to_response
from django import forms
from django.http import HttpResponse
from disk.models import User
from django.shortcuts import render

# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField()
    filepath = forms.FileField()


def upload(request):
    if request.method == "POST":
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            filepath = uf.cleaned_data['filepath']
            user = User()
            user.username = username
            user.filepath = filepath
            user.save()
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    return render_to_response('upload.html', {'uf': uf})
