# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from mark.models import markbook, markbookDIR

# Create your views here.

def index(request):
    if request != '' and request.method == 'POST':
        data = request.POST
    return HttpResponse('ok')

def showDIR(request):
    if request != '' and request.method == 'GET':
        mbDirList = markbookDIR.objects.all()
        return render_to_response('show_markbook_dir.html', locals())           # # loclas()是将所有变量传递给模板
        # return HttpResponse('ok')
    return Http404()


def showmarkbooklist(request, i):
    return HttpResponse(i)

def showmarkbookdetail(request, i):
    return HttpResponse(i)
