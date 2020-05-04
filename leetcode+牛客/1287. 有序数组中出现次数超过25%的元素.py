# -*- encoding: utf-8 -*-
'''
@File    :   1287. 有序数组中出现次数超过25%的元素.py
@Time    :   2020/03/03 09:15:51
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   1287. 有序数组中出现次数超过25%的元素.py
'''

'''
给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。

请你找到并返回这个整数

 

示例：

输入：arr = [1,2,2,6,6,6,6,7,10]
输出：6
 

提示：

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
'''
# 代码一
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        i=0;
        le=len(arr)//4;
        while True:
            if arr[i]==arr[i+le]:
                return arr[i];
            i+=1;

# 代码二
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter;
        return Counter(arr).most_common(1)[0][0]