#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/17 9:33
# @Author  : chenshoubiao
# @File    : 3level_menus.py
# @Soft    : python3
#实现三级菜单的功能

data = {
    '广东': {
        "深圳": {
            "南山": ['tianmao', 'weipinghui'],
            "福田": ['orale', 'mysql']
        },
        "广州": {
            "白云": ['tianmao', 'weipinghui'],
            "天河": ['alyun', 'huawei']
        },
        "东莞": {
            "南城": ['tianmao', 'weipinghui'],
            "东城": ['orale', 'mysql']
        }
    },

    '北京': {
        "昌平": {
            "A沙河": ['taobao', 'jd'],
            "A天通范": ['alyun', 'huawei']
        },
        "朝阳": {
            "B沙河": ['taobao', 'jd'],
            "B天通范": ['alyun', 'huawei']
        },
        "海锭": {
            "C沙河": ['taobao', 'jd'],
            "C天通范": ['alyun', 'huawei']
        }
    },

    '湖南': {
        "昌平": {
            "A沙河": ['taobao', 'jd'],
            "A天通范": ['alyun', 'huawei']
        },
        "朝阳": {
            "B沙河": ['taobao', 'jd'],
            "B天通范": ['alyun', 'huawei']
        },
        "海锭": {
            "C沙河": ['taobao', 'jd'],
            "C天通范": ['alyun', 'huawei']
        }
    }
}

exit_flag = False

while not exit_flag:
    # 默认打印第一层
    for i1 in data:
        print(i1)

    #接收用户选择第一层输入的选项
    choice1 = input("请选择输入第1层的选项>>：")
    #如果用户输入的选项在第一层里面，那么程序会继续执行
    if choice1 in data:
        while not exit_flag:
            #遍历和打印第二层的内容
            for i2 in data[choice1]:
                print("\t", i2)

            # 接收用户选择第二层输入的选项
            choice2 = input("请选择输入第2层的选项>>：")
            # 如果用户输入的选项在第二层里面，那么程序会继续执行
            if choice2 in data[choice1]:
                while not exit_flag:
                    # 遍历和打印第三层的内容
                    for i3 in data[choice1][choice2]:
                        print("\t\t", i3)

                    # 接收用户选择第三层输入的选项
                    choice3 = input("请选择输入第3层的选项>>：")
                    # 如果用户输入的选项在第三层里面，那么程序会继续执行
                    if choice3 in data[choice1][choice2]:
                        while not exit_flag:
                            # 遍历和打印第四层的内容
                            for i4 in data[choice1][choice2][choice3]:
                                print("\t\t\t", i4)

                            choice4 = input("最后一层，按b返回，按q退出>>:")

                            # 退出第四层for
                            if choice4 == "b":
                                break
                            elif choice4 == "q":
                                exit_flag = True

                    # 退出第三层for
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True

            # 退出第二层for
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
                        

