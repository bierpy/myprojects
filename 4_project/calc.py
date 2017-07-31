#!/usr/bin/env python
# -*- coding: utf-8 -*-

#计算器开发
#实现加减乘除及拓号优先级解析
#用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) 等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式，运算后得出结果，结果必须与真实的计算器所得出的结果一致

#思路：
#通过正则匹配到最里层，然后得到最里层的值，然后不断往外进行匹配括号。
#比如：(((2+3)*6)-5) 这个表达式
#先通过正则匹配到最里层的括号(2+3)，计算得到(2+3)的值，然后再匹配到(5*6)这一层，然后值计算值，以此类推



import re

# 处理负数的问题
def deal_minus_issue (calc_list):
    # 把列表里重新得到的包含*/的表达式重新添加到这个列表里面，如果表达式后面是*/结尾就需要这样子处理
    new_calc_list = []
    # 如果他的index和所在的项在计算的列表里面
    for index,item in enumerate(calc_list):
        # 让所在的项去掉空格后，判断如是以*结尾或者以/结尾的进行处理
        if item.strip().endswith("*") or item.strip().endswith("/"):
            # 得到新的计算的两个项的值加新的计算值new_calc_list列表里面，如['2*5/', '3 ']这两个列表值的处理，要-处理
            new_calc_list.append("%s-%s" %(calc_list[index],calc_list[index+1]))
        elif ("*" or "/") in item: # 列表里面如果包含*或者/的表达式，让他追加到new_calc_list
            new_calc_list.append(item)
    print("new_calc_list:",new_calc_list)
    return new_calc_list # 返回给calc_list


#定义计算乘除的的函数
def mutilpy_and_dividend(formula):
    print("运算：",formula)
    # 以+-为分隔符，把*/找出来
    calc_list = re.split("[+-]",formula)
    calc_list = deal_minus_issue(calc_list)
    print(calc_list)

    # 然后再开始运算表达式的结果
    for item in calc_list:
        # 得到表达式的数字列表
        sub_calc_list = re.split("[*/]",item)
        #得到*/的运算符列表
        sub_operator_list = re.findall("[*/]",item)
        print(sub_calc_list,sub_operator_list)

        sub_res = None # 假设运算的结果为None
        #index，i分别是数字的索引和数字
        for index,i in enumerate(sub_calc_list):
            if sub_res: #这不是第一次循环
                #得到*/运算符，然后再进行判断
                if sub_operator_list[index-1] == "*":
                    sub_res *= float(i)
                else:
                    sub_res /= float(i)

            else:
                sub_res = float(i)  # float(i)代表每一个数字

        print("\033[31;1m [%s]=%s\033[0m" %(item,sub_res)) #item 是表达式，sub_res是表达式的结果
        #把表达式的结果替换到item里面，如：(9-2*5/-3 + 7 /3*99/4*2998 +10 * 568/14 ) 每个表达式就是一个item
        formula = formula.replace(item,str(sub_res))


    print("\033[32;1m 结果：\033[0m" ,formula)  #得到*/的结果，并放到原列表中
    #return formula

    #去掉重复的+-
    new_remove_list = []
    formula = formula.replace("++", "+")
    formula = formula.replace("+-", "-")
    formula = formula.replace("-+", "-")
    formula = formula.replace("--", "+")
    formula = formula.replace("- -", "+")
    new_remove_list.append(formula)
    print(new_remove_list)   #最终计算这个表达式的值

    #计算+-的结果
    for item2 in new_remove_list:
        # 得到表达式的数字列表
        shuzi_list = re.split("[+-]",item2)
        #得到+-的运算符列表
        add_jian_list = re.findall("[+-]",item2)
        print(shuzi_list,add_jian_list)

        sub_res2 = None # 假设运算的结果为None
        for index,i in enumerate(shuzi_list):
            if sub_res2: #这不是第一次循环
                if add_jian_list[index-1] == "+":
                    sub_res2 += float(i)
                else:
                    sub_res2 -= float(i)

            else:
                sub_res2 = float(i)

        print("\033[32;1m 最终结果:[%s]=%s\033[0m" % (item2, sub_res2))

def calc(formula):
    parentheses_flag = True  # 定义括号的标签，没有括号程序就为设置为false，开始让它是有括号
    while parentheses_flag:
        #匹配括号,让匹配的值里面不包含括号,括号里面不包含括号的里面的值的一个或者多个
        m = re.search("\([^()]+\)",formula)
        if m:
            print(m.group())
            #开始计算
            sub_formula = m.group().strip("()") #去掉括号，得到表达式
            sub_res = mutilpy_and_dividend(sub_formula)  # 把表达式传给计算函数去处理

        break

if __name__ == "__main__":
    #formula = "1 - 2 * ( (60-30 * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2)+(-40/5) )"
    formula = "1 - 2 * ( (60-30 * (9-2*5/-3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2)+(-40/5) )"
    res = calc(formula)


