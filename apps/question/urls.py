# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from apps.question.views import *

urlpatterns = [

    path('questions/', QuestionIndexView.as_view()),
    path('questions/create-update/', QuestionCreateUpdateView.as_view()),
    path('questions/delete/', QuestionDeleteView.as_view()),
]
