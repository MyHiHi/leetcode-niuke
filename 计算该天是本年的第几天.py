# -*- encoding: utf-8 -*-
'''
@File    :   计算该天是本年的第几天.py
@Time    :   2020/03/05 10:12:55
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   计算该天是本年的第几天.py
'''

'''
题目描述

输入年、月、日，计算该天是本年的第几天。  
输入：  
包括三个整数年(1<=Y<=3000)、月(1<=M<=12)、日(1<=D<=31)。  
输出：  
输入可能有多组测试数据，对于每一组测试数据，  
输出一个整数，代表Input中的年、月、日对应本年的第几天。 

示例1 
输入
2000 5 1 
输出
122
'''
y,m,d=list(map(int,input().split()));
def isLeaf(y):
    if y%4!=0:return False;
    if y%100==0 and y%400!=0:return False;
    return True
def whatDay(y,m,d):
    mon=[31,28,31,30,31,30,31,31,30,31,30,31];
    if d>2:
        if isLeaf(y):
            mon[1]+=1;
    return sum(mon[:m-1])+d;
        
print(whatDay(y,m,d))