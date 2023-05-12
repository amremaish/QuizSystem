# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models

from apps.common.shared_models import TimeStampedModel


class Category(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
