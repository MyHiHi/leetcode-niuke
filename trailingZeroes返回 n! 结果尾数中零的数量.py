# -*- encoding: utf-8 -*-
'''
@File    :   trailingZeroes.py
@Time    :   2019/12/29 10:21:10
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

# 给定一个整数 n，返回 n! 结果尾数中零的数量。

# 示例 1:

# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
# 找到一个 5，一定能找到一个 2 与之配对。所以我们只需要找有多少个 5。
# 我们只需要判断每个累乘的数有多少个 5 的因子即可。


class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 0
        while n:
            i += n//5
            n //= 5
        return i
