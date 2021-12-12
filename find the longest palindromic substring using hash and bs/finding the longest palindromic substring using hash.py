array_of_hashes = [0]
array_of_hashes_inverse = [0]


def hash_the_input(string_input):
    length = len(string_input)
    for i in range(1, length + 1):
        array_of_hashes.append(array_of_hashes[i - 1] + (ord(string_input[i - 1]) * pow(31, i - 1)))
    for j in reversed(range(1, length + 1)):
        array_of_hashes_inverse.append(array_of_hashes_inverse[length - j] + (ord(string_input[j - 1]) * pow(31, length - j)))


def hash_the_array(L, R):
    return array_of_hashes[R + 1] - array_of_hashes[L]


def reverse_hash(L, R):
    length = len(array_of_hashes) - 1
    return array_of_hashes_inverse[length - L] - array_of_hashes_inverse[length - R - 1]


def check_is_palindrome(LENGTH, string):
    n = len(string)
    L = 0
    while L + LENGTH <= n:
        if (hash_the_array(L, L + LENGTH - 1)/pow(31, L)) == (reverse_hash(L, L + LENGTH - 1)/pow(31, n - L - LENGTH)):
            return True
        L += 1
    return False


maximum = 1
string = input()
hash_the_input(string)
low = 1
high = len(string)
while low <= high:
    mid = int((low + high + 1) / 2)
    if check_is_palindrome(mid, string):
        maximum = max(maximum, mid)
        low = mid + 1
    else:
        high = mid - 1
print(maximum)