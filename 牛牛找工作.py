# -*- encoding: utf-8 -*-
'''
@File    :   牛牛找工作.py
@Time    :   2020/02/02 18:36:54
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

# 题目描述
# 为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在
# 难度不超过自身能力值的情况下，牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，
# 牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，
# 于是他只好把这个任务交给了你。
# 输入描述:
# 每个输入包含一个测试用例。
# 每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙
# 伴的数量M(M<=100000)。
# 接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和
# 报酬Pi(Pi<=1000000000)。
# 接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
# 保证不存在两项工作的报酬相同。
# 输出描述:
# 对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。
# 一个工作可以被多个人选择。
# 示例1

# 输入
# 3 3 
# 1 100 
# 10 1000 
# 1000000000 1001 
# 9 10 1000000000

# 输出
# 100 
# 1000 
# 1001


import sys
lines = sys.stdin.readlines()
# windows+z+enter  : 才结束readlines()
lines = [l.strip().split() for l in lines if l.strip()]
N, M = map(int, lines[0])
job_money = {}
for i in lines[1:-1]:
    a, b = map(int, i)
    job_money[a] = b
c = map(int, lines[-1])
# index 记录控制台输入的M个伙伴的先后顺序
index = []
for v in c:
    index += [v]
    job_money[v] = 0 if v not in job_money else job_money[v]
# 按照难度从大到小排序，
# 为了后面难度总能得到前面小难度的最大报酬
job_money = sorted(job_money.items(), key=lambda x: x[0])
mx = 0
res = {}
# job_money 
# key: 难度
# value:最大报酬
for i, k in job_money:
    # mx总比较难度i前面的最大报酬
    mx = max(mx, k)
    res[i] = mx
# 按照顺序输出M个伙伴对应的最大报酬
for v in index:
    print(res[v])
