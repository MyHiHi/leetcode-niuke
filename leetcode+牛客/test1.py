def look(n):
    p = [0 for i in range(n+1)]
    p[0] = 1
    for i in range(n+1):
        for j in range(1, i):
            p[i] = max(p[i], j*p[i-j], j*(i-j))
    return p[n]


print(look(57))
