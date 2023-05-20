# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from apps.category.models import Category
from apps.question.models import Question
from apps.users.models import User


@login_required(login_url="/admin/login/")
def index(request):

    return HttpResponse(loader.get_template('home/index.html').render(
        {
            'segment': 'web',
            'users_number':  User.objects.all().count(),
            'questions_number': Question.objects.all().count(),
            'categories_number': Category.objects.all().count(),
        }
        , request))


def default404(request, exception):
    return render(request, 'errors/page-404.html')


def directed404(request):
    return render(request, 'errors/page-404.html')


def default500(request):
    return render(request, 'errors/page-500.html')
