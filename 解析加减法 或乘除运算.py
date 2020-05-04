# -*- encoding: utf-8 -*-
'''
@File    :   解析加减法运算.py
@Time    :   2020/03/02 11:42:45
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   解析加减法运算.py
'''

'''
题目描述
解析加减法运算
如：
输入字符串："1+2+3" 输出："6"
输入字符串："1+2-3" 输出："0"
输入字符串："-1+2+3" 输出："4"
输入字符串："1" 输出："1"
输入字符串："-1" 输出："-1"

已知条件：输入的运算都是整数运算，且只有加减运算
要求：输出为String类型，不能使用内建的eval()函数

输入描述:
输入字符串："1+2+3"
输出描述:
输出："6"
'''
# 解析加减
s = input()
# end:初始化为1 ，可能有开头 为 -1
le, start, end, res = len(s), 0, 1, 0
while end < le:
    if s[end] in ['+', '-']:
        # 1+2+3-9
        # s[start:end] =>+1 、+2、+3、-9
        res += int(s[start:end])
        start = end
    end += 1
res += int(s[start:])
print(res)

# 解析乘除


def run(s: str):
    le = len(s)
    # start 用来获取表达式第一个数字
    start, end = True, 1
    res = 0
    while end < le:
        if s[end] == '/':
            if start:
                res = int(s[:end])
            start = False
            end += 1
            k = end
            while end < le and s[end].isdigit():
                end += 1
            res /= int(s[k:end])
        elif s[end] == '*':
            if start:
                res = int(s[:end])
            start = False
            end += 1
            k = end
            while end < le and s[end].isdigit():
                end += 1
            res *= int(s[k:end])
        else:
            end += 1
    return res


s = "12*3/2*5/6"
print(run(s))
