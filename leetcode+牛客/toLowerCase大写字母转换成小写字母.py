# -*- encoding: utf-8 -*-
'''
@File    :   toLowerCase py
@Time    :   2020/01/25 08:33:32
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''
'''
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，
并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
'''

'''
大写变小写、小写变大写 : ASCII码 ^= 32
大写变小写、小写变小写 : ASCII码 |= 32
小写变大写、大写变大写 : ASCII码 &= -33

'''
'''
var toLowerCase = function(str) {
    let result = '';
    for(let i = 0;i < str.length;i++){
        result += String.fromCharCode(str.charCodeAt(i) | 32);
    }
    return result;
};
'''
class Solution:
    def toLowerCase(self, str: str) -> str:
        s=""
        for i in str:
            p=ord(i);
            if 65<=p<=90:p+=32;
            s+=chr(p);
        return s