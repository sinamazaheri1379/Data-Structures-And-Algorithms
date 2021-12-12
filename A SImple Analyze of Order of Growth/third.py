import sys
sys.setrecursionlimit(10 ** 8)


n = int(input())
sequence = list(map(int, input().split()))


def calculate(array):
    if len(array) == 1:
        return max(0, array[0])
    maximum1 = calculate(array[0: int(len(array) / 2)])
    maximum2 = calculate(array[int(len(array) / 2):])
    max_sum_j = 0
    sum_j = 0
    for j in range(int(len(array) / 2), len(array)):
        sum_j += array[j]
        max_sum_j = max(max_sum_j, sum_j)
    sum_i = 0
    max_sum_i = 0
    for i in reversed(range(int(len(array) / 2))):
        sum_i += array[i]
        max_sum_i = max(sum_i, max_sum_i)
    return max(maximum1, maximum2, max_sum_j + max_sum_i)


print(calculate(sequence))
