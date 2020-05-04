# -*- encoding: utf-8 -*-
'''
@File    :   1013. 将数组分成和相等的三个部分.py
@Time    :   2020/02/15 12:45:28
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   1013. 将数组分成和相等的三个部分.py
'''

'''
给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果我们可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

 

示例 1：

输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
示例 2：

输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
示例 3：

输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
'''

# 从左右两边分别向里，判断是否都是三分之一
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        su = sum(A)
        avg = su//3
        if avg == 0:
            return False
        l, r = 0, 0
        le = len(A)
        i, j = 0, le-1
        while l != avg and i < le:
            l += A[i]
            i += 1
        while r != avg and j > -1:
            r += A[j]
            j -= 1
        # i<=j：必须的
        if l == r == avg and i <= j:
            return True
        return False
# scala


def canThreePartsEqualSum(A: Array[Int]): Boolean = {
    var avg = A.sum/3;
    if (avg == 0) false;
    else{
        var le = A.length
        var(l, r, i, j) = (0, 0, 0, le-1);
        println(l, r, i, j)
        while (l != avg & & i < le){
            l += A(i);
            i += 1;}
        while (r != avg & & j > -1){
            r += A(j);
            j -= 1;}
        print(l, r, avg)
        if(l == r & & r == avg & & i <= j){
            true
        } else{
            false
        }

    }

}
