# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.shortcuts import render


def index(request):
    return render(request, 'web/index.html')


def login(request):
    return render(request, 'web/login.html')


def question(request):
    return render(request, 'web/question.html')
