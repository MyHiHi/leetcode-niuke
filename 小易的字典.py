# -*- encoding: utf-8 -*-
'''
@File    :   小易的字典.py
@Time    :   2020/02/16 12:54:30
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   小易的字典.py
'''

'''
题目描述
小易在学校中学习了关于字符串的理论, 于是他基于此完成了一个字典的项目。

小易的这个字典很奇特, 字典内的每个单词都包含n个'a'和m个'z', 并且所有单词按照字典序排列。

小易现在希望你能帮他找出第k个单词是什么。

输入描述:
输入包括一行三个整数n, m, k(1 <= n, m <= 100, 1 <= k <= 109), 以空格分割。

输出描述:
输出第k个字典中的字符串，如果无解，输出-1。
示例1
输入
2 2 6
输出
zzaa
说明
字典中的字符串依次为aazz azaz azza zaaz zaza zzaa
'''
'''

//思路，利用字典排序的规律进行选择：
构造一个排列计算函数，计算m+n长度的字符串中，m个z的排列共有多少种可能性C(m,m+n)
首先固定第一位为a，
假如在剩下的m+n-1个位置中选择m个z的位置的排列数小于选取序号k，则说明不在这
个排列集合中，此时，可以确定，序号k的数在剩下的排列数中，则第一位序号为z，此时m=m-1，k=k-C(m,m+n-1)
​假如选取序号k<C(m,m+n-1)，则说明该数在首字母为a的排列数中，此时n=n-1，
继续在剩下的字符中按照这种规则进行判断序号k和排列数的关系，直到m和n一方变为0未知
最后，将剩下的m或n补全即可
'''
n,m,k=list(map(int,input().strip().split()));
def C(n,m):
    ret=1;
    for i in range(n+1,n+m+1):
        ret*=i
    for i in range(1,m+1):
        ret//=i;
    return ret;
ans="";
if C(n,m)<k:
    ans+="-1"
else:
    while n and m:
        t=C(n-1,m);
        if t<k:
            k-=t;
            ans+='z'
            m-=1;
        else:
            ans+='a'
            n-=1;
    ans+='a'*n;
    ans+='z'*m;
print(ans)
            
        