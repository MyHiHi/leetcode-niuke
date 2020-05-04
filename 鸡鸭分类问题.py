# -*- encoding: utf-8 -*-
'''
@File    :   鸡鸭分类问题.py
@Time    :   2020/03/09 12:27:07
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   鸡鸭分类问题.py
'''

'''
题目描述
农场有n只鸡鸭排为一个队伍，鸡用“C”表示，鸭用“D”表示。
当鸡鸭挨着时会产生矛盾。需要对所排的队伍进行调整，使鸡鸭各在一边。
每次调整只能让相邻的鸡和鸭交换位置，现在需要尽快完成队伍调整，
你需要计算出最少需要调整多少次可以让上述情况最少。
例如：CCDCC->CCCDC->CCCCD这样就能使之前的两处鸡鸭相邻变为一处鸡鸭相邻，需要调整队形两次。

输入描述:
输入一个长度为N，且只包含C和D的非空字符串。
输出描述:
使得最后仅有一对鸡鸭相邻，最少的交换次数
示例1
输入
CCDCC
输出
2
'''
'''
么鸡全在左边，要么鸭全在左边，记录当前顺序变到这两种情况的移动次数，取较小值即可
注：若某鸡的下标为i  其左边还有cnt只鸡  则最少需要i - cnt次才能将其移到左鸡堆的最右边
'''
s=input();
def solve(s,t):
    res,cnt=0,0;
    for i in range(len(s)):
        if s[i]==t:
            res+=i-cnt;
            cnt+=1;
    return res;
print(min(solve(s,'D'),solve(s,'C')))