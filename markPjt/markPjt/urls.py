# -*- coding:utf-8 -*-
"""markPjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 主页
    url(r'^$', 'mark.views.index', name='index'),
    # /markbookDIR/
    url(r'^markbookdir/$', 'mark.views.showDIR', name='markbookdir'),
    # /markbook/()/  ---------------()括号中的值被传递到views下面的函数中
    url(r'^markbook/(.*)', 'mark.views.showmarkbooklist', name='markbook'),
    # /markbook/()/detail
    url(r'^markbook/(.*)/detail/$', 'mark.views.showmarkbookdetail', name='markbookDetail'),
]
