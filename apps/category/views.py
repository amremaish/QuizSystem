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


class CategoryIndexView(AdminView):
    search_cols = []

    def get(self, request):
        serializer = PageSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        paginator = Paginator(Category.objects.all(), serializer.data.get('size'))
        page_obj = paginator.get_page(serializer.data.get('page'))
        return HttpResponse(
            loader.get_template('categories/categories.html').render(
                {
                    'page_obj': page_obj,
                    'q': serializer.data.get('q'),
                    'segment': 'categories'
                }
                , request))


class CategoryCreateUpdateView(AdminView):
    def post(self, request):
        params = request.POST.dict()
        del params['csrfmiddlewaretoken']
        Category.objects.update_or_create(id=params.get("id"), defaults=params)
        return redirect("/admin/categories/")


class CategoryDeleteView(AdminView):
    def post(self, request):
        data = request.POST.dict()
        try:
            Question.objects.filter(category__id=data.get("id")).delete()
        except Exception as a:
            pass
        Category.objects.get(id=data.get("id")).delete()
        return redirect("/admin/categories/")
