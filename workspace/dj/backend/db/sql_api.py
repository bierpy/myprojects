#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 11:43
# @Author  : chenshoubiao
# @File    : sql_api.py
# @Soft    : python3

from dj.config import settings


def db_auth(configs):
    if configs.DATABASE["user"] == "root" and configs.DATABASE["password"] == "123":
        print("db auth passed!")
        return True

    else:
        print("db login error.....")


def select(table,colum):
    if db_auth(settings):
        if table == "user":
            user_info = {
                "001":["www",22,"engines"],
                "002": ["bier", 22, "pythnon"],
                "003": ["eson", 22, "thiger"]
            }
            return user_info








