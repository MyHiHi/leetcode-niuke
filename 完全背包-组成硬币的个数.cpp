/*
@File    :   完全背包-组成硬币的个数.cpp
@Time    :   2020/04/23 11:47:48
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   完全背包-组成硬币的个数.cpp
*/
/*
*/
#include <iostream>
using namespace std;
class Solution
{
public:
  int waysToChange(int n)
  {
    int *dp = new int[n + 1]{1}, MAX = 1e9 + 7;
    int coins[4] = {1, 5, 10, 25};
    for (auto coin : coins)
    {
      for (int i = coin; i <= n; i++)
        // 这是总计次数，不是放入背包要求资产最大化，不用 max()
        // 当前i 不放coin + 放coin
        dp[i] = (dp[i] + dp[i - coin]) % MAX;
    }
    return dp[n];
  }
};
int main()
{
  return 0;
}
