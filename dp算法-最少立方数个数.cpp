/*
@File    :   最少立方数个数.cpp
@Time    :   2020/04/18 11:52:46
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   dp...最少立方数个数.cpp
*/
/*
题目描述
给出一个数字N（0<N<1000000）,将N写成立方数和的形式，求出需要的最少立方数个数。
例如N=17，1+8+8 = 17，最少需要3个立方数，则输出3。
N= 28,1+1+1+1+8+8+8=28, 需要7个立方数，1+27=28,需要2个立方数，所以最少立方数为2，则输出2。
输入描述:
一个数字N（0<N<1000000）
输出描述:
最少立方数个数
示例1
输入
28
*/
/*
动态规划，设dp[n]为组成 n需要的最少立方数个数
所有差一步(这一步是个立方数)可以组成n的方案，求最小值加一
dp[n] = 1 + min(dp[n-1],dp[n-8],dp[n-27],...) 要求n-i*i*i>=0
*/
#include <iostream>
using namespace std;
int main()
{
  int n;
  cin >> n;
  int *dp = new int[n + 1];
  dp[0] = 0;
  for (int t = 1; t <= n; t++)
  {
    int mi = 1e8;
    for (int i = 1; i * i * i <= t; i++)
      mi = mi > dp[t - i * i * i] ? dp[t - i * i * i] : mi;
    dp[t] = mi + 1;
  }
  for(int i=0;i<n+1;i++){
    int a=dp[i];
    cout <<i<<": "<< a<<endl ;
  }
  cout << dp[n];
  return 0;
}
