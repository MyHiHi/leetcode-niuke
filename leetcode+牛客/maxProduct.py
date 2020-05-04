class Solution:
  # 最大值要么是全部数字相乘，要么是下边的两种情况。
    def maxProduct(self, nums: List[int]) -> int:
        c = -1e2
        lek = len(nums)
        mc = 1
        # 包含了所有数相乘的情况
        # 奇数个负数的情况一
        for i in nums:
            mc *= i
            c = max(mc, c)
            if mc == 0:
                mc = 1
        # 奇数个负数的情况一
        mc = 1
        for i in nums[::-1]:
            mc *= i
            c = max(mc, c)
            if mc == 0:
                mc = 1
        return c

# 我们先定义一个数组 dpMax，用 dpMax[i] 表示以第 i 个元素的结尾的子数组，乘积最大的值，也就是这个数组必须包含第 i 个元素。

# 那么 dpMax[i] 的话有几种取值。

# 当 nums[i] >= 0 并且dpMax[i-1] > 0，dpMax[i] = dpMax[i-1] * nums[i]
# 当 nums[i] >= 0 并且dpMax[i-1] < 0，此时如果和前边的数累乘的话，会变成负数，所以dpMax[i] = nums[i]
# 当 nums[i] < 0，此时如果前边累乘结果是一个很大的负数，和当前负数累乘的话就会变成一个更大的数。所以我们还需要一个数组 dpMin 来记录以第 i 个元素的结尾的子数组，乘积最小的值。
# 当dpMin[i-1] < 0，dpMax[i] = dpMin[i-1] * nums[i]
# 当dpMin[i-1] >= 0，dpMax[i] = nums[i]


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m, n = nums[0], nums[0]
        res = m
        for i in nums[1:]:
            mx, mn = m, n
            m = max(mx*i, i, mn*i)
            n = min(mx*i, i, mn*i)
            res = max(res, m)
        return res
