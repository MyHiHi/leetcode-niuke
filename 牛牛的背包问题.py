# -*- encoding: utf-8 -*-
'''
@File    :   牛牛的背包问题.py
@Time    :   2020/02/09 11:39:35
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
题目描述
牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。
输入描述:
输入包括两行
第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。
输出描述:
输出一个正整数, 表示牛牛一共有多少种零食放法。
示例1
输入
3 10
1 2 4
输出
8
说明
三种零食总体积小于10,于是每种零食有放入和不放入两种情况，一共有2*2*2 = 8种情况。
'''

# 代码一
import sys
lines = sys.stdin.readlines()
p = [line.strip() for line in lines]
n, w = list(map(int, p[0].split()))
v = list(map(int, p[1].split()))


def junkFood(w, v):
    if w <= 0:
        return 1
    if len(v) <= 0:
        return 1
    if sum(v) <= w:
        return 2**len(v)
    if v[0] <= w:
      # 放还是不放
        return junkFood(w-v[0], v[1:])+junkFood(w, v[1:])
      # 放不了
    else:
        return junkFood(w, v[1:])


print(junkFood(w, v))


# 代码二:
lines = sys.stdin.readlines()
p = [line.strip() for line in lines]
n, w = list(map(int, p[0].split()))
v = list(map(int, p[1].split()))
# 背包为空,也是一种情况
co = 1
'''
su:当前背包里的东西的总体积;
total:背包最大体积:w;
cur:当前选择的零食
'''


def junkFood(su, total, cur):
    if cur < n:
        if su > total:
            return
        # 不放
        junkFood(su, total, cur+1)
        p = v[cur]
        if su+p <= total:
            global co
            co += 1
            # 放
            junkFood(su+p, total, cur+1)


if sum(v) <= w:
    co = 2**len(v)
else:
    junkFood(0, w, 0)
print(co)


# 代码三
lines = sys.stdin.readlines()
p = [line.strip() for line in lines]
n, w = list(map(int, p[0].split()))
v = list(map(int, p[1].split()))
co = 0
v.sort()


def DFS(su, total, cur):
    if su > total:
        return
    global co
    co += 1
    for i in range(cur, n):
        if su+v[i] <= total:
            DFS(su+v[i], total, i+1)


if sum(v) <= w:
    co = 2**len(v)
else:
    DFS(0, w, 0)
print(co)
