# -*- encoding: utf-8 -*-
'''
@File    :   python多线程测试.py
@Time    :   2020/03/05 22:59:35
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   python多线程测试.py
'''


import threading
import time

lock = threading.Lock()
# COUNT = 0
# MOD = 3

# 运行报错
# class printChar(threading.Thread):
#     global COUNT

#     def __init__(self, threadIdentify, name):
#         threading.Thread.__init__(self)
#         self.threadIdentify = threadIdentify
#         self.name = name

#     def run(self):
#         i = 0
#         while i < 2:
#             lock.acquire()
#             try:
#                 print(">>> ", self.name, end='')
#                 if COUNT % MOD == self.threadIdentify:
#                     print(self.name, end='')
#                     COUNT += 1
#                     i += 1
#             except:
#                 pass
#             finally:
#                 lock.release()


# a = printChar(0, 'A')
# b = printChar(1, "B")
# c = printChar(2, 'C')
# a.start()
# b.start()
# c.start()

timer = 0


class SleepSort(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):

        # lock.acquire()
        time.sleep(self.num)
        print(': ', self.num)
        # lock.release()


arr = [1, 5, 4, 3, 2, 1, 3]
come = [SleepSort(n) for n in arr]
for c in come:
    c.start()
# [c.start() for c in come]
# [ i.join() for i in come]
