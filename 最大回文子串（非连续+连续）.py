# -*- encoding: utf-8 -*-
'''
@File    :   最大回文子串.py
@Time    :   2020/02/25 15:15:39
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   最大回文子串.py
'''

'''
最大回文子串是被研究得比较多的一个经典问题。最近月神想到了一个变种，对于一个字符串，如果不要求子串连续，那么一个字符串的最大回文子串的最大长度是多少呢。
输入描述:
每个测试用例输入一行字符串（由数字0-9，字母a-z、A-Z构成），字条串长度大于0且不大于1000.
输出描述:
输出该字符串的最长回文子串的长度。（不要求输出最长回文串，并且子串不要求连续）
示例1
输入
adbca
输出
3
说明
因为在本题中，不要求回文子串连续，故最长回文子串为aba(或ada、aca)
'''
s = input().strip()
n = len(s)
dp = [[0 for _ in range(n)] for _ in range(n)]
for r in range(n):
    dp[r][r] = 1
    for l in range(r-1, -1, -1):
        if s[l] == s[r]:
            dp[l][r] = dp[l+1][r-1]+2
        else:
            dp[l][r] = max(dp[l+1][r], dp[l][r-1])
print(dp[0][n-1])

# 连续的回文字串最大长度


s = input().strip()

# 动态规划
def findLong(s):
    n = len(s)
    maxLen, start = 1, 0
    dp = [[False for _ in range(n)] for _ in range(n)]
    # 右边界大于左边界
    for r in range(1, n):
        for l in range(r):
          # 状态转移方程：如果头尾字符相等并且中间也是回文
          # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
          # 否则要继续看收缩以后的区间的回文性
            if s[l] == s[r] and ((r-l) <= 2 or dp[l+1][r-1]):
                dp[l][r] = True
                if (r-l+1 > maxLen):
                    maxLen = r-l+1
                    start = l
    return s[start:start + maxLen]


print(findLong(s))

# 中心扩展法
s = input().strip()


class Solution:
    def getCenter(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return (i+1, j-i-1)

    def longestPalindrome(self, s: str) -> str:
        n, start, maxLen = len(s), 0, 0
        for i in range(n):
            p1 = self.getCenter(s, i, i)
            p2 = self.getCenter(s, i, i+1)
            p = max([p1, p2], key=lambda i: i[1])
            if maxLen < p[1]:
                start = p[0]
                maxLen = p[1]
        return s[start:start+maxLen]


print(Solution().longestPalindrome(s))
