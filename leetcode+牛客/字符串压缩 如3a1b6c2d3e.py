# -*- encoding: utf-8 -*-
'''
@File    :   字符串压缩.py
@Time    :   2020/03/02 10:57:49
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   字符串压缩.py
'''

'''
题目描述
对字符串进行RLE压缩，将相邻的相同字符，用计数值和字符值来代替。例如：aaabccccccddeee，则可用3a1b6c2d3e来代替。

输入描述:
输入为a-z,A-Z的字符串，且字符串不为空，如aaabccccccddeee
输出描述:
压缩后的字符串，如3a1b6c2d3e
示例1
输入
aaabccccccdd
输出
3a1b6c2d
'''
# "0"的作用是循环到字符串最后还能把(k,v)添加到res中 结果才对
p = input().strip()+"0"
res=""
le=len(p)
k,v=p[0],1
for i in range(1,le):
    s=p[i];
    if s!=k:
        res+=str(v)+k;
        k=s;
        v=1;
    else:
        v+=1;
print(res)
    
