# -*- encoding: utf-8 -*-
'''
@File    :   1042. 不邻接植花.py
@Time    :   2020/02/19 11:17:38
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   1042. 不邻接植花.py
'''

'''
有 N 个花园，按从 1 到 N 标记。在每个花园中，你打算种下四种花之一。

paths[i] = [x, y] 描述了花园 x 到花园 y 的双向路径。

另外，没有花园有 3 条以上的路径可以进入或者离开。

你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。

以数组形式返回选择的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1, 2, 3, 4 表示。保证存在答案。

 

示例 1：

输入：N = 3, paths = [[1,2],[2,3],[3,1]]
输出：[1,2,3]
示例 2：

输入：N = 4, paths = [[1,2],[3,4]]
输出：[1,2,1,2]
'''
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
      # 构建邻接表G，存储当前位置的相邻所有index
        res,G=[0 for _ in range(N)],[[] for _ in range(N)];
        for x,y in paths:
            G[x-1]+=[y-1];
            G[y-1]+=[x-1];
        for i in range(N):
          # 所有花色-相邻节点已经选的花色=当前i可选的花色（选其一就行）
            res[i]=({1,2,3,4}-{res[j] for j in G[i]}).pop();
        return res