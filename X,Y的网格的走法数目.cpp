/*
@File    :   X,Y的网格的走法数目.cpp
@Time    :   2020/03/24 11:25:05
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   X,Y的网格的走法数目.cpp
*/
/*
*/
// 代码一
/*
注意只能走格点，不是走方块，你画个网格就知道了。

所以 3 * 2 的网格，实际上格点数却是 4 * 3 。
*/
#include <iostream>
#include <cstring>
using namespace std;
int main()
{
  int x, y;
  cin >> x >> y;
  int dp[x + 1][y + 1];
  memset(dp, 0, sizeof(dp));
  for (int a = 0; a <= x; a++)
    for (int b = 0; b <= y; b++)
    {
      if (a == 0 || b == 0)
        dp[a][b] = 1;
      else
        dp[a][b] = dp[a - 1][b] + dp[a][b - 1];
    }
  cout << dp[x][y];
  return 0;
}

// 代码二
/*
组合问题

因为只能向右走和向下，所以无论怎么走，向右的总距离和向下总距离都只能是x和y
（即网格大小，曼哈顿距离不变），
可以转换成排列组合问题，
假设用0代表向右，1代表向下，题目转化成用x个0和Y个1能组成多少个不同的数，
由排列组合公式可知，组合数应当是：
C(x+y,x)==C(x+y,y)
*/
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
  int x, y;
  cin >> x >> y;
  int sum = x + y;
  int mi = min(x, y);
  long d1 = 1, d2 = 1;
  for (int t = 1; t <= mi; t++, sum--)
  {
    d1 *= sum;
    d2 *= t;
  }
  cout << d1 / d2;
  return 0;
}

#include <iostream>
using namespace std;
int main()
{
  return 0;
}
