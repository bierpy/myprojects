#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 15:10
# @Author  : chenshoubiao
# @File    : login.py
# @Soft    : python3
import os

# 存放用户账号密码文件
account_file = 'account.txt'
# 存放被锁用户文件
lock_file = 'lock.txt'

# 开始使循环为true
while True:
    # 程序每次执行都需要去读取被锁用户，存放到lock_list列表里面
    f = open(lock_file)
    lock_list = []
    for i in f.readlines():
        line = i.strip()
        lock_list.append(line)
    f.close()

    # 设置一个变量loginSuccess为false，让程序正常执行
    loginSuccess = False
    username = input('请输入账号:').strip()

    # 如果输入的用户在被锁用户列表，提示用户被锁定，退出整个程序
    if username in lock_list:
        print("对不起，你输入的账号已经被锁住，请联系管理员开通!")
        break

    # 把用户账号密码全部读取出来放到account_list列表['www 123\n', 'qqq 123\n', 'bier 123\n',]
    f = open(account_file)
    account_list = f.readlines()
    f.close()

    # 从这里开始不断去遍历用户列表
    for line in account_list:
        # 把account_list用户列表切开，成为['www', '123']，默认是\n分隔
        user = line.split()
        if user[0] == username:
            # 如果输入的账号正确，验证输入的3次密码是否正确，超过三次锁住用户
            for i in range(3):
                password = input('请输入密码:').strip()
                if password == user[1]:
                    print("你好 %s ：欢迎你登陆存管系统!" % username)
                    loginSuccess = True  # 整个程序退出
                    break
                else:
                    # 输入密码错误超过三次就退出 for i in range(3):层循环
                    print("你输入的密码不正确,请重新输入！")

            # 如果输入的三次密码不正确，那就将该账号追加到被锁用户文件里面
            else:
                f = open(lock_file, 'a')
                f.write('\n%s' % username)
                f.close()
                print("你输入的密码错误次数超过3次，你的账号:%s 已经被锁住！" % username)
                loginSuccess = True  # 设置这个就是为了让下面判断为True就跳出整个程序
                break

            if loginSuccess is True:
                break  # 跳出顶层for循环，for line in account_list:
    else:
        # 除了判断输入的用户user[0] == username:外，其他情况就是不存在了。for....else 可以这样子写
        print("你输入的账号不存在，请重新输入！")
        continue

    if loginSuccess is True:
        break  # 跳出while循环
