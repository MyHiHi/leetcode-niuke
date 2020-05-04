# -*- encoding: utf-8 -*-
'''
@File    :   judgeSquareSum.py
@Time    :   2020/01/21 09:40:52
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a,b=0,int(c**0.5);
        res=a**2+b**2;
        while a<=b:
           if res==c:return True;
           elif res<c:a+=1;
           else:b-=1;
           res=a**2+b**2;
        return False



class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if not c:return True
        for i in range(1, int(c**0.5)+1):
            r = (c-i*i)**0.5
            k = int(r)
            if r**2 == k**2:
                return True
        return False
