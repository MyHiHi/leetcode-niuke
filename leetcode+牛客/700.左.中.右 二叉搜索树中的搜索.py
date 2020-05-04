# -*- encoding: utf-8 -*-
'''
@File    :   700.左.中.右 二叉搜索树中的搜索.py
@Time    :   2020/03/06 10:06:00
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   700.左.中.右 二叉搜索树中的搜索.py
'''

'''
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

例如，

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2


你应该返回如下子树:

      2     
     / \   
    1   3


在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
'''
# 利用了BST的性质：左<根<右
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def get(root,val):
            if not root or root.val==val:return root;
            return get(root.left,val) if root.val>val else get(root.right,val)
        return get(root,val)
  #  scala
object Solution {
    def searchBST(root: TreeNode, `val`: Int): TreeNode = {
        if(root==null || root.value==`val`){
            root
        }
        else{
            if (root.value>`val`) searchBST(root.left,`val`) else searchBST(root.right,`val`)
        }

    }
}   
# 代码二
# 普通搜索：没有用左<根<右

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def get(root,val):
            if root==None or root.val==val:return root;
            left=get(root.left,val);
            right=get(root.right,val)
            
            if left:return left;
            if right:return right;
            return None
        return get(root,val)