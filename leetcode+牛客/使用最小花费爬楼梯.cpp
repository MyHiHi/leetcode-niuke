/*
@File    :   使用最小花费爬楼梯.cpp
@Time    :   2020/04/04 11:21:13
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   动态规划+使用最小花费爬楼梯.cpp
*/
/*
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
  int minCostClimbingStairs(vector<int> &cost)
  {
    int size = cost.size();
    int *dp = new int[size]{cost[0], cost[1]};
    for (int t = 2; t < size; t++)
    {
      dp[t] = min(dp[t - 1], dp[t - 2]) + cost[t];
    }
    return min(dp[size - 1], dp[size - 2]);
  }
};

// 二
class Solution
{
public:
  int minCostClimbingStairs(vector<int> &cost)
  {
    cost.push_back(0);
    for (int t = 2; t < cost.size(); t++)
    {
      cost[t] += min(cost[t - 1], cost[t - 2]);
    }
    return cost.back();
  }
};