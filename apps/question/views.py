# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from apps.category.models import Category
from apps.common.AdminView import AdminView
from apps.common.serializers import PageSerializer

# Create your views here.
from apps.question.models import Question


class QuestionIndexView(AdminView):
    def get(self, request):
        serializer = PageSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        paginator = Paginator(Question.objects.all(), serializer.data.get('size'))
        page_obj = paginator.get_page(serializer.data.get('page'))
        return HttpResponse(
            loader.get_template('questions/questions.html').render(
                {
                    'page_obj': page_obj,
                    'categories': Category.objects.all(),
                    'q': serializer.data.get('q'),
                    'segment': 'questions'
                }
                , request))


class QuestionCreateUpdateView(AdminView):
    def post(self, request):
        params = request.POST.dict()
        del params['csrfmiddlewaretoken']
        if params.get('category'):
            params['category'] = Category.objects.get(id=params['category'])

        Question.objects.update_or_create(id=params.get("id"), defaults=params)
        return redirect("/admin/questions/")


class QuestionDeleteView(AdminView):
    def post(self, request):
        data = request.POST.dict()
        Question.objects.get(id=data.get("id")).delete()
        return redirect("/admin/questions/")
