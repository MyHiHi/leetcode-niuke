# -*- encoding: utf-8 -*-
'''
@File    :   塔.py
@Time    :   2020/02/15 15:23:24
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   塔.py
'''

'''
题目描述
小易有一些立方体，每个立方体的边长为1，他用这些立方体搭了一些塔。
现在小易定义：这些塔的不稳定值为它们之中最高的塔与最低的塔的高度差。
小易想让这些塔尽量稳定，所以他进行了如下操作：每次从某座塔上取下一块立方体，并把它放到另一座塔上。
注意，小易不会把立方体放到它原本的那座塔上，因为他认为这样毫无意义。
现在小易想要知道，他进行了不超过k次操作之后，不稳定值最小是多少。
输入描述:
第一行两个数n,k (1 <= n <= 100, 0 <= k <= 1000)表示塔的数量以及最多操作的次数。
第二行n个数，ai(1 <= ai <= 104)表示第i座塔的初始高度。
输出描述:
第一行两个数s, m，表示最小的不稳定值和操作次数(m <= k)
接下来m行，每行两个数x,y表示从第x座塔上取下一块立方体放到第y座塔上。
示例1
输入
3 2
5 8 5
输出
0 2
2 1
2 3
'''
n, k = list(map(int, input().strip().split()))
tower = []
for i, v in enumerate(list(map(int, input().strip().split()))):
    tower += [[v, i+1]]
# 按塔高排序
tower = sorted(tower, key=lambda x: x[0])
res = []
t = 0
while tower[-1][0]-tower[0][0] > 0 and k > 0:
    tower[-1][0] -= 1
    tower[0][0] += 1
    res += [str(tower[-1][1])+" "+str(tower[0][1])]
    tower = sorted(tower, key=lambda x: x[0])
    t += 1
    k -= 1
res = [str(tower[-1][0]-tower[0][0])+" "+str(t)]+res
for k in res:
    print(k)
