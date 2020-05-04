# -*- encoding: utf-8 -*-
'''
@File    :   求H 小时内吃掉所有喵粮的最小速度 K.py
@Time    :   2020/03/11 12:04:24
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   求H 小时内吃掉所有喵粮的最小速度 K.py
'''

'''
题目描述
小招喵喜欢吃喵粮。这里有 N 堆喵粮，第 i 堆中有 p[i] 粒喵粮。喵主人离开了，将在 H 小时后回来。

小招喵可以决定她吃喵粮的速度 K （单位：粒/小时）。每个小时，她将会选择一堆喵粮，从中吃掉 K 粒。
如果这堆喵粮少于 K 粒，她将吃掉这堆的所有喵粮，然后这一小时内不会再吃更多的喵粮。  

小招喵喜欢慢慢吃，但仍然想在喵主人回来前吃掉所有的喵粮。

返回她可以在 H 小时内吃掉所有喵粮的最小速度 K（K 为整数）。

输入描述:
第一行输入为喵粮数组，以空格分隔的N个整数

第二行输入为H小时数
输出描述:
最小速度K
示例1
输入
3 6 7 11
8
输出
4
'''
# 代码一
# 二分法：最小速度：1 最大速度：粮的最大值
# 贪心  + 二分查找
# 理论最小进食速度： 所有喵粮求和 / 给定的小时数
# 理论最大进食速度：最大堆的喵粮数
# 在这两个之间二分查找最小实际可行进食速度即可
P=list(map(int,input().split()));
H=int(input());
def getK(P,H):
    def getHour(P,k):
        hour=0
        for i in P:
          # hour+=(i-1)//k+1 也是向下取整
            hour+=i//k if i%k==0 else i//k+1;
        return hour;
    l,r=sum(P)//H,max(P);
    while l<=r:
        mid=(l+r)>>1;
        if getHour(P,mid)<=H:
            r=mid-1;
        else:
            l=mid+1;
    return l
print(getK(P,H))

# 代码二
P=list(map(int,input().split()));
H=int(input());
def getK(P,H):
    def getHour(P,k):
        return sum([(i-1)//k+1 for i in P])
    total=sum(P);
    res=total//H;
    while getHour(P,res)>H:
        res+=1;
    return res
print(getK(P,H))