# -*- encoding: utf-8 -*-
'''
@File    :   整理房间.py
@Time    :   2020/02/13 13:26:56
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''
'''
题目描述
又到了周末，小易的房间乱得一团糟。
他希望将地上的杂物稍微整理下，使每团杂物看起来都紧凑一些，没有那么乱。
地上一共有n团杂物，每团杂物都包含4个物品。第i物品的坐标用(ai,bi)表示，
小易每次都可以将它绕着(xi,yi)逆时针旋转90^ \circ90 
∘
 ，这将消耗他的一次移动次数。如果一团杂物的4个点构成了一个面积不为0的正方形，我们说它是紧凑的。
因为小易很懒，所以他希望你帮助他计算一下每团杂物最少需要多少步移动能使它变得紧凑。
输入描述:
第一行一个数n(1 <= n <= 100)，表示杂物的团数。
接下来4n行，每4行表示一团杂物，每行4个数ai, bi，xi, yi, (-104 <= xi, yi, ai, bi <= 104)，表示第i个物品旋转的它本身的坐标和中心点坐标。
输出描述:
n行，每行1个数，表示最少移动次数。
示例1
输入
4
1 1 0 0
-1 1 0 0
-1 1 0 0
1 -1 0 0
1 1 0 0
-2 1 0 0
-1 1 0 0
1 -1 0 0
1 1 0 0
-1 1 0 0
-1 1 0 0
-1 1 0 0
2 2 0 1
-1 0 0 -2
3 0 0 -2
-1 1 -2 0
输出
1
-1
3
3
'''
# p(a,b)绕(x,y)逆时针旋转90度：[x+y-b,y-x+a]


def rotate(p, x, y):
    return [x+y-p[1], y-x+p[0]]

# 两点距离


def dis(a, b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

# 判断正方形
def isSquare(a, b, c, d):
  # 枚举所有可能的距离
    d = [dis(a, b), dis(a, c), dis(a, d), dis(b, c), dis(b, d), dis(c, d)]
    d.sort()
    if d[0] and d[0] == d[1] == d[2] == d[3] and d[4] == d[5] == 2*d[3]:
        return True
    return False


n = int(input().strip())
for w in range(n):
    res = 100
    p = []
    for i in range(4):
        a, b, x, y = map(int, input().strip().split())
        # 第w团杂物的第一个坐标是没有逆时针90度的
        temp = [[a, b]]
        for _ in range(3):
          # 分别在上一个坐标的基础上旋转，依次存入temp
            temp += [rotate(temp[-1], x, y)]
        # temp代表第i坐标 旋转0、1、2、3次后的坐标
        # 逆时针转四次就转回去了
        p += [temp]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                  # i,j,k,l就分别代表旋转次数
                    if isSquare(p[0][i], p[1][j], p[2][k], p[3][l]):
                        res = min(res, i+j+k+l)
    print(-1 if res == 100 else res)
