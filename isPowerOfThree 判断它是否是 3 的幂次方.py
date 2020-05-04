# -*- encoding: utf-8 -*-
'''
@File    :   isPowerOfThree.py
@Time    :   2020/01/07 11:07:09
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
