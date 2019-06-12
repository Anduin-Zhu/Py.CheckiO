# -*- coding:utf-8 -*-
__author__ = '朱永刚'

class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print('喝')

    def run(self):
        print('跑')

    def sleep(self):
        print('睡')


class Dog(Animal):

    def bark(self):
        print('狗在叫！！！')



class Cat(Animal):

    def catch_mouse(self):
        print('抓老鼠！！')


class XiaoTianQuan(Dog):

    # 重写bark方法
    def bark(self):
        print('哮天犬在叫')
        # 覆盖的方式重写
        super(XiaoTianQuan, self).bark()

    def fly(self):
        print('狗在飞！！！')



XiaoTianQuan().bark()

class demo:

    def __init__(self):
        self.__num1 = 1
        self.num2 = 2

    def __test(self):
        print('私有方法%d %d'%(self.__num1,self.num2))

    def test(self):
        print('公有方法1')


class demo1():

    def test(self):
        print('公有方法2')


class demo2(demo1,demo):
    pass

demo2().test()

print(demo2.__mro__)
