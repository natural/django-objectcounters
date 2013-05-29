from django.contrib import admin

from objectcounters.admin import CounterTabularInline

from .models import MySite


class MySiteAdmin(admin.ModelAdmin):
    inlines = [CounterTabularInline]

admin.site.register(MySite, MySiteAdmin)