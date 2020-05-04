/*
@File    :   594. 最长和谐子序列.cpp
@Time    :   2020/03/19 10:38:18
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   594. 最长和谐子序列.cpp
*/
/*
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

示例 1:

输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
  int findLHS(vector<int> &nums)
  {
    // hashMap默认按照key从小到大排序
    // 记录每个数字出现的次数,然后把key相差1的数字个数相加的最大值即为 最长和谐子序列的长度
    map<int, int> myMap;
    for (auto i : nums)
      myMap[i]++;
    map<int, int>::iterator it = myMap.begin(), p = it;
    int res = 0;
    for (; it != myMap.end(); it++)
    {
      if (it->first - p->first == 1)
        res = max(it->second + p->second, res);
      p = it;
    }
    return res;
  }
};
int main()
{
  return 0;
}
