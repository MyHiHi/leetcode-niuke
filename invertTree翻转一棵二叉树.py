# -*- encoding: utf-8 -*-
'''
@File    :   invertTree.py
@Time    :   2020/01/05 22:06:15
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:return None;
        right=self.invertTree(root.right);
        left=self.invertTree(root.left);
        root.left=right;
        root.right=left;
        return root