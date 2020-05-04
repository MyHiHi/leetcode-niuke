/*
@File    :   选择一些点，保证每个区间至少包含这些点中的两个.cpp
@Time    :   2020/03/22 12:22:14
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   区间选点----选择一些点，保证每个区间至少包含这些点中的两个.cpp
*/
/*
题目描述
我们有很多区域，每个区域都是从a到b的闭区间，现在我们要从每个区间中挑选至少2个数，那么最少挑选多少个？
输入描述:
第一行是N（N<10000）,表示有N个区间，之间可以重复
然后每一行是ai,bi，持续N行，表示现在区间。均小于100000
输出描述:
输出一个数，代表最少选取数量。
示例1
4
4 7
2 4
0 2
3 6
输出
4
*/

// 题意：选择一些点，保证每个区间至少包含这些点中的两个。

// 目标：让这些选点的数量尽可能的少。

// 主要思路：区间右端排序 + 贪心
// 一
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct node
{
  int a, b;
  node() {}
  node(int x, int y) : a(x), b(y) {}
};
bool cmp(node x, node y)
{
  if (x.a == y.a)
    return x.b < y.b;
  else
    return x.a < y.a;
}
int main()
{
  int n;
  cin >> n;
  vector<node> area(n);
  for (int t = 0; t < n; t++)
  {
    int a, b;
    cin >> a >> b;
    area[t] = node(a, b);
  }
  // 从小到大排序
  sort(area.begin(), area.end(), cmp);
  int cnt = 2;
  // l,r表示选点区间
  int l = area[0].a, r = area[0].b;
  for (int t = 1; t < n; t++)
  {
    node c = area[t];
    if (c.a >= l && c.a <= r)
    {
      // 取部分交集
      l = c.a;
      r = min(r, c.b);
    }
    else
    {
      // 更新选点区间
      cnt += 2;
      l = c.a;
      r = c.b;
    }
  }
  cout << cnt;
  return 0;
}

// 二
// 贪心,按右端排序后，遍历区间，如果遍历到的区间代表数不够，每次优先取最右两个数
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// 右端排序
bool cmp(pair<int, int> x, pair<int, int> y)
{
  return x.second < y.second;
}
int main()
{
  int n;
  cin >> n;
  vector<pair<int, int>> area(n);
  for (int t = 0; t < n; t++)
  {
    int a, b;
    cin >> a >> b;
    area[t] = make_pair(a, b);
  }
  sort(area.begin(), area.end(), cmp);
  vector<int> res;
  res.push_back(area[0].second - 1);
  res.push_back(area[0].second);
  for (int t = 1; t < n; t++)
  {
    pair<int, int> r = area[t];
    // 相离
    if (r.first > res.back())
    {
      res.push_back(r.second - 1);
      res.push_back(r.second);
    }
    else if (r.first > res.at(res.size() - 2))
    {
      // 部分相交,res最后取最大值
      res.push_back(r.second);
    }
  }
  cout << res.size();

  return 0;
}
