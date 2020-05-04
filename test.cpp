/*
@File    :   test.cpp
@Time    :   2020/04/27 09:47:04
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test.cpp
*/
/*
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
  vector<int> p = {12, 2, 43, 23, 34, 45, 5, 5, 45};
  cout << *max_element(p.begin(), end(p));
  return 0;
}
