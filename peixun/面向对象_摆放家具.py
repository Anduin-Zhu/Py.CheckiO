# -*- coding:utf-8 -*-
__author__ = '朱永刚'

'''
class Person:

    def __init__(self,name,weight):

        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字叫 %s 体重 %.2f 公斤" % (self.name,self.weight)

    def run(self):
        """
        跑步
        :return:
        """

        print("%s 爱跑步，跑步会减肥" % self.name)
        self.weight -= 0.5

    def eat(self):
        """
        吃东西
        :return:
        """

        print("%s 是吃货，越吃越胖" % self.name)
        self.weight += 1

xiaoming = Person("小明",75)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

xiaomei = Person("小美",45)
xiaomei.eat()
xiaomei.run()
print(xiaomei)'''

class HouseItem:

    def __init__(self,name,area):

        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地面积 %.2f" % (self.name, self.area)

class House:

    def __init__(self,house_type,area):

        self.huose_type = house_type
        self.area = area
        #定义一个 剩余面积的属性，初始值和总面积相等
        self.free_area = area
        #定义一个空的列表用于存放家具
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s" %
                (self.huose_type,self.area,self.free_area,self.item_list))

    def add_item(self,item):

        print("要添加 %s" % item)
        #判断家具面积是否大于剩余面积
        if item.area > self.free_area:
            print("%s 的面积太大，不能添加到房子中" % item.name)
            return
        self.item_list.append(item.name)
        #计算剩余面积
        self.free_area -= item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bed)
print(chest)
print(table)

my_home = House("三室一厅",120)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)