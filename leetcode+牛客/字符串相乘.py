# -*- encoding: utf-8 -*-
'''
@File    :   字符串相乘.py
@Time    :   2020/04/14 19:08:01
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   字符串相乘.py
'''

# 代码一
# 字符串相加


def strAdd(s1, s2):
    res, carry = '', 0
    l1, l2 = len(s1)-1, len(s2)-1
    while l1 >= 0 and l2 >= 0:
        a, b = s1[l1], s2[l2]
        r = int(a)+int(b)+carry
        carry = r//10
        res = str(r % 10)+res
        l1 -= 1
        l2 -= 1

    def continueAdd(l, s, carry):
        nonlocal res
        while l >= 0:
            a = s[l]
            r = int(a)+carry
            carry = r//10
            res = str(r % 10)+res
            l -= 1
    if l1 >= 0:
        continueAdd(l1, s1, carry)
    elif l2 >= 0:
        continueAdd(l2, s2, carry)
    return res

# 找到末尾有几个0


def findZero(s):
    t, i, n = s[-1], len(s)-1, 0
    while t == '0':
        i -= 1
        t = s[i]
        n += 1
    return s[:i+1], n


def strMulti(n, s):
    f = [str(n*int(i)) for i in s[::-1]]
    res = f[0]
    i = -1
    for s in f[1:]:
        res = strAdd(s, res[:i])+res[i:]
        i -= 1
    return res


s1 = input()
s2 = input()
# 提取出末尾的0
s1, a = findZero(s1)
s2, b = findZero(s2)
zero = a+b
s1 = int(s1)
s2 = int(s2)
if (len(str(s1)) > len(str(s2))):
    print(strMulti(s1, str(s2))+'0'*zero)
else:
    print(strMulti(s2, str(s1))+'0'*zero)

# 代码二


def strMulti(s1, s2):
    n1 = int(s1)
    t = [int(i)*n1 for i in s2[::-1]]

    member, ans, i = t[0], '', 1
    while i < len(t):
        ans = str(member % 10)+ans
        member //= 10
        member += t[i]
        i += 1
    ans = str(member)+ans
    return ans


s1, s2 = input(), input()
print(strMulti(s1, s2))
