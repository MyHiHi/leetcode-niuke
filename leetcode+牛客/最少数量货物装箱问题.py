# -*- encoding: utf-8 -*-
'''
@File    :   最少数量货物装箱问题.py
@Time    :   2020/02/29 12:26:39
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   最少数量货物装箱问题.py
'''

'''
题目描述
有重量分别为3，5，7公斤的三种货物，和一个载重量为X公斤的箱子（不考虑体积等其它因素，只计算重量）
需要向箱子内装满X公斤的货物，要求使用的货物个数尽可能少（三种货物数量无限）

输入描述:
输入箱子载重量X(1 <= X <= 10000)，一个整数。
输出描述:
如果无法装满，输出 -1。
如果可以装满，输出使用货物的总个数。
示例1
输入
4
输出
-1
说明
无法装满
'''
# 代码一
X=int(input())
def r(X):
    res=0;
    for i in range(X):
        for j in range(X):
            k=3*i+j*5;
            if (X-k<0):break;
            if (X-k)%7==0:
                c=(X-k)//7;
                res+=i+j+c;
                return res;
    return -1

print(r(X))

# 代码二
X=int(input())
ma=float('inf')
dp=[ma for _ in range(8)];
dp[3],dp[5],dp[6],dp[7]=1,1,2,1

if (X<8):
    res=dp[X];
else:
    for i in range(8,X+1):
        dp+=[min(dp[i-3],dp[i-5],dp[i-7])+1];
    res=dp[X]
print(-1 if  res>=ma else res)
