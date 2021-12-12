class MaxHeap:
    def __init__(self, max_count):
        self.list = [0] * max_count
        self.current_size = 0

    def insert(self, element):
        self.list[self.current_size] = element
        self.current_size += 1
        current = self.current_size - 1
        while current != 0 and self.list[current] > self.list[(current - 1) // 2]:
            self.list[current], self.list[(current - 1) // 2] = \
                self.list[(current - 1) // 2], self.list[current]
            current = (current - 1) // 2

    def max_heapify(self, index):
        if index + 1 <= self.current_size // 2:
            left = -1
            right = -1
            if index * 2 + 3 <= self.current_size:
                left = self.list[index * 2 + 1]
                right = self.list[index * 2 + 2]
            elif index * 2 + 2 <= self.current_size:
                left = self.list[index * 2 + 1]
            if self.list[index] < left or self.list[index] < right:
                if left > right:
                    self.list[index], self.list[index * 2 + 1] = self.list[index * 2 + 1], self.list[index]
                    self.max_heapify(index * 2 + 1)
                else:
                    self.list[index], self.list[index * 2 + 2] = self.list[index * 2 + 2], self.list[index]
                    self.max_heapify(index * 2 + 2)

    def get_max(self):
        if self.current_size > 0:
            return self.list[0]
        else:
            return 10000000000

    def pop_max(self):
        if self.current_size > 0:
            root = self.list[0]
            self.list[0], self.list[self.current_size - 1] = self.list[self.current_size - 1], self.list[0]
            self.current_size -= 1
            if self.current_size > 1:
                self.max_heapify(0)
            return root
        else:
            return None


class MinHeap:
    def __init__(self, max_amount):
        self.list = [0] * max_amount
        self.current_size = 0

    def insert(self, element):
        self.list[self.current_size] = element
        self.current_size += 1
        current = self.current_size - 1
        while current != 0 and self.list[current] < self.list[(current - 1) // 2]:
            self.list[current], self.list[(current - 1) // 2] = \
                self.list[(current - 1) // 2], self.list[current]
            current = (current - 1) // 2

    def min_heapify(self, index):
        if index + 1 <= self.current_size // 2:
            left = 10000000000
            right = 10000000000
            if index * 2 + 3 <= self.current_size:
                left = self.list[index * 2 + 1]
                right = self.list[index * 2 + 2]
            elif index * 2 + 2 <= self.current_size:
                left = self.list[index * 2 + 1]
            if self.list[index] > left or self.list[index] > right:
                if left < right:
                    self.list[index], self.list[index * 2 + 1] = self.list[index * 2 + 1], self.list[index]
                    self.min_heapify(index * 2 + 1)
                else:
                    self.list[index], self.list[index * 2 + 2] = self.list[index * 2 + 2], self.list[index]
                    self.min_heapify(index * 2 + 2)

    def get_min(self):
        if self.current_size > 0:
            return self.list[0]
        else:
            return -1

    def pop_min(self):
        if self.current_size > 0:
            root = self.list[0]
            self.list[0], self.list[self.current_size - 1] = self.list[self.current_size - 1], self.list[0]
            self.current_size -= 1
            if self.current_size > 1:
                self.min_heapify(0)
            return root
        else:
            return None

days = int(input())
min_heap = MinHeap(days)
max_heap = MaxHeap(days)
for i in range (days):
    number = int(input())
    if number > min_heap.get_min():
        min_heap.insert(number)
    else:
        max_heap.insert(number)
    while max_heap.current_size>min_heap.current_size :
        min_heap.insert(max_heap.pop_max())
    while min_heap.current_size > max_heap.current_size+1:
        max_heap.insert(min_heap.pop_min())
    if min_heap.current_size == max_heap.current_size :
        print(max_heap.get_max())
    else:
        print(min_heap.get_min())



