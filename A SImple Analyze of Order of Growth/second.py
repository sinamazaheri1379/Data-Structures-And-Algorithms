n = int(input())
sequence = list(map(int, input().split()))
cumsum = 0
for i in range(n):
    my_sum = 0
    for j in range(i, n):
        my_sum += sequence[j]
        if my_sum > cumsum:
            cumsum = my_sum
print(cumsum)