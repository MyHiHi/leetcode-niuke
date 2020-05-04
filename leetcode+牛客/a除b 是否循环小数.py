# -*- encoding: utf-8 -*-
'''
@File    :   a除b 是否循环小数.py
@Time    :   2020/03/08 11:14:57
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   a除b 是否循环小数.py
'''

'''
题目描述
求a/b的小数表现形式。如果a可以整除b则不需要小数点。如果是有限小数，则可以直接输出。
如果是无限循环小数，则需要把小数循环的部分用"()"括起来。 

输入描述:
两个整数a和b，其中

0 <= a <= 1000 000

1 <= b <= 10 000
输出描述:
一个字符串，该分数的小数表现形式
示例1 
输入
10 1
输出
10
'''
def solve(x,y):
    k=x//y;
    # pre存放整数；
    # back存放小数后面的
    pre,back=str(k),"";
    cycle={}
    while x%y:
        # x=(x%y)*10;
        # 比如x=1,y=3;
        # 此时 x=(x%y)*10=10 余数再次出现 ，
        # 则对应的商值为循环开始，
        # 若没有相同余数，则为有限小数。不考虑无限不循环小数 
        if cycle.get(x)!=None:
            i=cycle[x]
            back=back[:i]+"("+back[i:]+")";
            break;
        else:
            p=x//y;
            back+=str(p);
            # 用一个map保存每个余数出现的位置
            cycle[x]=len(back)-1;
    if back:
        return pre+"."+back;
    else:
        return pre
x,y=list(map(int,input().split()))
print(solve(x,y))