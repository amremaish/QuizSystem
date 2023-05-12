# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models

from apps.category.models import Category
from apps.common.shared_models import TimeStampedModel


class Question(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    choice_1 = models.TextField()
    choice_2 = models.TextField()
    choice_3 = models.TextField()
    choice_4 = models.TextField()
    answer_number = models.IntegerField()
