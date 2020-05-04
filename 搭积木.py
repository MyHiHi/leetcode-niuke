# -*- encoding: utf-8 -*-
'''
@File    :   搭积木.py
@Time    :   2020/02/19 15:56:07
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   搭积木.py
'''

'''
题目描述
小明有一袋子长方形的积木，如果一个积木A的长和宽都不大于另外一个积木B的长和宽，则积木A可以搭在积木B的上面。好奇的小明特别想知道这一袋子积木最多可以搭多少层，你能帮他想想办法吗？
定义每一个长方形的长L和宽W都为正整数，并且1 <= W <= L <= INT_MAX, 袋子里面长方形的个数为N, 并且 1 <= N <= 1000000.
假如袋子里共有5个积木分别为 (2, 2), (2, 4), (3, 3), (2, 5), (4, 5), 则不难判断这些积木最多可以搭成4层, 因为(2, 2) < (2, 4) < (2, 5) < (4, 5)。
输入描述:
第一行为积木的总个数 N

之后一共有N行，分别对应于每一个积木的宽W和长L
输出描述:
输出总共可以搭的层数
示例1
输入
5
2 2
2 4
3 3
2 5
4 5
输出
4
'''
from bisect import bisect
N=int(input());
bricks=[];
for i in range(N):
    w,l=map(int,input().split())
    bricks.append((w,l))
# 先按宽排序 后按长排序
# 1：先对宽排序 2：长度就等于是求最长非递减子序列的长度
bricks=sorted(bricks);
# res存储有序的长度
res=[];
for i in range(N):
    v=bricks[i][1];
    if not res:
        res.append(v)
    elif v>=res[-1]:
        res.append(v)
    else:
#  res宽度< bricks[i]的，所以 积木bricks[i]的宽度 > res[index]宽度，
#  and  bricks[i]的长度 >= dp[index],在堆积木情况下，当然是优先选择宽度和长度更大的积木。     
        index=bisect(res,v)
     #   index=lower_bin(res,v);
        res[index]=v;
print(len(res))