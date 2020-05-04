# -*- encoding: utf-8 -*-
'''
@File    :   wordBreak.py
@Time    :   2020/01/14 11:42:23
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否
可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        默认前0个
        dp[0] = True
        for i in range(n):
          # 因为要判断前n个（也就是整个s）拆分后是否在wordDict
          # 所以 j 要到 n+1
            for j in range(i+1, n+1):
              # dp[i]判断前i个是否在wordDict
              # 如果s[i:j]也在wordDict，则dp[j]=True:前j个在wordDict
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]
