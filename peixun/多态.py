# -*- coding:utf-8 -*-
__author__ = '朱永刚'

class Dog(object):

    def __init__(self,name):

        self.name = name

    def game(self):

        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianQuan(Dog):

    def game(self):

        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):

    def __init__(self,name):

        self.name = name

    def game_with_dog(self,dog):

        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
        # 让狗玩耍
        dog.game()

wangcai = Dog('旺财')
xiaotianquan = XiaoTianQuan('哮天犬')
xiaoming = Person('小明')
xiaoming.game_with_dog(wangcai)
xiaoming.game_with_dog(xiaotianquan)