# -*- encoding: utf-8 -*-
/*
@File    :   1071. 字符串的最大公因子.py
@Time    :   2020/02/21 16:37:47
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   1071. 字符串的最大公因子.py
*/

/*
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

 

示例 1：

输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
示例 2：

输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
*/
// scala
object Solution {
    def gcdOfStrings(str1: String, str2: String): String = {
        // 最大公约数
        def gcd(a:Int,b:Int):Int=if (b==0) a else gcd(b,a%b);
        if (str1+str2 != str2+str1){
            ""
        }
        else{
            str2.substring(0,gcd(str1.length,str2.length))
        }
    }
}

// python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(len(str1),-1,-1):
            v=str1[:i];
            if str1.replace(v,"") == str2.replace(v,"")=="":
                return v;
        return ""