#!/usr/bin/env python
# -*- coding: utf-8 -*-
#学生信息查询

def staff_query():
    staff_dic = {}
    f = open('stu_info.txt')
    for line in f.readlines():
        #把读进来的每一行切成列存放到对应的字段里面
        stu_id, stu_name, mail, company, title, phone = line.split()
        #把每一行内容放到字典里面,stu_id是key，后面是values
        staff_dic[stu_id] = [stu_name, mail, company, title, phone]

    while True:
        query = input('\033[32;1m请输入查询的字符串: \033[0m').strip()
        if len(query) < 3:
            print('您必须输入至少3个字母才能查询！!')
            continue

        # 记录数目
        match_counter = 0
        for k, v in staff_dic.items():
            # 得到key里面的位置,首先查找k部分的内容，然后在查找v部分的内容
            index = k.find(query)
            # find()函数不包含里面的内容就等于-1
            if index != -1:
                # print k,v
                # print(k[:index])  # 得到k的长度，从列表头开始截取该长度的值
                # print(k[index + len(query):])  # 从index的长度+query的长度开始截取列表到末尾的值
                print(k[:index] + '\033[32;1m%s\033[0m' % query + k[index + len(query):], v)

                match_counter += 1
            else:
                # 把v列表变成字符串，查找v部分的内容
                str_v = '\t'.join(v)
                index = str_v.find(query)
                if index != -1:
                    # print k,v
                    print(k, str_v[:index] + '\033[32;1m%s\033[0m' % query + str_v[index + len(query):])
                    match_counter += 1

        print('Matched \033[31;1m%s\033[0m records!' % match_counter)


if __name__ == '__main__':
    staff_query()
