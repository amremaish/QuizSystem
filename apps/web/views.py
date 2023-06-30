# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from apps.category.models import Category
from apps.question.models import Question


def index(request):
    return HttpResponse(loader.get_template('web/index.html').render({'categories': Category.objects.all()}, request))


def generate_quiz(request, category_id):
    questions = Question.objects.filter(category__id=category_id).order_by('?')[:10]
    cat = Category.objects.get(id=category_id)
    return HttpResponse(loader.get_template('web/quiz.html').render(
        {"questions": questions, "category": cat}, request))


def login(request):
    return render(request, 'web/login.html')


def question(request):
    return render(request, 'web/question.html')
