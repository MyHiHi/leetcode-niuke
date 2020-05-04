# -*- encoding: utf-8 -*-
'''
@File    :   1029. 两地调度.py
@Time    :   2020/02/16 10:31:28
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   1029. 两地调度.py
'''

'''
公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。

返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。

 

示例：

输入：[[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去 A 市，费用为 10。
第二个人去 A 市，费用为 30。
第三个人去 B 市，费用为 50。
第四个人去 B 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
'''
'''
思路:
先安排2N人全部到B，然后安排其中N人到A，这产生的额外开销为A_price-B_price,只要这开销最小就可以
所以先对数组按照
'''


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        n = len(costs)//2
        cost = 0
        for i in range(n):
            cost += costs[i][0]+costs[i+n][1]
        return cost
