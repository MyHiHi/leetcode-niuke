# -*- encoding: utf-8 -*-
'''
@File    :   thirdMax.py
@Time    :   2020/01/17 15:55:22
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        one,two,three=-float('inf'),-float('inf'),float('inf')
        for i in nums:
            if i>one:
                one,two,three=i,one,two;
            elif i==one:continue;
            elif i>two:
                two,three=i,two;
            elif i==two:continue;
            elif i>three:
                three=i;
            else:continue
        if three!=-float('inf'):return three;
        else:return one

        
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        p=set(nums);
        if len(p)<3:
            return max(p);
        else:
            p.remove(max(p));
            p.remove(max(p));
            return max(p)

        