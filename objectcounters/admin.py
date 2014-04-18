#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

try:
    from genericadmin.admin import GenericAdminModelAdmin as ModelAdmin
except ImportError:
    ModelAdmin = admin.ModelAdmin

from .models import Counter


class CounterAdmin(ModelAdmin):
    ordering = ('name',)
    list_display = ('id', 'name', 'value', 'content_type', 'object_id',
                    'content_object',)
    list_filter = ('name', 'content_type',)
    search_fields = ('object_id',)


admin.site.register(Counter, CounterAdmin)
