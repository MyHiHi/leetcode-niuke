# -*- encoding: utf-8 -*-
'''
@File    :   hammingWeight.py
@Time    :   2020/01/03 22:30:46
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''


'''
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        c = 1
        for i in range(32):
            if n & c != 0:
                sum += 1
            c <<= 1
        return sum


class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        for i in range(32):
            if (n >> i) & 1 == 1:
                sum += 1
        return sum
