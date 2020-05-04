/*
@File    :   897. 递增顺序查找树.cpp
@Time    :   2020/04/11 14:29:32
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   897. 构建只有右子树，原树中最左边的结点是其树的根.cpp
*/
/*
给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，
并且每个结点没有左子结点，只有一个右子结点。

示例 ：

输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
*/
#include <bits/stdc++.h>
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
  TreeNode *increasingBST(TreeNode *root)
  {
    stack<TreeNode *> s;
    TreeNode *Fi = new TreeNode(0);
    TreeNode *p = Fi;
    while (s.size() > 0 || root)
    {
      if (root)
      {
        s.push(root);
        root = root->left;
      }
      else
      {
        TreeNode *f = s.top();
        s.pop();
        root = f->right;
        f->left = NULL;
        p->right = f;
        p = f;
      }
    }
    return Fi->right;
  }
};

// 递归
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
  TreeNode *res, *cur;
  void inOrder(TreeNode *r)
  {
    if (r)
    {
      inOrder(r->left);
      cur->right = new TreeNode(r->val);
      cur = cur->right;
      inOrder(r->right);
    }
  }
  TreeNode *increasingBST(TreeNode *root)
  {
    cur = new TreeNode(0);
    res = cur;
    inOrder(root);
    return res->right;
  }
};
int main()
{
  return 0;
}
