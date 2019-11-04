def heapify(arr, index, heap_size):
    parent = index
    leftchild = 2 * index + 1
    rightchild = 2 * index + 2
    if leftchild < heap_size:
        if (len(arr[leftchild]) > len(arr[parent])) or (len(arr[leftchild]) == len(arr[parent]) and arr[leftchild] >  arr[parent]):
            parent = leftchild
    if rightchild < heap_size:
        if (len(arr[rightchild]) > len(arr[parent])) or (len(arr[rightchild]) == len(arr[parent]) and arr[rightchild] > arr[parent]):
            parent = rightchild
    if parent != index:
        arr[parent], arr[index] = arr[index], arr[parent]
        heapify(arr, parent, heap_size)

def heapsort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr


from sys import stdin

n = int(stdin.readline())

txt = []

for _ in range(n):
    t = stdin.readline()[:-1]
    txt.append(t)

txt = list(set(txt))

txt = heapsort(txt)

for v in txt:
    print(v)