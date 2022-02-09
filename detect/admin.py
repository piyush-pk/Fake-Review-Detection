# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'ip', 'userAgent', 'time')
    list_filter = ('time',)
    search_fields = ('name',)