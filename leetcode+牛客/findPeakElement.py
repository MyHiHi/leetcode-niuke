# -*- encoding: utf-8 -*-
'''
@File    :   findPeakElement.py
@Time    :   2019/12/28 09:18:17
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''
# 峰值元素是指其值大于左右相邻值的元素。
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
# 你可以假设 nums[-1] = nums[n] = -∞。
# 示例 1:
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。

# 时间复杂度:n
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        le=len(nums)
        for i in range(1,le-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        return 0 if le==1 else nums.index(max(nums))
      
      
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        le=len(nums)
        for i in range(le-1):
            if nums[i]>nums[i+1]:
                return i
        return 0 if le==1 else nums.index(max(nums))
# 二分法,时间复杂度：  O(logN)    
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        le=len(nums)
        start,end=0,le-1;
        while start<end:
            mid=(start+end)>>1;
            if nums[mid]>nums[mid+1]:
                end=mid;
            else: start=mid+1;
        return start