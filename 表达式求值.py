# -*- encoding: utf-8 -*-
'''
@File    :   表达式求值.py
@Time    :   2020/02/14 11:14:18
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   表达式求值.py
'''

'''
今天上课，老师教了小易怎么计算加法和乘法，乘法的优先级大于加法，但是如果一个运算加了括号，
那么它的优先级是最高的。例如：
1+2*3=7
1*(2+3)=5
1*2*3=6
(1+2)*3=9
现在小易希望你帮他计算给定3个数a，b，c，在它们中间添加"+"， "*"， "("， ")"符号，
能够获得的最大值。
输入描述:
一行三个数a，b，c (1 <= a, b, c <= 10)
输出描述:
能够获得的最大值
示例1
输入
1 2 3
输出
9
'''
# 代码一
nums=list(map(int,input().strip().split()));
def max1(a,b):
    return max(a*b,a+b);
def max2(*args):
    a,b,c=args
    return max(max1(max1(a,b),c),max1(a,max1(b,c)));
print(max2(*nums))

# 代码二
a, b, c = [int(x) for x in input().strip().split(" ")]
print(max([a+b+c, a*b*c, a+b*c, a*b+c, (a+b)*c, a*(b+c)]))