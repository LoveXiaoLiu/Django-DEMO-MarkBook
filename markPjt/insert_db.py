#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-07-28 20:38:38
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
 
'''
create some records for demo database
'''
 
from markPjt.wsgi import *
from mark.models import markbook, markbookDIR
 
 
def main():
    mbdir = [
      ('java', 'j2ee'),
      ('mysql', 'mysqldb'),
      ('c++', 'c#'),
    ]
 
    for name, info in mbdir:
        c = markbookDIR.objects.get_or_create(dir_name=name, dir_info=info)[0]
 
        # 创建 10 个书签
        for i in range(1, 11):
            mb = markbook.objects.get_or_create(
                mark_name='{}_{}'.format(name, i),
                mark_url='https://{}'.format(i),
                mark_belong=c
            )[0]
 

 
 
if __name__ == '__main__':
    main()
    print("Done!")