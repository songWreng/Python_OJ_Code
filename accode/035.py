def Heapify(A, i, size):
    left = 2*i + 1
    right = 2*i + 2
    if left < size and A[left] > A[i]: largest = left
    else: largest = i
    if right < size and A[right] > A[largest]: largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Heapify(A, largest, size)

def BuildHeap(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        Heapify(A, i, len(A))

def solve():
    p = list(map(int, input().split(',')))
    n = int(input())

    BuildHeap(p)
    # print(p)
    size = len(p)
    for i in range(len(p) - 1, len(p) - n, -1):
        p[i], p[0] = p[0], p[i]
        size -= 1
        Heapify(p, 0, size)
        # print(p)

    print(p[0])

solve()

