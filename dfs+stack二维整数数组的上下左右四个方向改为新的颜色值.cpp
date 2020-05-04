/*
@File    :   二维整数数组的上下左右四个方向改为新的颜色值.cpp
@Time    :   2020/04/03 10:48:35
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   dfs/stack二维整数数组的上下左右四个方向改为新的颜色值.cpp
*/
/*
有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

最后返回经过上色渲染后的图像。

示例 1:

输入: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],[2,2,0],[2,0,1]]
解析: 
在图像的正中间，(坐标(sr,sc)=(1,1)),
在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，
因为它不是在上下左右四个方向上与初始点相连的像素点。
*/
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
  int l1, l2, me;
  stack<vector<int>> stacky;
  void change(vector<vector<int>> &image, int sr, int sc, int newColor)
  {
    vector<int> l = {sr - 1, sr + 1, sr, sr}, r = {sc, sc, sc - 1, sc + 1};
    for (int t = 0; t < 4; t++)
    {
      int p1 = l[t], p2 = r[t];
      if (p1 >= 0 && p1 < l1 && p2 >= 0 && p2 < l2 && image[p1][p2] == me)
      {
        image[p1][p2] = newColor;
        vector<int> temp = {p1, p2};
        stacky.push(temp);
      }
    }
  }
  vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int newColor)
  {
    l1 = image.size(), l2 = image[0].size();
    me = image[sr][sc];
    if (me == newColor)
      return image;
    image[sr][sc] = newColor;

    change(image, sr, sc, newColor);
    while (!stacky.empty())
    {
      vector<int> p = stacky.top();
      stacky.pop();
      change(image, p[0], p[1], newColor);
    }
    return image;
  }
};

// dfs
class Solution
{
public:
  int l1, l2;
  int me, newC;
  void dfs(vector<vector<int>> &image, int r, int c)
  {
    if (image[r][c] == me)
    {
      image[r][c] = newC;
      if (r + 1 < l1)
        dfs(image, r + 1, c);
      if (c + 1 < l2)
        dfs(image, r, c + 1);
      if (r - 1 >= 0)
        dfs(image, r - 1, c);
      if (c - 1 >= 0)
        dfs(image, r, c - 1);
    }
  }
  vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int newColor)
  {
    l1 = image.size(), l2 = image[0].size();
    me = image[sr][sc], newC = newColor;
    if (me == newColor)
      return image;
    dfs(image, sr, sc);
    return image;
  }
};