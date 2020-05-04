/*
@File    :   test1.cpp
@Time    :   2020/04/27 20:16:42
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test1.cpp
*/
/*
*/
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
bool look(string S, string &C)
{
  int i = 0;
  for (char s : S)
  {

    if (find(C.begin() + i, C.end(), s) != C.end())
    {
      i = find(C.begin() + i, C.end(), s) - C.begin(), C = C.erase(i, 1);
    }
    else
    {
      return false;
    }
  }
  return true;
}
bool chkMixture(string A, int n, string B, int m, string C, int v)
{
  // write code here
  if (v != n + m)
    return false;
  bool a = look(A, C);
  cout << a << " " << C << " " << C.size() << endl;
  bool b = look(B, C);
  cout << b << " " << C << endl;
  return a && b && !C.size();
}
int main()
{
  cout << chkMixture("bcbccabccacccbcac", 17, "abbbacaabccbccaaaabbcbcbaaacccbaaba", 35, "babbbacaabccbccaaaabbcbcbaaacccbaabacbccabccacccbcac", 52);

  return 0;
}
