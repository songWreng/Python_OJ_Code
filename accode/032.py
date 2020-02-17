def min_heapify(A, i, size):
    left = 2*i + 1
    right = 2*i + 2
    if left < size and A[left] < A[i]: mini = left
    else: mini = i
    if right < size and A[right] < A[mini]: mini = right
    if mini != i:
        A[i], A[mini] = A[mini], A[i]
        min_heapify(A, mini, size)

def solve():
    p = list(map(int, input().split()))
    size = len(p)
    N = int(input())
    while N > 0:
        ord = input()
        if ord == 'D':
            p[0] = p[size - 1]
            del p[size - 1]
            size -= 1
            min_heapify(p, 0, size)

        else:
            num = int(input())
            p.append(num)
            size += 1
            min_heapify(p, (size - 1) // 2, size)
        N -= 1
    print(p)
solve()


