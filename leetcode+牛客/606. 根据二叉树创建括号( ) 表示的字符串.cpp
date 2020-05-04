/*
@File    :   606. 根据二叉树创建括号( ) 表示的字符串.cpp
@Time    :   2020/03/23 11:02:29
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   606. 根据二叉树创建括号( ) 表示的字符串.cpp
*/
/*
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响
字符串与原始二叉树之间的一对一映射关系的空括号对。

示例 1:

输入: 二叉树: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

输出: "1(2(4))(3)"

解释: 原本将是“1(2(4)())(3())”，
在你省略所有不必要的空括号对之后，
它将是“1(2(4))(3)”。
*/
#include <iostream>
using namespace std;
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution
{
public:
  string tree2str(TreeNode *t)
  {
    if (t)
    {
      string s = to_string(t->val);
      if (t->left || t->right)
        s += "(" + tree2str(t->left) + ")";
      if (t->right)
        s += "(" + tree2str(t->right) + ")";
      return s;
    }
    return "";
  }
};
int main()
{
  return 0;
}
