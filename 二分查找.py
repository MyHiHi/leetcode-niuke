# -*- encoding: utf-8 -*-
'''
@File    :   二分查找.py
@Time    :   2020/02/19 12:16:50
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   二分查找.py
'''


# 经按照非递减顺序排序的数组中找到第一个大于等于给定值key的那个数的索引，
def binary_search(p:List, k):
    l, r = 0, len(p)-1
    while l < r:
        n = (l+r) >> 1
        if p[n] >= k:
            r = n
        else:
            l = n+1
    return l
# 在按照非递减顺序排好序的数组中找到第一个大于给定值key的那个数索引，
    #  * 其基本实现原理是二分查找
    # from bisect import bisect
    # bisect(p,k)
def binary_search(p:List, k):
    l, r = 0, len(p)-1
    while l < r:
        n = (l+r) >> 1
        if p[n] <= k:
            l=n+1
        else:
            r=n
    return l