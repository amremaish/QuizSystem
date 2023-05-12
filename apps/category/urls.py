# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from apps.category.views import *

urlpatterns = [

    path('categories/', CategoryIndexView.as_view()),
    path('categories/create-update/', CategoryCreateUpdateView.as_view()),
    path('categories/delete/', CategoryDeleteView.as_view()),
]
