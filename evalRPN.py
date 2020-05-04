# -*- encoding: utf-8 -*-
'''
@File    :   evalRPN.py
@Time    :   2019/12/20 19:16:25
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

# 根据逆波兰表示法，求表达式的值。
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
# 说明：
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

# 示例 1：

# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: ((2 + 1) * 3) = 9
def evalRPN(tokens) -> int:
    i = 0
    while tokens:
        now = tokens[i]
        if now in ["/", "+", "*", "-"]:
            now = tokens.pop(i)
            fir = tokens.pop(i-1)
            second = tokens.pop(i-2)
            tokens.insert(i-2, str(int(eval(second+now+fir))))
            i = i-2
        elif len(tokens) == 1:
            return tokens.pop()
        else:
            i += 1


c = ["2","1","+","3","*"]
print(evalRPN(c))
