# -*- encoding: utf-8 -*-
'''
@File    :   latex爱好者.py
@Time    :   2020/02/26 09:59:52
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   latex爱好者.py
'''

'''
题目描述
latex自然是广大研究人员最喜欢使用的科研论文排版工具之一。
月神想在iPhone 上查阅写好的paper，但是无赖iPhone 上没有月神喜欢使用的阅读软件，于是月神也希望像tex老爷爷Donald Knuth那样自己动手do it yourself一个。
在DIY这个阅读软件的过程中，月神碰到一个问题，已知iPhone屏幕的高为H，宽为W，若字体大小为S(假设为方形），则一行可放W / S(取整数部分）个文字，一屏最多可放H / S （取整数部分）行文字。
已知一篇paper有N个段落，每个段落的文字数目由a1, a2, a3,...., an表示，月神希望排版的页数不多于P页（一屏显示一页），那么月神最多可使用多大的字体呢？

1 <= W, H, ai <= 1000
1 <= P <= 1000000
输入描述:
每个测试用例的输入包含两行。

第一行输入N,P,H,W

第二行输入N个数a1,a2,a3,...,an表示每个段落的文字个数。
输出描述:
对于每个测试用例，输出最大允许的字符大小S
示例1
输入
1 10 4 3 10 2 10 4 3 10 10
输出
3 2
'''
# 代码一
'''
采用二分法解决本问题，字号最小值为1，最大为行宽和列高中较小的一个;

'''
import math
N,P,H,W=list(map(int,input().strip().split()));
pWord=list(map(int,input().strip().split()));
l,r=1,min(H,W);
while l<r:
    S=(l+r)//2+1;
    w=W//S;
    # 一共有多少行
    cols=0;
    for i in pWord:
        cols+=math.ceil(i/w);
    # cols/(H/S) > cols/(H//S)
    # 一共有多少页
    p=math.ceil(cols/(H/S));
    # 当前S下的页数大于限制页数,故r=mid-1;
    # 当前S下的页数小于等于限制页数,S=mid时符合条件,应该查早最佳取值(mid也有可能),故l=mid
    if p>P:
        r=S-1;
    else:
        l=S
print(l)
        
# 代码二
'''
以行为单位，每段不足一行的向上取整，
总段数不超过  最大页数*最大行数
'''
import math
N,P,H,W=list(map(int,input().strip().split()));
pWord=list(map(int,input().strip().split()));
S=1;
while True:
    w,h=W//S,H//S;
    if w==0 or h==0:break;
    cols=0;
    for i in range(N):
        cols+=math.ceil(pWord[i]/w);
    if cols>h*P:break;
    S+=1;
print(S-1)
        
    