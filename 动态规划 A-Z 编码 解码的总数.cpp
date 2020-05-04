/*
@File    :   动态规划 A-Z 编码 解码的总数.cpp
@Time    :   2020/03/16 11:38:33
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   动态规划 A-Z 编码 解码的总数.cpp
*/
/*
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

输入描述:
12可以解码成“AB”，“L”这两种
输出描述:
解码方法的总数
示例1
输入
12
输出
2
*/
#include <iostream>
#include <cstring>
using namespace std;
int decoder(string s)
{
  int le = s.size();
  int *dp = new int[le + 1];
  dp[0] = 1;
  dp[1] = 1;
  for (int t = 2; t <= le; t++)
  {
    int m = s[t - 2], n = s[t - 1];
    dp[t] += n != 0 ? dp[t - 1] : 0;

    if (m == '1' || (m == '2' && n <= '6'))
    {
      dp[t] += dp[t - 2];
    }
  }
  return dp[le];
}

int main()
{
  string s;
  cin >> s;
  cout << decoder(s) << endl;
  return 0;
}