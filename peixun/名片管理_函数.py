# -*- coding:utf-8 -*-
__author__ = '朱永刚'
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
#定义一个列表来存放卡片
card_list = []


def show_meun():
    """
    主页面菜单显示
    :return:
    """
    print("*"*30 + "\n"
            "欢迎使用【名片管理系统】V1.0\n"
            "1. 新建名片\n"
            "2. 显示全部\n"
            "3. 查询名片\n"
            "0. 退出系统\n" + "*" * 30 )


def new_card():
    """
    新增名片
    :return:
    """
    while True:
        name_input = input("请输入你的姓名：")
        tel_input = input("请输入你的电话：")
        qq_input = input("请输入你的QQ：")
        mail_input = input("请输入你的邮件地址：")
        card_dict = {"姓名": name_input,
                     "电话": tel_input,
                     "QQ": qq_input,
                     "邮件": mail_input}
        card_list.append(card_dict)
        if input("请问是否继续添加名片？\n"
                 "1. 按 1 继续添加\n"
                 "2. 按任意键回到主菜单\n") == "1":
            continue
        else:
            break


def print_card(d):
    """
    打印名片
    :param d:
    :return:
    """
    print("姓名：%s\n"
           "电话：%s\n"
           "QQ:%s\n"
           "邮件:%s\n"
           % (d["姓名"], d["电话"], d["QQ"], d["邮件"]))


def show_card():
    """
    显示全部名片
    :return:
    """
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请使用新增功能添加名片！\n")
        return
    for d in card_list:
        print_card(d)


def search_card():
    """
    查询名片
    :return:
    """
    name_chaxun = input("请输入要查询的姓名：")
    for d in card_list:
        if d["姓名"] == name_chaxun:
            print_card(d)
            #查询到名片可以进行功能选择，修改或删除
            deal_card(d)
            break
    else:
        print("抱歉，没有找到姓名为%s的人"%d["姓名"])


def deal_card(find_dict):
    """
    处理名片功能
    :param find_dict:
    :return:
    """
    name_caozuo = input("请选择要进行的操作：\n"
                        "1. 修改名片\n"
                        "2. 删除名片\n"
                        "3. 按任意键回到主菜单\n")
    if name_caozuo == "1":
        find_dict["姓名"] = input("请输入你的姓名：")
        find_dict["电话"] = input("请输入你的电话：")
        find_dict["QQ"] = input("请输入你的QQ：")
        find_dict["邮件"] = input("请输入你的邮件地址：")
    elif name_caozuo == "2":
        card_list.remove(find_dict)


if __name__ == '__main__':
    while True:
        show_meun()
        user_input = input()
        #选择 1 新建名片
        if user_input == "1":
            new_card()
        #选择 2 显示全部名片
        elif user_input == "2":
            show_card()
        #选择 3 查询名片
        elif user_input == "3":
            search_card()
        #选择 0 退出
        elif user_input == "0":
            break
        #选择其他返回主界面
        else:
            continue

