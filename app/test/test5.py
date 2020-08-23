# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 20:43
# @Author  : yang
# @File    : test5.py
from idna import unicode

s = u'\xc7\xeb\xca\xb9\xd3\xc3\xca\xda\xc8\xa8\xc2\xeb\xb5\xc7\xc2\xbc\xa1\xa3\xcf\xea\xc7\xe9\xc7\xeb\xbf\xb4'
a = s.encode("latin1").decode("gbk")
# b = repr(a)
print(a)