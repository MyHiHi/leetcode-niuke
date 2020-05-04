# 最大堆
def bulid_max_heap(arr):
    for i in range(len(arr)//2, -1, -1):
        headify(arr, i)


def headify(arr, i):
    l, r, largest = 2*i+1, 2*i+2, i
    if l < le and arr[largest] < arr[l]:
        largest = l
    if r < le and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        swap(arr, i, largest)
        headify(arr, largest)


def swap(arr, i, j):
    arr[j], arr[i] = arr[i], arr[j]


def head_sort(arr):
    global le
    le = len(arr)
    bulid_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        # arr[0]为最大值，与最后一个值交换，然后长度-1，重新对新长度堆化
        swap(arr, 0, i)
        le -= 1
        headify(arr, 0)
    return arr


p = [12, 4, 5, 6, 2, 2, 5, 23, 6]
print(head_sort(p))
