/*
@File    :   572. 另一个树的子树.cpp
@Time    :   2020/03/20 10:32:36
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   572. 另一个树的子树.cpp
*/
/*
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4 
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
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
// 判断是否是相同的树
  bool isSame(TreeNode *s, TreeNode *t)
  {
    if (s == NULL && t == NULL)
      return true;
    if (s == NULL || t == NULL)
      return false;
    return s->val == t->val && isSame(s->left, t->left) && isSame(s->right, t->right);
  }
  // 从s的子树开始判断 是否存在 和t 结构 数值相同的子树
  bool isSubstr(TreeNode *s, TreeNode *t)
  {
    return s != NULL && (isSame(s, t) || isSubstr(s->left, t) || isSubstr(s->right, t));
  }
  // 这是题目最终调用方法
  bool isSubtree(TreeNode *s, TreeNode *t)
  {
    return isSubstr(s, t);
  }
};
int main()
{
  return 0;
}

// python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def toTup(t):
            return (t.val,toTup(t.left),toTup(t.right)) if t else None;
        print(toTup(s),"**",toTup(t))
        
// (3, (4, (1, None, None), (2, None, None)), (5, None, None)) ** 
// (4, (1, None, None), (2, None, None))

        return str(toTup(t)) in str(toTup(s))

// python
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def preOrder(s,st):
            if s:
                st+=[','+str(s.val)];
                preOrder(s.left,st);
                preOrder(s.right,st);
            st+=[',?']
        k1,k2=[],[]
        preOrder(s,k1)
        preOrder(t,k2);
        print (''.join(k1) ,'**', ''.join(k2))
        // ,3,4,1,?,?,?,2,?,?,?,?,5,?,?,?,? ** ,4,1,?,?,?,2,?,?,?,?
        return ''.join(k2) in ''.join(k1)