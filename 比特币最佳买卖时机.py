# -*- encoding: utf-8 -*-
'''
@File    :   比特币最佳买卖时机.py
@Time    :   2020/03/10 10:40:34
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   比特币最佳买卖时机.py
'''

'''
题目描述
给定一个正整数数组，它的第 i 个元素是比特币第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一次），
设计一个算法来计算你所能获取的最大利润。

注意你不能在买入比特币前卖出。

输入描述:
正整数数组，为以空格分隔的n个正整数
输出描述:
最大利润
示例1
输入
7 1 5 3 6 4
输出
5
'''
# 代码一：
bits=list(map(int,input().split()));
mi=10000;
profit=0;
for i in bits:
  # 获取最大利润
    profit=max(i-mi,profit);
  # 买入最低值
    mi=min(mi,i);
print(profit)

# 代码二:

mo=list(map(int,input().split()));
ma=0;
le=len(mo)
for i in range(le):
    nex=mo[i+1:];
    now=mo[i];
    maN=max(nex) if nex else 0;
    ma=maN-now if (maN-now)>ma else ma
print(ma)