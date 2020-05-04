# -*- encoding: utf-8 -*-
'''
@File    :   字符串长度最大乘积.py
@Time    :   2020/03/04 10:52:18
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   字符串长度最大乘积.py
'''

'''
题目描述
已知一个字符串数组words，要求寻找其中两个没有重复字符的字符串，使得这两个字符串的长度乘积最大，输出这个最大的乘积。如：
words=["abcd","wxyh","defgh"], 其中不包含重复字符的两个字符串是"abcd"和"wxyh"，则输出16
words=["a","aa","aaa","aaaa"], 找不到满足要求的两个字符串，则输出0
输入描述:
Input:

["a","ab","abc","cd","bcd","abcd"]
输出描述:
Output:
4
'''
# 代码一
lis=eval(input());
le=len(lis);
ma=0
for i in range(le):
    k1=lis[i];
    l1=len(k1);
    for j in range(i+1,le):
        k2=lis[j];
        l2=len(k2);
        if not (set(k1) & set(k2)) and l1*l2>ma:
            ma=l1*l2;
print(ma)
    