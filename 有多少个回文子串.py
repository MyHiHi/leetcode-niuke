# -*- encoding: utf-8 -*-
'''
@File    :   有多少个回文子串.py
@Time    :   2020/03/01 11:46:10
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   有多少个回文子串.py
'''

'''
题目描述
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
("回文串”是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。)
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
可用C++,Java,C#实现相关代码逻辑
输入描述:
输入一个字符串S 例如“aabcb”(1 <= |S| <= 50), |S|表示字符串S的长度。
输出描述:
符合条件的字符串有"a","a","aa","b","c","b","bcb"

所以答案:7
示例1
输入
aabcb
输出
7
'''
S=input().strip();
le=len(S);
res=0
def isH(i,j,S):
    global res
    while i>=0 and j<le and S[i]==S[j]:
        i-=1;
        j+=1;
        res+=1;
        
for i in range(le):
    isH(i,i+1,S)
    isH(i,i,S)
print(res)
    