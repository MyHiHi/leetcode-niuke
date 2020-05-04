# -*- encoding: utf-8 -*-
'''
@File    :   1137. 第 N 个泰波那契数.py
@Time    :   2020/02/25 11:10:21
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   1137. 第 N 个泰波那契数.py
'''

'''
1137. 第 N 个泰波那契数
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

 

示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
示例 2：

输入：n = 25
输出：1389537
'''
# 代码一
class Solution:
    def tribonacci(self, n: int) -> int:
        def r(a,b,c,n):
            if n>2:
                return r(a+b+c,a,b,n-1);
            return a
        if n==0:
            return 0;
        elif n==1 or n==2:
            return 1
        
        return r(1,1,0,n)
      
# 代码二
class Solution:
    myM={}
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0;
        elif n==1 or n==2:
            return 1;
        if n not in self.myM:
            self.myM[n]=self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3);
            return self.myM[n];
        else:return self.myM[n]
        