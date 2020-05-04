def func(n, mp):
    if n == 1 or n == 2:
        return 1
    # 存储中间变量
    if mp.get(n):
        return mp.get(n)
    else:
        mp[n] = func(n-1, mp)+func(n-2, mp)
    return func(n-1, mp)+func(n-2, mp)


print(func(10, {}))
