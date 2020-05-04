# -*- encoding: utf-8 -*-
'''
@File    :   1022. 从根到叶的二进制数之和.py
@Time    :   2020/02/20 09:47:05
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   1022. 从根到叶的二进制数之和.py
'''

'''
给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的
二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

以 10^9 + 7 为模，返回这些数字之和。

示例：
输入：[1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
输入
[1,0,1,0,1,0,1]
            1
          /   \
          0    1
        /  \  / \
       0    1 0  1
输出
22
预期结果
22
stdout
100
101
110
111
'''
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.su=0;
        def dfs(root,val,k):
           if root:
                val=(val<<1)+root.val;
                k+=str(root.val)
                if (root.left==None and root.right==None):
                    self.su+=val;
                    print(k)
                dfs(root.left,val,k);
                dfs(root.right,val,k);
        dfs(root,0,"");
        return self.su