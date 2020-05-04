/*
@File    :   560. 和为K的子数组.cpp
@Time    :   2020/04/22 10:59:51
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   560. 和为K的子数组.cpp
*/
/*
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
*/
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
  int subarraySum(vector<int> &nums, int k)
  {
    map<int, int> mp;
    mp[0] = 1;
    int cnt = 0, sum = 0;
    for (auto a : nums)
    {
      sum += a;
      /*map:  (sum_1,sum_1出现的次数
  的出现次数)
        sum - k 在 mp中存在 ，说明至少有一个在 sum-k ---- sum 中存在序列和为 k，
        而 mp[sum-k]也不一定是当前位置之前的次数和，比如 [1,1,-1,1],[1]=sum([1])=1,而 [1]=sum([1,1,-1]);
        故 mp[sum-k]如果存在，则表示有 mp[sum-k]次 序列和为 k

      */
      if (mp[sum - k])
      {
        cout << sum - a << ": " << mp[sum - a] << endl;
        cnt += mp[sum - k];
      }

      mp[sum]++;
    }
    return cnt;
  }
};

/* 变种
1248. 统计「优美子数组」
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
*/
/*
nums中偶数设为0,奇数为1，
连续 子数组中恰好有 k 个奇数数字 的个数  表示 有多少个和为k 的子序列
*/
int main()
{
  return 0;
}
