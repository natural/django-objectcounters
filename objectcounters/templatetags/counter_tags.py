#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template import Library

from ..models import Counter


register = Library()


@register.assignment_tag
def counter_for_object(name, obj, default=0):
    """Returns the counter value for the given name and instance."""
    try:
        return Counter.objects.get_for_object(name, obj).value
    except (Exception, ):
        return default
