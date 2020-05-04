# -*- encoding: utf-8 -*-
'''
@File    :   findTheDifference.py
@Time    :   2020/01/08 22:18:32
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。
示例:

输入：
s = "abcd"
t = "abcde"
输出：
e
解释：
'e' 是那个被添加的字母。
'''


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = s+t
        p = ord(t[0])
        # 相同的数字异或都为0，
        # 新加的数字和前面相同数字异或和 0 的异或为新加的数字了
        for i in t[1:]:
            p ^= ord(i)
        return chr(p)


class Solution:
  # ascii 和 相减 答案为 新添加的
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t))-sum(map(ord, s)))
