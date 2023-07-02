# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import LoginForm
from .models import User, Message
from ..common.AdminView import AdminView
from ..common.serializers import PageSerializer


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None
    if request.user.is_authenticated:
        return redirect("/admin")

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect("/admin")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def logout_view(request):
    logout(request)
    return redirect("/admin/login/")


class UsersView(AdminView):

    def get(self, request):
        serializer = PageSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        paginator = Paginator(User.objects.all(), serializer.data.get('size'))
        page_obj = paginator.get_page(serializer.data.get('page'))
        return HttpResponse(
            loader.get_template('users/users.html').render(
                {
                    'page_obj': page_obj,
                    'size': serializer.data.get('size'),
                    'q': serializer.data.get('q'),
                    'segment': 'users'
                }
                , request))


class ContactsIndexView(AdminView):
    def get(self, request):
        serializer = PageSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        paginator = Paginator(Message.objects.all(), serializer.data.get('size'))
        page_obj = paginator.get_page(serializer.data.get('page'))
        return HttpResponse(
            loader.get_template('users/contacts.html').render(
                {
                    'page_obj': page_obj,
                    'q': serializer.data.get('q'),
                    'segment': 'contacts'
                }
                , request))
