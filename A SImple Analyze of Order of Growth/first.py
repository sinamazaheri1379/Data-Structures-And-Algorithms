n = int(input())
sequence = list(map(int, input().split()))
cumsum = 0
for i in range(n):
    for j in range(n):
        my_sum = 0
        for k in range(i, j + 1):
            my_sum += sequence[k]
        if my_sum > cumsum:
            cumsum = my_sum
print(cumsum)
