# -*- encoding: utf-8 -*-
'''
@File    :   180度旋转+有效+不同于X的个数.py
@Time    :   2020/03/12 12:47:58
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   180度旋转+有效+不同于X的个数.py
'''

'''
题目描述
我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。

如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？

输入描述:
输入正整数N
输出描述:
输出1到N中好数个数
示例1
输入
10
输出
4
说明
在[1, 10]中有四个好数： 2, 5, 6, 9。
注意 1 和 10 不是好数, 因为他们在旋转之后不变。
'''
# 代码一
N = int(input())


def getHao(N):
    P1 = [0, 1, 8, 2, 5, 6, 9]
    P2 = [0, 1, 8, 5, 2, 9, 6]
    cnt = 0
    for i in range(1, N+1):
        f = ""
        p = i
        while i:
            v = i % 10
            if v not in P1:
                break
            f = str(P2[P1.index(v)])+f
            i //= 10
        else:
            if int(f) != p:
                cnt += 1
    return cnt


print(getHao(N))


# 代码二
N = int(input())


def getHao(N):
    cnt = 0
    H, B = [2, 5, 6, 9], [3, 4, 7]
    for i in range(1, N+1):
      #  包含2、5、6、9中任意个，且不包含3、4、7的即为好数
        if any([int(c) in H for c in str(i)]) and not any([int(c) in B for c in str(i)]):
            cnt += 1
    return cnt


print(getHao(N))
