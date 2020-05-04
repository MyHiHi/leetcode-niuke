# -*- encoding: utf-8 -*-
'''
@File    :   快速排序.py
@Time    :   2020/02/25 21:30:12
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   快速排序.py
'''

'''
快速排序由 C. A. R. Hoare 在 1960 年提出。它的基本思想是：
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，
整个排序过程可以递归进行，以此达到整个数据变成有序。
'''
# 一行


def quick(lis): return lis if len(lis) < 2 else quick([
    i for i in lis[1:] if i <= lis[0]])+[lis[0]]+quick([p for p in lis[1:] if p > lis[0]])


def quicksort(arr):
    left, right = [], []
    if len(arr) < 2:
        return arr
    n = len(arr)

    point = arr.pop(n//2)
    '''
    排序+去重的作用：
    1.point = arr[n//2]
    2.for循环的else 改为elif k>point:
    '''
    for k in arr:
        if k < point:
            left += [k]
        else:
            right += [k]
    return quicksort(left)+[point]+quicksort(right)


arr = [1, 2, 3, 1, 2, 4, 5322, 1, 232, 12, 1, 45,
       6, 45, 3453, 432, 42, 31, 2312, 313, 1, 434]
print(quicksort(arr))
# [1, 1, 1, 1, 1, 2, 2, 3, 4, 6, 12, 31, 42, 45, 45, 232, 313, 432, 434, 2312, 3453, 5322]
