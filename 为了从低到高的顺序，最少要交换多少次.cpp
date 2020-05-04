// /*
// @File    :   为了从低到高的顺序，最少要交换多少次.cpp
// @Time    :   2020/03/20 14:56:43
// @Author  :   Zhang tao
// @Version :   1.0
// @Desc    :   为了从低到高的顺序，最少要交换多少次.cpp
// */
// /*
// */

// // 代码一
// // 求逆序数
// #include <iostream>
// using namespace std;
// int main(){
//     int n;
//     cin>>n;
//     int height[n];
//     for (int t=0;t<n;t++)
//         cin>>height[t];
//     int ans=0;
//     for(int t=0;t<n;t++)
//         for(int y=0;y<t;y++){
//             if (height[y]>height[t])
//                 ans++;
//         }
//     cout<<ans;
//     return 0;
// }

// // 代码二
// #include <iostream>
// using namespace std;
// int main(){
//     int n;
//     cin>>n;
//     int ans=0;
//     int height[n];
//     for(int t=0;t<n;t++)
//         cin>>height[t];
//     // 插入排序
//     // 统计交换次数
//     for(int t=1;t<n;t++){
//         int tmp=height[t];
//         int i=t-1;
//         // 每一遍交换,t之前都是有序的
//         for(;i>=0 && height[i]>tmp;i--){
//             height[i+1]=height[i];
//             ans++;
//         }
//         height[i+1]=tmp;
//     }
//     cout<<ans;
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;
int main()
{
  vector<int> values{17, 11, 40, 36, 22, 54, 48, 70, 61, 82, 78, 89, 99, 92, 43};
  sort(values.begin(), values.end());
  for (auto c : values)
  {
    cout << c << " ";
  }
  cout << endl;
  int wanted{34}; // What we are looking for
  std::cout << "The upper bound for " << wanted << " is " << upper_bound(values.begin(), values.end(), wanted) - values.begin() << std::endl;
}