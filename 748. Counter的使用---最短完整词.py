# -*- encoding: utf-8 -*-
'''
@File    :   748. 最短完整词.py
@Time    :   2020/03/05 11:18:20
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   748. 最短完整词.py
'''

'''
如果单词列表（words）中的一个单词包含牌照（licensePlate）中所有的字母，那么我们称之为完整词。在所有完整词中，最短的单词我们称之为最短完整词。

单词在匹配牌照中的字母时不区分大小写，比如牌照中的 "P" 依然可以匹配单词中的 "p" 字母。

我们保证一定存在一个最短完整词。当有多个单词都符合最短完整词的匹配条件时取单词列表中最靠前的一个。

牌照中可能包含多个相同的字符，比如说：对于牌照 "PP"，单词 "pair" 无法匹配，但是 "supper" 可以匹配。

 

示例 1：

输入：licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
输出："steps"
说明：最短完整词应该包括 "s"、"p"、"s" 以及 "t"。对于 "step" 它只包含一个 "s" 所以它不符合条件。同时在匹配过程中我们忽略牌照中的大小写。

'''
# 代码一
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        alph=''.join(map(lambda x: x.lower(), (filter(str.isalpha, licensePlate))));
        ans=[];
        for w in words:
            v=w;
            f=True
            for a in alph:
                i=w.find(a)
                if i==-1:
                    f=False
                    break;
                w=w[:i]+w[i+1:];
            if f:
                ans+=[v];
        print(ans)
        ans=sorted(ans,key=len);
        return ans[0]
# 代码二
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import Counter
        licensePlate = Counter(filter(str.isalpha, licensePlate.lower()))
        return min(filter(lambda w: not (licensePlate - Counter(w.lower())), words), key=len)

                

# 知识点：
from collections import Counter
# Counter({'s': 2, 't': 1, 'e': 1, 'p': 1})
licensePlate = Counter('steps')
w = "SPPETSS"
# Counter({'s': 3, 'p': 2, 'e': 1, 't': 1})
c = Counter(w.lower())
#  Counter()
v = licensePlate - c
# Counter({'s': 1, 'p': 1})
v1 = c-licensePlate
print(licensePlate, Counter(w.lower()), v, v1)

                

