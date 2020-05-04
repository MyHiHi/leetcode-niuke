/*
@File    :   914. 最大公约.卡牌分组.cpp
@Time    :   2020/04/15 08:30:35
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   914. 最大公约.卡牌分组.cpp
*/
/*
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

示例 1：

输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
示例 2：

输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
*/

#include <iostream>
#include <vector>
#include <map>
using namespace std;
class Solution
{
public:
// 求最大公约
  int gcd(int a, int b)
  {
    return b == 0 ? a : gcd(b, a % b);
  }
  bool hasGroupsSizeX(vector<int> &deck)
  {
    int miLen = 100;
    map<int, int> nums;
    for (auto a : deck)
    {
      nums[a]++;
    }
    int x = 0;
    for (auto t : nums)
    {
      int c = t.second;
      x = gcd(x, c);
      if (x == 1)
        return false;
    }
    return x >= 2;
  }
};
int main()
{
  return 0;
}
