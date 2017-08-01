#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 11:42
# @Author  : chenshoubiao
# @File    : user_main.py
# @Soft    : python3


from dj.backend.logic import handle

handle.home()



#调用关系
#user_main.py程序的入口文件，执行该文件，然后去调用handle.py处理，handle.py再去调用sql_api.py验证
#然后sql_api.py再去读取settings.py的配置





