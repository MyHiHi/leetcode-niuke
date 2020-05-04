# -*- encoding: utf-8 -*-
'''
@File    :   被3整除.py
@Time    :   2020/02/03 10:26:54
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
题目描述
小Q得到一个神奇的数列: 1, 12, 123,...12345678910,1234567891011...。

并且小Q对于能否被3整除这个性质很感兴趣。

小Q现在希望你能帮他计算一下从数列的第l个到第r个(包含端点)有多少个数可以被3整除。

输入描述:
输入包括两个整数l和r(1 <= l <= r <= 1e9), 表示要求解的区间两端。
输出描述:
输出一个整数, 表示区间内能被3整除的数字个数。
示例1
输入
2 5
输出
3
说明
12, 123, 1234, 12345...
其中12, 123, 12345能被3整除。
'''

# 思路一：通过
'''
    1, 12, 123, 1234, 12345 123456  1234567....

%3：1   0  0 ---  1    0     0   ---  1
[1,x]:中模3其中余数为1的个数：(x+2)//3
'''
import sys
lines = sys.stdin.readlines()
lines = [line.strip() for line in lines if line.strip()]
l, r = map(int, lines[0].split())
s1 = (l-1+2)//3
s2 = (r+2)//3
# 求[l,r] 模3 时 余数为1的总个数
s = s2-s1
# 用[1,r]总个数-1个数(余数为1,不能被3整除)
print(r-l+1-s)


# 思路二：
'''
序号    1  2   3    4      5     6       7      
        1 12, 123, 1234, 12345 123456  1234567....
序号%3  1  2   0    1      2     0       1
能否整除 N  Y   Y    N      Y     Y       N 
'''
# 代码一：这个准确率70% 超时了
lines = sys.stdin.readlines()
lines = [line.strip() for line in lines if line.strip()]
l, r = map(int, lines[0].split())
co = 0
for i in range(l, r+1):
    if i % 3 != 1:
        co += 1
print(co)

# 代码二：通过
lines = sys.stdin.readlines()
lines = [line.strip() for line in lines if line.strip()]
l, r = map(int, lines[0].split())

# [1,x]:N Y Y /  N Y Y /N Y Y
# 每三份就有2个Y


def get(m):
    su = m//3*2
    if m % 3 == 2:
        su += 1
        return su
    # 余数为0 或1 ，直接返回
    return su


print(get(r)-get(l-1))
