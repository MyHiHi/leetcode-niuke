/*
@File    :   1006. 笨阶乘.cpp
@Time    :   2020/04/20 11:16:18
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   1006. 算术运算顺序-笨阶乘.cpp
*/
/*
*/
#include <iostream>
using namespace std;

// 我的，先计算 */ 的结果存到q1，然后在和+ - 计算在一起，分别都是4个 一组
class Solution
{
public:
  int clumsy(int N)
  {
    int *q1 = new int[N], l1 = 0;
    for (int i = N; i >= 1; i -= 4)
    {
      int c = i - 1, y = i;
      y *= c >= 1 ? c, c-- : 1;
      y /= c >= 1 ? c : 1;
      q1[l1++] = y;
    }
    int ans = 0, c = q1[l1 - 1], j = 0;
    int v1 = j < l1 ? q1[j++] : 0;
    for (int i = N - 3; i >= 1; i -= 4)
    {
      int v2 = j < l1 ? q1[j++] : 0;
      ans = v1 + i - v2;
      v1 = ans;
    }
    return N - 3 >= 1 ? ans : c;
  }
};

// 别人code，4个一组
class Solution
{
public:
  int clumsy(int N)
  {
    int ans = 0, temp = N;
    for (int i = 1; i < N; i++)
    {
      int v = N - i, f = i % 4;
      if (f == 1)
      {
        temp *= v;
      }
      else if (f == 2)
      {
        temp /= v;
      }
      else if (f == 3)
      {
        temp += v;
      }
      else if (f == 0)//4个循环完了，此时到负号，temp赋为-v
      {
        ans += temp;
        temp = -v;
      }
    }
    ans += temp;
    return ans;
  }
};
int main()
{
  return 0;
}
