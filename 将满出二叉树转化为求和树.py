# -*- encoding: utf-8 -*-
'''
@File    :   将满出二叉树转化为求和树.py
@Time    :   2020/02/18 10:40:15
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   将满出二叉树转化为求和树.py
'''

'''
题目描述
给满出二叉树，编写算法将其转化为求和树

什么是求和树：二叉树的求和树， 是一颗同样结构的二叉树，其树中的每个节点将包含原始树中的左子树和右子树的和。

二叉树：
                  10
               /      \
             -2        6
           /   \      /  \ 
          8    -4    7    5

求和树：
                 20(4-2+12+6)
               /      \
           4(8-4)      12(7+5)
            /   \      /  \ 
          0      0    0    0

二叉树给出前序和中序输入，求和树要求中序输出；
所有处理数据不会大于int；

输入描述:
2行整数，第1行表示二叉树的前序遍历，第2行表示二叉树的中序遍历，以空格分割
输出描述:
1行整数，表示求和树的中序遍历，以空格分割
示例1
输入
10 -2 8 -4 6 7 5
8 -2 -4 10 7 6 5
输出
0 4 0 20 0 12 0
'''
# 代码一
# 思路：结合中、先序想象
pre = list(map(int, input().strip().split()))
mid = list(map(int, input().strip().split()))
le = len(mid)
# 这里不用isVisited=[False]*le,
# 原因：生成的le个False都为一个对象，其中一个改为True，就全部为True
# isVisited，res都是针对中序变的
isVisited = [False for _ in range(le)]
res = [0 for _ in range(le)]


def sumNode(node: int, isVisited, res):
    index = mid.index(node)
    isVisited[index] = True
    # 求和不用加自身的值，所以默认为0
    su = 0
    # 分index前和后 加
    for i in range(index):
      # 中序的节点左边只要跳过访问过的
        if not isVisited[i]:
            su += mid[i]
    for i in range(index+1, le):
      # 中序的节点右边一旦有访问过的index，说明index右边都是其他子树
        if not isVisited[i]:
            su += mid[i]
        else:
            break
    res[index] = su


for i in pre:
    # 先序是从上往下访问
    # 父节点是所有子节点的和，父节点的位置isVisited首先变为True
    # 子节点不能访问父节点的
    sumNode(i, isVisited, res)
print(' '.join(map(str, res)))

# 代码二
# 思路：满二叉树个数为奇数，他的二分法 算出来的节点是相应子树的根节点
# 满二叉树可以直接由中序决定性质
pre=list(map(int,input().strip().split()));
mid=list(map(int,input().strip().split()));
le=len(mid);
res=[0 for _ in range(le)];
def sumNode(mid,left,right,res):
    mi=(left+right)//2;
    if mi==left:
        res[mi]=0;
    else:
        res[mi]=sum(mid[left:mi])+sum(mid[mi+1:right]);
        sumNode(mid,left,mi,res);
        sumNode(mid,mi+1,right,res);
sumNode(mid,0,le,res)
print(' '.join(map(str,res)))
