/*
@File    :   归并排序.数组中的逆序对.cpp
@Time    :   2020/04/24 21:21:41
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   归并排序.数组中的逆序对.cpp
*/
/*
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，
求出这个数组中的逆序对的总数。
示例 1:

输入: [7,5,6,4]
输出: 5
*/
/*
归并和快速排序区别：
1.联系
原理都是基于分而治之，首先把待排序的数组分为两组，然后分别对两组排序，最后把两组结果合并起来

2.区别
进行分组的策略不同，合并的策略也不同。
归并的分组策略：自顶向下，是假设待排序的元素存放在数组中，那么把数组前面的一半元素作为一组，后面一半作为另一组（merge_sort）,
然后两个有序的数组根据大小合并（插入排序 merge），时间复杂度为 O(nlogn)
快速排序：自底向上，根据元素的值来分的，大于某个值的元素一组，小于某个值的元素一组，然后对每组递归进行同样操作，
最好：时间复杂度为 O(nlogn)，最坏：时间复杂度为 O(n^2)
*/
/*
下面我们这样来思考:[7,5,6,4]
1.先把数组分成两个部分[7,5],[6,4],在继续分割成[[7],[5]],[[6],[4]]两个组merge_sort
接着进行合并,先合并[[7],[5]],由于7>5,在这个组内存在一个逆序排列,根据由小到大排序得到[5,7];
同理对[[6],[4]]进行同样的操作,得到[4,6],同样也存在一个逆序对
2.下面进行组间的合并（merge）s1=[5,7],s2=[4,6],此时我们需要需要一个辅助数组s来存储排序好的数组,
我们设置两个指针分别指向s1和s2的尾部,当前指向的数字为7和6,由于这两个数组都是排好序的,
所以7会大于s2中的所有数字,即与7能组成逆序对的个数为s2数组的长度,然后将7放入s的末尾,再比较5和6,5<6,不存在逆序对,将6放入s中,此时s=[6,7],再次比较5和4,5>4,存在逆序对,逆序对的数目等于1,将5放入s,将4放入s
如此下去,可以发现上面的过程就是归并排序的过程,只需简单的加入统计逆序对变量即可
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
  int cnt = 0;
  void merge_sort(vector<int> &nums)
  {
    int n = nums.size();
    if (n < 2)
      return;
    int t = n / 2;
    vector<int> s1(nums.begin(), nums.begin() + t), s2(nums.begin() + t, nums.end());
    merge_sort(s1);
    merge_sort(s2);
    merge(s1, s2, nums);
  }
  void merge(vector<int> &s1, vector<int> &s2, vector<int> &nums)
  {
    int l1 = s1.size() - 1, l2 = s2.size() - 1, t = nums.size() - 1;
    while (l1 >= 0 && l2 >= 0)
    {
      // 下面是从小到大排序，改为if (s1[l1] < s2[l2]):从大到小排序
      if (s1[l1] > s2[l2])
      {
        cnt += l2 + 1;
        nums[t] = s1[l1], t--, l1--;
      }
      else
      {
        nums[t] = s2[l2], t--, l2--;
      }
    }
    while (l1 >= 0)
    {
      nums[t] = s1[l1], t--, l1--;
    }
    while (l2 >= 0)
    {
      nums[t] = s2[l2], t--, l2--;
    }
  }
  int reversePairs(vector<int> &nums)
  {
    merge_sort(nums);
    return cnt;
  }
};
int main()
{
  return 0;
}
