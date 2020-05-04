# -*- encoding: utf-8 -*-
'''
@File    :   maxProduct2.py
@Time    :   2020/01/08 10:10:12
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "xtfn"。
'''


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        le = len(words)
        values = [0]*le
        for i in range(le):
            word = words[i]
            # 用二进制记录每个单词中的字母对应的位置，
            for j in word:
                values[i] |= 1 << (ord(j)-97)
        return max([len(words[i])*len(words[j])
                    for i in range(le) for j in range(i, le)
                    #  如果& 结果为0，则单词没有公共字母
                    if not values[i] & values[j]]
                   or [0])

# 这样肯定是过不了的，关键在于集合太费时间。


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        return max([len(w1) * len(w2) for w1 in words for w2 in words if not set(w1) & set(w2)] or [0])
