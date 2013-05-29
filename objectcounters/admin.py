#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline, GenericStackedInline

from .models import Counter


class CounterAdmin(GenericAdminModelAdmin):
    ordering = ('name', )
    list_display = ('id', 'name', 'value', 'content_type', 'object_id',
                    'content_object', )
    list_filter = ('name', 'content_type', )
    search_fields = ('object_id', )


class CounterTabularInline(GenericTabularInline):
    model = Counter
    extra = 1


class CounterStackedInline(GenericStackedInline):
    model = Counter
    extra = 1


admin.site.register(Counter, CounterAdmin)
