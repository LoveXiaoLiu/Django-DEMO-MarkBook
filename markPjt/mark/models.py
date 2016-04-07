# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class markbookDIR(models.Model):
    dir_name = models.CharField('书签夹', max_length=200, unique=True)
    dir_info = models.CharField('描述', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.dir_name


class markbook(models.Model):
    mark_name = models.CharField('书签名', max_length=100, unique=True)
    mark_url = models.CharField('URL地址', max_length=500)
    mark_belong = models.ForeignKey(markbookDIR, verbose_name='所属书签夹', blank=True, null=True)
    create_time = models.CharField('创建时间', max_length=20, blank=True)

    def __str__(self):
        return self.mark_name