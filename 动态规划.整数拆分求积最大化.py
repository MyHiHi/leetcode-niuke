# -*- encoding: utf-8 -*-
'''
@File    :   动态规划.整数拆分求积最大化.py
@Time    :   2020/04/25 12:42:16
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   动态规划.整数拆分求积最大化.py
'''
'''
整数拆分
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。
返回你可以获得的最大乘积。
示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

思路：
最优子结构：通过求子问题的最优解，可以求原问题的最优解。
方法：动态规划，自底向上
内层循环就是为了找到memo[i]的最大值
i是总和，把i分割成j和(i - j)，
循环比较j * (i - j)、j * memo[i - j]和memo[i]三者的大小关系
其中memo[i - j]是将i-j继续分割的最大值，而memo[i]是之前一次内层循环求出的memo[i]
由于i- j < i, memo[i- j]一定已经计算过
'''

def look(n):
    p = [0 for i in range(n+1)]
    p[0] = 1
    for i in range(n+1):
        for j in range(1, i):
            p[i] = max(p[i], j*p[i-j], j*(i-j))
    return p[n]


print(look(57))