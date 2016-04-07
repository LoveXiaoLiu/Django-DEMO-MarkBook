# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from mark.models import markbook, markbookDIR

# Create your views here.

def index(request):
    # if request != '' and request.method == 'POST':
    #     data = request.POST
    # return HttpResponse('ok')
    return  HttpResponseRedirect('/markbookdir/')                  # 重定向到书签夹页面

def showDIR(request):
    if request != '' and request.method == 'GET':
        mbDirList = markbookDIR.objects.all()                        # 获取数据库中 书签夹 的所有数据
        return render_to_response('show_markbook_dir.html', locals())           # # loclas()是将所有变量传递给模板
        # return HttpResponse('ok')
    return Http404()


def showmarkbooklist(request, i):
    dir_i = i.strip('/')                               # 出现了一个问题是由于传过来的‘i’带了一个‘/’，导致后面无法使用该参数
    if request != '' and request.method == 'GET':
        markObj = markbookDIR.objects.get(dir_name=dir_i)             # 获取书签夹名称为 dir_i 的对象
        markBookList = markObj.markbook_set.all()                         # 获得 dir_i 书签夹下的所有书签
        return render_to_response('show_markbook.html', locals())
        # return HttpResponse(dir_i)
    # return HttpResponse(request.method)

def showmarkbookdetail(request, i):
    dir_i = i.strip('/')
    if request != '' and request.method == 'GET':
        # markObj = markbookDIR.objects.get(dir_name=dir_i)
        # markB = markObj.markbook_set.get(mark_name=dir_i)
        markB = markbook.objects.get(mark_name=dir_i)
        return render_to_response('show_markbook _detail.html', locals())
        # return HttpResponse(markB.mark_name)
    # return HttpResponse(dir_i)
