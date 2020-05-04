# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 注意:
# 你可以假设树中没有重复的元素。
# 例如，给出
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.pre_co=0;
        def run(start,end):
            # 边界判断
            if start>end:return None;
            # 先序的节点
            p=preorder[self.pre_co];
            node=TreeNode(p);
            # 依次遍历先序节点
            self.pre_co+=1;
            # 找到中序中的父节点，为了对左子数和右子树依次遍历
            index=inorder.index(p)
            node.left=run(start,index-1);
            node.right=run(index+1,end);
            return node;
        return run(0,len(preorder)-1);
    
# 根据一棵树的中序遍历与后序遍历构造二叉树。
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：
#     3
#    / \
#   9  20
#     /  \
#    15   7


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        le=len(inorder)
        self.post=le-1;
        def run(start,end):
            if start>end:return None;
            p=postorder[self.post];
            node=TreeNode(p);
            index=inorder.index(p);
            # 从后序的从后往前遍历
            self.post-=1;
            # 观察：从3开始，前面的20 在右子树上，所以先连接右子树
            # 也是从index开始分为左子数和右子树
            node.right=run(index+1,end);
            node.left=run(start,index-1);
            return node;
        return run(0,le-1);