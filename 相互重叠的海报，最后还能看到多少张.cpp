/*
@File    :   相互重叠的海报，最后还能看到多少张.cpp
@Time    :   2020/03/19 16:36:59
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   相互重叠的海报，最后还能看到多少张.cpp
*/
/*
我们部门需要装饰墙，但是墙非常非常的长，有一千万米。我们会按顺序贴很多海报在上面，
这些海报相互之间会重叠，请问下，最后还能看到哪些？（只看到一部分也算）
输入描述:
N表示N张海报
接下来每一行代表海报的左右边界（上下默认全满），Li，Ri，均为整数，大于0，小于一千万。
海报按输入顺序张贴。
输出描述:
有多少张海报是可见的
示例1
输入
5
1 4
2 6
8 10
3 4
7 10
输出
4
*/
#include <iostream>
#include <cmath>
#include <vector>
#include <set>
using namespace std;
int main()
{
  int maxValue = 10000000, minValue = 1;
  vector<int> pixels(maxValue + 1, 0);
  int n;
  cin >> n;
  for (int t = 1; t <= n; t++)
  {
    int a, b;
    cin >> a >> b;
    // 记录海报的 最右和最左， 这样就不用从1开始遍历了
    maxValue = max(maxValue, b);
    minValue = min(minValue, a);
    // 将当前海报的长度 每个像素  用同一个t编码
    for (int i = a; i <= b; i++)
      pixels[i] = t;
  }
  // 记录不重复值
  set<int> res;
  for (int t = minValue; t <= maxValue; t++)
  {
    // 只有墙上有海报（被编码，非0），才插入
    if (pixels[t])
      res.insert(pixels[t]);
  }
  cout << res.size() << endl;
  return 0;
}

// python 复杂度太大,60%
N = int(input());
maxValue, minValue = 10000000, 1;
pixels=[0]*(maxValue+1)
for t in range(1,N+1):
    a,b=list(map(int,input().split()));
    for
      i in range(a, b + 1) : pixels[i] = t;
    maxValue, minValue = max(maxValue, b), min(minValue, a);
res=set([pixels[t] for t in range(minValue,maxValue+1) if pixels[t]])
print(len(res))