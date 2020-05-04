# -*- encoding: utf-8 -*-
'''
@File    :   507. 完美数 正因子之和与数相等.py
@Time    :   2020/03/10 10:04:21
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   507. 完美数 正因子之和与数相等.py
'''

'''
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。

给定一个 整数 n， 如果他是完美数，返回 True，否则返回 False
示例：

输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14
'''
# 代码一：
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        su=1;
        if num==1:return False;
        i=2;
        while i**2<=num:
            su+=i+num/i if num%i==0 else 0;
            i+=1 
        return su==num
# 代码二 scala
object Solution {
    def checkPerfectNumber(num: Int): Boolean = {
        if (num==1){
            false
        }else{
            var su=1;
            for (i <- 2 to math.sqrt(num).toInt if num%i==0){
                su+= i+num/i 
            }
            su==num
        }

    }
}