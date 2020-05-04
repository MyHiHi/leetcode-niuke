/*
@File    :   大整数相加-爬楼梯.cpp
@Time    :   2020/04/19 19:10:03
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   大整数相加-爬楼梯.cpp
*/
/*
题目描述
在你面前有一个n阶的楼梯，你一步只能上1阶或2阶。
请问计算出你可以采用多少种不同的方式爬完这个楼梯。
输入描述:
一个正整数n(n<=100)，表示这个楼梯一共有多少阶
输出描述:
一个正整数，表示有多少种不同的方式爬完这个楼梯
*/
#include <iostream>
#include <string>
#include <vector>
using namespace std;
// n太大，需要大整数相加
string strAdd(string a, string b)
{
  int carry = 0, i = a.size() - 1, j = b.size() - 1, p1 = 0, p2 = 0, v = 0;
  string ans = "";
  while (i >= 0 || j >= 0)
  {
    p1=(i>=0)?a[i--]-'0':0,p2=(j>=0)?b[j--]-'0':0;
    v=p1+p2+carry;
    carry=v/10,ans=to_string(v%10)+ans;
  }
  return carry == 1 ? "1" + ans : ans;
}
int main()
{
  int n;
  cin >> n;
  // 注意 负数也为1
  if (n <= 1)
  {
    cout << 1;
    return 0;
  }
  string *dp = new string[n + 1];
  dp[0] = "1", dp[1] = "1", dp[2] = "2";
  for (int t = 3; t < n + 1; t++)
  {
    dp[t] = strAdd(dp[t - 1], dp[t - 2]);
  }
  cout << dp[n];
}

// python 直接相加
n=int(input())
p=[0,1,2]
for i in range(3,n+1):
    p+=[p[-2]+p[-1]]
print(p[n])