# -*- encoding: utf-8 -*-
'''
@File    :   isLongPressedName.py
@Time    :   2020/02/05 11:18:22
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时
，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），
那么就返回 True。

 

示例 1：

输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：

输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
示例 3：

输入：name = "leelee", typed = "lleeelee"
输出：true
'''


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        leN, leT = len(name), len(typed)
        if leN > leT:
            return False
        if name == typed:
            return True
        '''
        l指针跟踪name,r指针跟踪typed
        '''
        l, r = 0, 0
        while l < leN and r < leT:
            if name[l] == typed[r]:
                l += 1
                r += 1
            else:
                r += 1
        return l == leN
