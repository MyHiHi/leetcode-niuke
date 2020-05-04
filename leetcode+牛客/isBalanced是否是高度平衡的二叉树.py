# 给定一个二叉树，判断它是否是高度平衡的二叉树。

# 本题中，一棵高度平衡二叉树定义为：

# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

# 示例 1:

# 给定二叉树 [3,9,20,null,null,15,7]

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 自上而下
# 下面的结点会重复计算高度
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:return True;
        def getHeight(root):
            if not root:return 0;
            return max(getHeight(root.left),getHeight(root.right))+1;
        p,stack=root,[];
        while p or stack:
            while p:
                l,r=getHeight(p.left),getHeight(p.right);
                if abs(l-r)>1:return False;
                stack.append(p);
                p=p.left;
            if stack:
                p=stack.pop();
                p=p.right;
        else:return True;


# 自底向上;
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res=True;
        def run(root):
            if not root:
                return 0;
            l=run(root.left);
            r=run(root.right);
            if abs(l-r)>1:
                self.res=False;
            # 下面是求高度的
            return max(l,r)+1;
        run(root);
        return self.res;
        