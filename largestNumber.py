# -*- encoding: utf-8 -*-
'''
@File    :   largestNumber.py
@Time    :   2020/01/02 11:44:40
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''
'''
定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ''
        from functools import cmp_to_key
        nums = map(str, nums)
        # 采用cmp_to_key 函数，可以接受两个参数
        nu = sorted(nums, key=cmp_to_key(lambda x, y: int(y+x)-int(x+y)))
        res = ''.join(nu).lstrip('0')
        return res or '0'

# from functools import cmp_to_key
# d: dict = [12, 2, 1324, 23, 1, 23, 44, 11]
# # # key仅仅支持一个参数
# li: list = sorted(d, key=cmp_to_key(lambda x, y: y-x))
# print(li)


# nums = [3, 30, 34, 5, 9]
# nums = map(str, nums)
# #         # 采用cmp_to_key 函数，可以接受两个参数
# nu = sorted(nums, key=cmp_to_key(lambda x, y: int(x+y)-int(y+x)))

# print(nu)
