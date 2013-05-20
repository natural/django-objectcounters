#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin

from .models import Counter


class CounterAdmin(GenericAdminModelAdmin):
    ordering = ('name', )
    list_display = ('id', 'name', 'value', 'content_type', 'object_id',
                    'content_object', )
    list_filter = ('name', 'content_type', )
    search_fields = ('object_id', )


admin.site.register(Counter, CounterAdmin)
