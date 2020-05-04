/*
@File    :   非相邻的地块种花问题.cpp
@Time    :   2020/03/22 09:59:23
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   非相邻的地块种花问题.cpp
*/
/*
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
// 最左边和最后添加0
  bool canPlaceFlowers(vector<int> &flowerbed, int n)
  {
    flowerbed.insert(flowerbed.begin(), 0);
    flowerbed.push_back(0);
    int le = flowerbed.size(), i = 0;
    while (n > 0 && i + 2 < le)
    {
      if (flowerbed[i] == 0 && flowerbed[i + 1] == 0 && flowerbed[i + 2] == 0)
      {
        flowerbed[i + 1] = 1;
        n--;
      }
      i++;
    }
    if (n == 0)
      return true;
    return false;
  }
};
int main()
{
  return 0;
}
