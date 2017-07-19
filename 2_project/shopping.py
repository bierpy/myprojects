#!/usr/bin/env python
# -*- coding: utf-8 -*-
#实现购物功能

import sys
while True:
        try:
                salary = int(input('请输入你的工资:'))
                break
        except ValueError:
                print("请输入数字")

products = [
['Iphone',5800],['MacPro',12000],['NB Shoes',680],['Cigarate',48],['MX',2500]

]

# 购物车列表
shopping_list = []

while True:
        for p in products:
                #products_index=products.index(p)
                #print products.index(['Iphone', 5800]) = 0
                #p[0]=Iphone
                #获取每一个商品的索引和值
                print (products.index(p) ,p[0], p[1])
        choice = input("\033[32;1m请选择你要购买的商品，按q结算:\033[0m").strip()
        if choice == 'q':
                print ("\033[32;1m你购买了如下商品:\033[0m")
                for i in shopping_list:
                        print ('\t',i)

                sys.exit('Goodbye!')
        if len(choice) == 0:
                print("\033[32;1m请选择你要购买的商品\033[0m")
                continue
        if not choice.isdigit():continue

        #将输入的值转为整形
        choice = int(choice)
        #如果输入的数字大于商品的长度，也就是index的值，提示找不到商品
        if choice >= len(products):
              print ('\033[31;1m没有找到该商品\033[0m')
              continue

        #将选择的商品赋值给一个变量pro,choice是一个数字，products[choice]就是完整的商品名与价格
        pro = products[choice]
        if salary >= pro[1]:
                salary = salary - pro[1]
                #将购买的商品加入到购物列表
                shopping_list.append(pro)
                print ("\033[34;1m已将 %s 添加到购物车列表 ,你还剩下$%s\033[0m" % (pro[0],salary))

        else:
                print ('你选择的%s 价格为 %s, 你的工资是%s ，没有足够的钱购买该商品，请重新选择商品' %(pro[0],pro[1],salary))
