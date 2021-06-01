# -*- coding: utf-8 -*-
# @Time    : 2021-06-01 11:37 a.m.
# @Author  : jiQi
# @FileName: menu.py
# @Software: PyCharm


import settings
from services import taxi_meter
from services import file_operator


class Menu:
    def __init__(self):
        self.menu = '菜单'

    def run(self):
        while True:
            meter = taxi_meter.Taxi_meter(starting_price=settings.STARTING_PRICE,
                                          starting_distance=settings.STARTING_DISTANCE,
                                          starting_unit_price=settings.STARTING_UNIT_PRICE,
                                          long_distance=settings.LONG_DISTANCE,
                                          long_unit_price=settings.LONG_UNIT_PRICE,
                                          extra=settings.EXTRA_MONEY)
            print('')
            print('==========出租车计价系统==========')
            print('请输入数字选择以下功能')
            print('1. 手动输入里程返回价格')
            print('2. 自动模拟计价器')
            print('3. 查看记录')
            print('0. 退出系统')
            option = int(input())
            if option == 1:
                while True:
                    print('')
                    print('========手动输入里程返回价格=========')
                    print('请输入里程数，输入-1返回主菜单：')
                    dis = float(input())
                    if dis == -1:
                        break

                    print('对应的价格为' + str('%.2f' % meter.distance_to_price(dis)))
                    file_operator.append('里程数：' + str('%.2f' % dis) + '  ' + '价格：' +
                                         str('%.2f' % meter.distance_to_price(dis)) + '  （手动输入里程）')
            elif option == 2:
                while True:
                    print('')
                    print('==========自动模拟计价器==========')
                    print('请输入模拟速度（单位：km/s），输入-1返回主菜单：')
                    speed = float(input())
                    if speed == -1:
                        break
                    dis, price = meter.uniform_speed(speed)
                    file_operator.append('里程数：' + str('%.2f' % dis) + '  ' + '价格：' +
                                         str('%.2f' % price) + '  （自动模拟计价）')
            elif option == 3:
                print('')
                print('===========查看记录============')
                records = file_operator.get_content()
                for i in records:
                    print(i)
            elif option == 0:
                print('退出系统')
                exit(0)
