# 递归
res=[]
def permutations(arr, position, end,res):

    if position == end:
        print(arr)
        res+=[arr[:]]

    else:
        for index in range(position, end):

            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position+1, end,res)
            arr[index], arr[position] = arr[position], arr[index]


arr = ["a", "b", "c"]
permutations(arr, 0, len(arr))

# 深度优先
visit = [True, True, True]
temp = ["" for x in range(0, 3)]


def dfs(position):
    if position == len(arr):
        print(temp)
        return

    for index in range(0, len(arr)):
        if visit[index] == True:
            temp[position] = arr[index]
            visit[index] = False
            dfs(position + 1)
            visit[index] = True

# arr = ["a","b","c"]
# dfs(0)
