# -*- encoding: utf-8 -*-
'''
@File    :   countPrimes.py
@Time    :   2020/01/07 10:25:36
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:return 0
        # 0：是质数
        # 1：不是质数
        sign=[0]*n;
        co=0;
        for i in range(2,n):
            if not sign[i]:
                co+=1;
                for k in range(i*2,n,i):
                  # 把不是质数的排除掉
                    sign[k]=1;
        return co;