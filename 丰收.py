# -*- encoding: utf-8 -*-
'''
@File    :   丰收.py
@Time    :   2020/02/12 11:07:14
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
题目描述
又到了丰收的季节，恰逢小易去牛牛的果园里游玩。
牛牛常说他对整个果园的每个地方都了如指掌，小易不太相信，所以他想考考牛牛。
在果园里有N堆苹果，每堆苹果的数量为ai，小易希望知道从左往右数第x个苹果是属于哪一堆的。
牛牛觉得这个问题太简单，所以希望你来替他回答。
输入描述:
第一行一个数n(1 <= n <= 105)。
第二行n个数ai(1 <= ai <= 1000)，表示从左往右数第i堆有多少苹果
第三行一个数m(1 <= m <= 105)，表示有m次询问。
第四行m个数qi，表示小易希望知道第qi个苹果属于哪一堆。
输出描述:
m行，第i行输出第qi个苹果属于哪一堆。
示例1
输入
5
2 7 3 4 9
3
1 25 11
输出
1
5
3
'''
import sys
c = sys.stdin.readlines()
c = [a.strip() for a in c]
n = int(c[0])
number = list(map(int, c[1].split()))
m = int(c[2])
apples = list(map(int, c[3].split()))
# 积累
for i in range(1, n):
    number[i] += number[i-1]
res = []
for i in apples:
  # 二分查找
  # import bisect
  # 用了python的二分查找插入模块bisect
  # bisect_left能够找到最接近并大于待查找数qi应该插入的位置
  #  res+=[ bisect.bisect_left(number, i) + 1]
    fi, la = 0, n-1
    while fi < la:
        mid = (fi+la) >> 1
        if number[mid] < i:
            fi = mid+1
        else:
            la = mid
    res += [la+1]
   

for i in res:
    print(i)

