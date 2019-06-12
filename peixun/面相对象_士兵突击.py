# -*- coding:utf-8 -*-
__author__ = '朱永刚'

"""
1.士兵 许三多 有一把 AK47
2.士兵 可以 开火
3.枪 能够 发射 子弹
4.枪 装填 装填子弹 —— 增加子弹数量
"""
class Gun:

    def __init__(self,model):

        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    # 发射子弹
    def shoot_bullet(self):

        # 判断是否还有子弹
        if self.bullet_count <= 0:
            print("没子弹了！！！")
            return
        # 发射一颗子弹
        self.bullet_count -= 1
        print("%s发射子弹,余弹[%d]。"%(self.model,self.bullet_count))

    # 装填子弹
    def add_bullet(self,count):

        self.bullet_count += count


class Soldier:

    def __init__(self,name,gun):

        self.gun = gun
        self.name = name

    def fire(self):

        # 装子弹
        self.gun.add_bullet(30)
        # 发射子弹
        self.gun.shoot_bullet()


# 创建枪对象
ak47 = Gun("AK47")
# 创建士兵许三多
xuSanDuo = Soldier("许三多",ak47)
xuSanDuo.fire()