# -*- encoding: utf-8 -*-
'''
@File    :   合并数组.py
@Time    :   2020/02/27 11:34:02
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   合并数组.py
'''

'''
题目描述
请实现一个函数，功能为合并两个升序数组为一个升序数组
点击页面左下角“例2”，了解如何实现输入输出
输入描述:
输入有多个测试用例，每个测试用例有1-2行，每行都是以英文逗号分隔从小到大排列的数字
输出描述:
输出一行以英文逗号分隔从小到大排列的数组
不允许使用原生的 sort、concat 等函数
示例1
输入
1,5,7,9
2,3,4,6,8,10
输出
1,2,3,4,5,6,7,8,9,10
'''
def r():
    n1 = list(map(int,input().strip().split(',')))
    #要处理只有一行输入的情况。否则会卡80%，非法访问。
    try:
        n2=list(map(int,input().strip().split(',')));
    except:
        print(','.join(map(str,n1)));
        return 
    res = []
    if n1[0] >= n2[-1]:
        res += n2+n1
    elif n1[-1] <= n2[0]:
        res += n1+n2
    else:
        l, r = 0, 0
        l1, l2 = len(n1), len(n2)
        while l < l1 and r < l2:
            k1, k2 = n1[l], n2[r];
            if k1 < k2:
                res += [k1]
                l += 1
            elif k1 > k2:
                res += [k2]
                r += 1
            else:
                res += [k1, k2]
                l += 1
                r += 1

        if l < l1:
            res += n1[l:]
        elif r < l2:
            res += n2[r:]
    print(','.join(map(str,res)))
r()