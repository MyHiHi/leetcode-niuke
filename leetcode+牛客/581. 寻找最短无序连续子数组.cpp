/*
@File    :   581. 最短无序连续子数组.cpp
@Time    :   2020/03/18 12:06:10
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   581. 寻找最短无序连续子数组.cpp
*/
/*
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
  int findUnsortedSubarray(vector<int> &nums)
  {
    vector<int> temp(nums.begin(), nums.end());
    sort(temp.begin(), temp.end());
    int l = 0, r = temp.size() - 1;
    while (l <= r && temp[l] == nums[l])
      l += 1;
    while (l <= r && temp[r] == nums[r])
      r -= 1;
    return r - l + 1;
  }
};

// 代码二
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int size=nums.size();
        int i=0,j=size-1;
        int prev_max=nums[i],back_min=nums[j];
        int l=0,r=0;
        while (i<size){
            int c=nums[i];
// 遍历:左 --> 右
//prev_max：i之前的最大值，prev_max > 当前值，说明nums[:i]非递增，记录右边界i
            if (c<prev_max)
                r=i;
            else
                prev_max=c;
            int b=nums[size-i-1];
// 遍历:右 --> 左
//back_min:i之后的最小值，back_min < 当前值,说明nums[i:]非递增，记录左边界i
            if (b>back_min)
                l=size-i-1;
            else
                back_min=b;
            i+=1;
        }
        return l==r?0:r-l+1;
    }
};
int main()
{
  return 0;
}
