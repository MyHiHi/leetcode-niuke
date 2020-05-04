# -*- encoding: utf-8 -*-
'''
@File    :   求连续子数组的最大和.py
@Time    :   2020/03/03 09:42:16
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   求连续子数组的最大和.py
'''

'''
题目描述
一个非空整数数组，选择其中的两个位置，使得两个位置之间的数和最大。
如果最大的和为正数，则输出这个数；如果最大的和为负数或0，则输出0
输入描述:
3,-5,7,-2,8
输出描述:
13

'''
# 代码一
num=list( map(int,input().strip().split(',')));
maxn,n=0,0;
for i in num:
    k=n+i;
    n=k if k>0 else 0;
    maxn=max(maxn,n);
print(maxn)

# 代码二
num=list( map(int,input().strip().split(',')));
su=0;
maxn=0;
for i in num:
    su+=i;
    su = su if su>0 else 0;
    maxn=max(maxn,su);
print(maxn)
    
# 代码三
# 最大子段和问题
# lis记录 num[:idx+1] 的最大字段和
num=list( map(int,input().strip().split(',')));
lis=[0];
t=0
for i in num:
    t=max(0,t)+i;
    lis+=[t];
print(max(lis))
    