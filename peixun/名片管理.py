# -*- coding:utf-8 -*-
__author__ = '朱永刚'

'''
i = 1
while i <= 5:
    print("*" * i)
    i += 1

'''
'''
#九九乘法表
row = 1#行

while row <= 9:
    col = 1
    while col <= row:
        print('%d*%d=%d'%(col,row,row*col),end='\t')
        col += 1
    print('\n')
    row += 1
'''
'''
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a + b
        n += 1
def yangHui():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]
        print(L)

n = 0
result = []
for i in yangHui():
    print(i)
    result.append(i)
    n += 1
    if n == 10:
        break

def person(name,*,city,job):
    print(name,city,job)

l = (1,2,3,4,5,6)
person('zyg',city='beijng',job='fuwuyuan')
'''
'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


def fact_iter(num,product=1):
    if num == 1:
        return product
    return fact_iter(num - 1,num * product)

print(fact_iter(5))'''
"""
名片管理系统

 1. 程序启动，显示名片管理系统欢迎界面，并显示功能菜单
**************************************************
欢迎使用【名片管理系统】V1.0
1. 新建名片
2. 显示全部
3. 查询名片
0. 退出系统
**************************************************
* 2. 用户用数字选择不同的功能
* 3. 根据功能选择，执行不同的功能
* 4. 用户名片需要记录用户的 **姓名**、**电话**、**QQ**、**邮件**
* 5. 如果查询到指定的名片，用户可以选择 **修改** 或者 **删除** 名片
"""
# 定义一个列表来存储名片
card_list = []
#程序启动，显示名片管理系统欢迎界面，并显示功能菜单
while True:
    print(("*"*30 +
           "\n欢迎使用【名片管理系统】V1.0\n"
            "1. 新建名片\n"
            "2. 显示全部\n"
            "3. 查询名片\n"
            "0. 退出系统\n"
            + "*" * 30 ))
    #获取用户输入，让用户选择功能
    user_input_str = input()
    #如果选择 1 则新建名片
    if user_input_str == '1':
        while True:
            name_input = input("请输入你的姓名：")
            tel_input = input("请输入你的电话：")
            qq_input = input("请输入你的QQ：")
            mail_input = input("请输入你的邮件地址：")
            d = {"姓名":name_input,"电话":tel_input,"QQ":qq_input,"邮件":mail_input}
            card_list.append(d)
            if input("请问是否继续添加名片？\n1. 按 1 继续添加\n2. 按任意键回到主菜单\n") == "1":
                continue
            else:
                break

    #如果选择 2 则显示全部名片
    elif user_input_str == '2':
        for d in card_list:
            print(("姓名：%s\n"
                   "电话：%s\n"
                   "QQ:%s\n"
                   "邮件:%s\n"
                   %(d["姓名"],d["电话"],d["QQ"],d["邮件"])))
    #如果选择 3 则查询名片，根据姓名查询
    elif user_input_str == '3':
        name_chaxun = input("请输入要查询的姓名：")
        for d in card_list:
            if d["姓名"] == name_chaxun:
                print("姓名：%s\n电话：%s\nQQ:%s\n邮件:%s\n"%(d["姓名"],d["电话"],d["QQ"],d["邮件"]))
                #查询到名片可以进行功能选择，修改或删除
                name_caozuo = input("请选择要进行的操作：\n1. 修改名片\n2. 删除名片\n3. 按任意键回到主菜单\n")
                if name_caozuo == "1":
                    d["电话"] = input("请输入你的电话：")
                    d["QQ"] = input("请输入你的QQ：")
                    d["邮件"] = input("请输入你的邮件地址：")
                elif name_caozuo == "2":
                    card_list.remove(d)
                else:
                    break
                break
        else:
            print("姓名输入错误，请重新输入。")

    #如果选择 0 则退出系统
    elif user_input_str == '0':
        break
    else:
        print("输入错误，请重新输入")