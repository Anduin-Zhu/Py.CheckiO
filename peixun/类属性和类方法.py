# -*- coding:utf-8 -*-
__author__ = '朱永刚'
'''

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def print_count(self):

        print(Student.count)

    @staticmethod
    def jingtai_fangfa():
        pass


a = Student("xiaoming")
a.print_count()
b = Student("xiaoming")
b.print_count()'''

"""
设计一个 Game 类
属性：
定义一个 类属性 top_score 记录游戏的 历史最高分
定义一个 实例属性 player_name 记录 当前游戏的玩家姓名
方法：
静态方法 show_help 显示游戏帮助信息
类方法 show_top_score 显示历史最高分
实例方法 start_game 开始当前玩家的游戏
主程序步骤
1) 查看帮助信息
2) 查看历史最高分
3) 创建游戏对象，开始游戏
"""

class Game(object):

    top_score = 0

    @staticmethod
    def show_help():

        print('帮助信息请访问www.baidu.com')

    @classmethod
    def show_top_score(cls):

        print('当前最高分是%d!'%cls.top_score)

    def __init__(self,player_name):

        self.player_name = player_name

    def start_game(self):

        print('%s开始游戏。'%self.player_name)
        # 修改最高分
        Game.top_score = 999


if __name__ == '__main__':

    # 查看游戏帮助
    Game.show_help()
    # 查看最高分
    Game.show_top_score()
    # 创建游戏对象，开始游戏
    game = Game('小明')
    game.start_game()
    #游戏结束，查看最高分
    Game.show_top_score()