# -*- encoding: utf-8 -*-
'''
@File    :   1005. K 次取反后最大化的数组和.py
@Time    :   2020/02/14 10:54:54
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   1005. K 次取反后最大化的数组和.py
'''


'''
给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）

以这种方式修改数组后，返回数组可能的最大和。

 

示例 1：

输入：A = [4,2,3], K = 1
输出：5
解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
示例 2：

输入：A = [3,-1,0,2], K = 3
输出：6
解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
'''
# 代码一
# 始终只对最小值求反


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for i in range(K):
            A.sort()
            A[0] = -A[0]
        return sum(A)


# 代码二
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        tmin = 0
        le = len(A)
        # 始终只对最小值求反
        for i in range(le):
            if A[i] < 0:
                A[i] *= -1
                tmin = tmin if A[tmin] < A[i] else i
                K -= 1
                if K == 0:
                    break
            else:
              # 此时A全是正数，就对最小值反复求反
                tmin = tmin if A[tmin] < A[i] else i
                if K % 2 != 0:
                    A[tmin] *= -1
                break
        return sum(A)
