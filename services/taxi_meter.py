# -*- coding: utf-8 -*-
# @Time    : 2021-06-01 11:01 a.m.
# @Author  : jiQi
# @FileName: taxi_meter.py
# @Software: PyCharm
import time


class Taxi_meter:
    def __init__(self, starting_price: float, starting_distance: float, starting_unit_price: float,
                 long_distance: float, long_unit_price: float, extra: float):
        self.starting_price = starting_price
        self.starting_distance = starting_distance
        self.starting_unit_price = starting_unit_price
        self.long_distance = long_distance
        self.long_unit_price = long_unit_price
        self.extra = extra

    # 输入里程数，输出价格
    def distance_to_price(self, distance: float) -> float:
        # 起步价
        if self.starting_distance > distance >= 0:
            return self.starting_price + self.extra
        # 起步里程计价
        elif self.long_distance > distance >= self.starting_distance:
            return self.starting_price + (distance - self.starting_distance) * self.starting_unit_price + self.extra
        # 远距离计价
        elif distance >= self.long_distance:
            return self.starting_price + (self.long_distance - self.starting_distance) * self.starting_unit_price + \
                   (distance - self.long_distance) * self.long_unit_price + self.extra
        else:
            print("不合理的里程输入，返回计价-1")
            return -1

    # 假设匀速行驶10秒，模拟计价，输入为每秒的公里数
    def uniform_speed(self, km_per_sec: float) -> [float, float]:
        if km_per_sec > 0:
            distance = 0
            for i in range(10):
                time.sleep(1)
                distance += km_per_sec
                print('===========模拟计价器===========')
                print('当前里程数为：' + str(distance))
                print('当前价格为： ' + str('%.2f' % self.distance_to_price(distance)))
                print('')
            return distance, self.distance_to_price(distance)
        else:
            print('不合理的速度，返回计价-1')
            return -1, -1
