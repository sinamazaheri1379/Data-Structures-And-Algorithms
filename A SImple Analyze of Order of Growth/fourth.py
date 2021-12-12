n = int(input())
sequence = list(map(int, input().split()))
my_sequence = []
my_sum = 0
for i in range(n):
    my_sum += sequence[i]
    my_sequence.append(my_sum)
current_max = max(my_sequence[0], 0)
minimum = 0
for j in range(1, n):
    minimum = min(my_sequence[j - 1], minimum)
    current_max = max(my_sequence[j] - minimum, current_max)
print(current_max)

