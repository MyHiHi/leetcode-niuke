# -*- encoding: utf-8 -*-
'''
@File    :   1260. 二维网格迁移.py
@Time    :   2020/03/02 10:20:12
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   1260. 二维网格迁移.py
'''

'''

给你一个 m 行 n 列的二维网格 grid 和一个整数 k。你需要将 grid 迁移 k 次。

每次「迁移」操作将会引发下述活动：

位于 grid[i][j] 的元素将会移动到 grid[i][j + 1]。
位于 grid[i][n - 1] 的元素将会移动到 grid[i + 1][0]。
位于 grid[m - 1][n - 1] 的元素将会移动到 grid[0][0]。
请你返回 k 次迁移操作后最终得到的 二维网格。
'''
# 代码一 就地迁移，传统思路
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        for _ in range(k):
            v=None
            for i in range(m):
                if v==None:
                    t=grid[i][0];
                else:t=v;
                for j in range(1,n):
                    k=grid[i][j];
                    grid[i][j]=t;
                    t=k;
                if i+1<m:
                    v=grid[i+1][0]
                    grid[i+1][0]=t;
                else:
                    grid[0][0]=t;
                    break;         
        return grid


# 代码二
# 将原始矩阵拉成一条直数组，每一次操作相当于循环右移动这个数值，然后重新填充进矩阵中。
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        myGrid=[];
        for p1 in grid:
            myGrid+=p1;
        newLen=len(myGrid)
        idx=k%newLen;
        line=myGrid[newLen-idx:]+myGrid[:newLen-idx];
        for i in range(m):
            for j in range(n):
                grid[i][j]=line.pop(0)         
        return grid