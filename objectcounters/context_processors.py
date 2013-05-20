#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models import CounterTool


def global_counter_tool(request):
    return {'counters' : CounterTool()}
