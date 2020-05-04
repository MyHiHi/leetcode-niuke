# 给定一个二叉树，返回它的中序 遍历。

# 示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1,3,2]

# 递归
def inorderTraversal(root: TreeNode):
        res=[];
        def run(root):
            if root:
                run(root.left);
                res.append(root.val);
                run(root.right);
        run(root);
        return res;
# 非递归   
def inorderTraversal(root: TreeNode):
    res=[];
    # 模拟栈:装入节点
    stack=[];
    p=root;
    while p or stack:
        while p:
            stack.append(p);
            p=p.left;
        if stack:
            p=stack.pop();
            res.append(p.val);
            p=p.right;
    return res;

