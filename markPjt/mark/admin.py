# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import markbook, markbookDIR

# Register your models here.
# 完善后台的功能，在后台添加，编辑，删除数据

class MarkboobAdmin(admin.ModelAdmin):
    list_display = ('mark_name', 'mark_url', 'mark_belong', 'create_time')

class MarkbookDirAdmin(admin.ModelAdmin):
    list_display = ('dir_name', 'dir_info')


admin.site.register(markbook, MarkboobAdmin)
admin.site.register(markbookDIR, MarkbookDirAdmin)
