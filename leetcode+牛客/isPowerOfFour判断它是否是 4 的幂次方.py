# -*- encoding: utf-8 -*-
'''
@File    :   isPowerOfFour.py
@Time    :   2020/01/16 12:41:38
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
算法：

我们首先检查 num 是否为 2 的幂：x > 0 and x & (x - 1) == 0。

现在的问题是区分 2 的偶数幂（当 xx 是 4 的幂时）和 2 的奇数幂（当 xx 不是 4 的幂时）。在二进制表示中，这两种情况都只有一位为 1，其余为 0。

有什么区别？在第一种情况下（4 的幂），1 处于偶数位置：第 0 位、第 2 位、第 4 位等；在第二种情况下，1 处于奇数位置。
'''
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num>0 and num & (num-1)==0 and num & 0xaaaaaaaa==0

