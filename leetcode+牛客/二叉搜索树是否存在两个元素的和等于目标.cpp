/*
@File    :   二叉搜索树是否存在两个元素的和等于目标.cpp
@Time    :   2020/03/25 10:02:44
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   二叉搜索树是否存在两个元素的和等于目标.cpp
*/
/*
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，
则返回 true。

案例 1:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
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
  vector<int> nums;
  void inOrder(TreeNode *root)
  {
    if (root)
    {
      inOrder(root->left);
      nums.push_back(root->val);
      inOrder(root->right);
    }
  }
  bool findTarget(TreeNode *root, int k)
  {
    // 二叉搜索树中序是从小到大排序的
    inOrder(root);
    int l = 0, r = nums.size() - 1;
    while (l < r)
    {
      int sum = nums[l] + nums[r];
      if (sum == k)
        return true;
      else if (sum > k)
        r--;
      else
        l++;
    }
    return false;
  }
};
// python 广遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        queue=[root];
        num=set();
        while queue:
            p=[];
            while queue:
                c=queue[0];
                queue.pop(0);
                if (k-c.val) in num:
                    return True;
                num.add(c.val);
                if (c.left):
                    p+=[c.left];
                if (c.right):
                    p+=[c.right]
            queue=p[:]
        return False
        
