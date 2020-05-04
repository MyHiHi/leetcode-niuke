# -*- encoding: utf-8 -*-
'''
@File    :   瞌睡.py
@Time    :   2020/02/11 11:36:59
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
题目描述
小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。你知道了小易对一堂课每分钟知识点的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，你可以叫醒他一次，这会使得他在接下来的k分钟内保持清醒。你需要选择一种方案最大化小易这堂课听到的知识点分值。
输入描述:
第一行 n, k (1 <= n, k <= 105) ，表示这堂课持续多少分钟，以及叫醒小易一次使他能够保持清醒的时间。
第二行 n 个数，a1, a2, ... , an(1 <= ai <= 104) 表示小易对每分钟知识点的感兴趣评分。
第三行 n 个数，t1, t2, ... , tn 表示每分钟小易是否清醒, 1表示清醒。
输出描述:
小易这堂课听到的知识点的最大兴趣值。
示例1
输入
6 3
1 3 5 2 5 4
1 1 0 1 0 0
输出
16
'''
# 代码一
# 最大兴趣值=清醒的固定值+叫醒小易一次的最大兴趣值

import sys
lines = sys.stdin.readlines()
lines = [line.strip() for line in lines]
n, k = list(map(int, lines[0].split()))
grades = list(map(int, lines[1].split()))
isWake = list(map(int, lines[2].split()))
su = 0
r = []
for i in range(n):
    a = grades[i]
    if isWake[i]:
        su += a
        # 0在r表示此刻不需要叫醒小易
        r += [0]
    else:
       # 非0 表示叫醒小易
        r += [a]
ma = 0
i = 0
while i < n:
    if r[i]:
        ma = max(ma, sum(r[i:min(i+k, n)]))
        if i+k > n:
            break
    i += 1
print(su+ma)
