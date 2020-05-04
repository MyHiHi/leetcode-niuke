/*
@File    :   563. 二叉树左子树的结点之和和右子树结点之和的差的和.cpp
@Time    :   2020/03/15 12:34:16
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   563. 二叉树左子树的结点之和和右子树结点之和的差的和.cpp
*/
/*
*/


/*
给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。
空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。

示例:

输入: 
         1
       /   \
      2     3
输出: 1
解释: 
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
*/
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
  int sumC(TreeNode *root, int *sum)
  {
    if (root == NULL)
      return 0;
    int left = sumC(root->left, sum);
    int right = sumC(root->right, sum);
    *sum += abs(left - right);
    return root->val + left + right;
  }
  int findTilt(TreeNode *root)
  {
    int sum = 0;
    sumC(root, &sum);
    return sum;
  }
};
