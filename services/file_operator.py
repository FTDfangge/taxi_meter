# -*- coding: utf-8 -*-
# @Time    : 2021-06-01 2:27 p.m.
# @Author  : jiQi
# @FileName: file_operator.py
# @Software: PyCharm

import time
from typing import List


def append(content: str) -> None:
    with open('record.txt', 'a', encoding='utf-8') as record:
        record.write(content+' 时间：' + time.asctime(time.localtime()) + '\n')
    record.close()


def get_content() -> List[str]:
    try:
        with open('record.txt', 'r', encoding='utf-8') as record:
            return record.readlines()
    except:
        print("No such file")
