/*
@File    :   784. 字母大小写全排列.CPP
@Time    :   2020/04/06 11:21:09
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   784. 字母大小写全排列.CPP
*/
/*
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]
注意：

S 的长度不超过12。
S 仅由数字和字母组成。
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
  bool isAlpha(char c)
  {
    if (('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z'))
      return true;
    return false;
  }
  char trans(char c)
  {
    if ('a' <= c && c <= 'z')
      return c - 'a' + 'A';
    return c - 'A' + 'a';
  }
  vector<string> letterCasePermutation(string S)
  {
    vector<string> res = {""};
    for (char c : S)
    {
      int size = res.size();
      if (!isAlpha(c))
      {
        for (int t = 0; t < size; t++)
          res[t] += c;
      }
      else
      {
        vector<string> temp;
        for (int t = 0; t < size; t++)
          temp.push_back(res[t] + c), temp.push_back(res[t] + trans(c));
        res.assign(begin(temp), end(temp));
      }
    }
    return res;
  }
};
int main()
{
  return 0;
}

// python
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def f(x): return (x.lower(), x.upper()) if x.isalpha() else x
        # product 笛卡儿积
        return (list(map(''.join, itertools.product(*map(f, S)))))