#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 11:43
# @Author  : chenshoubiao
# @File    : handle.py
# @Soft    : python3


from dj.backend.db.sql_api import select


def home():
    print("this is home page!")
    q_data = select("user",'add')
    print("q_data=",q_data)

def movie():
    print("this is movie page!")


def tv():
    print("this is tv page!")















