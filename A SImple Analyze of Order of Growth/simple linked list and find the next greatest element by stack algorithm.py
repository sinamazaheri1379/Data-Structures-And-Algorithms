import sys


class Box:
    def __init__(self, count_of_chocolate, box_id, previous_box=None, next_box=None):
        self.count_of_chocolate = count_of_chocolate
        self.box_id = box_id
        self.previous_box = previous_box
        self.next_box = next_box
        self.point = 0


class LinkedList:
    def __init__(self):
        self.headval = None
        self.last_entered = None

    def __add_box__(self, count_of_chocolate, box_id):
        if self.headval == None:
            box = Box(count_of_chocolate, box_id)
            self.headval = box
        elif self.headval.next_box == None:
            box = Box(count_of_chocolate, box_id, self.headval, None)
            self.headval.next_box = box
        else:
            box = Box(count_of_chocolate, box_id, self.headval, self.headval.next_box)
            self.headval.next_box.previous_box = box
            self.headval.next_box = box

    def __add_box_first__(self, count_of_chocolate, box_id):
        if self.last_entered == None:
            box = Box(count_of_chocolate, box_id)
            self.headval = box
            self.last_entered = box
        else:
            box = Box(count_of_chocolate, box_id, self.last_entered)
            self.last_entered.next_box = box
            self.last_entered = box

    def __getHeadValue__(self):
        return self.headval

    def __delete_headValue__(self):
        per_box = self.headval.previous_box
        next_nox = self.headval.next_box
        if next_nox != None:
            self.headval = next_nox
            next_nox.previous_box = per_box
            if per_box != None:
                per_box.next_box = next_nox
            return self.headval
        else:
            self.headval = per_box
            per_box.next_box = None
            return per_box

    def __go_next_box__(self):
        if self.headval.next_box != None:
            self.headval = self.headval.next_box
            return self.__getHeadValue__()
        else:
            return None

    def __go_prev_box__(self):
        if self.headval.previous_box != None:
            self.headval = self.headval.previous_box
            return self.__getHeadValue__()
        else:
            return None

    def __print_list__(self):
        box = self.headval
        while (box.previous_box != None):
            box = box.previous_box
        while (box != None):
            print(str(box.count_of_chocolate) + " " + str(box.box_id))
            box = box.next_box
n, m = map(int, sys.stdin.readline().split())
box_id = 0
boxes_list = LinkedList()
list_of_seen_boxes = list()
for i in range(n):
    boxes_list.__add_box_first__(int(sys.stdin.readline()), box_id)
    box_id += 1
list_of_seen_boxes.append(boxes_list.__getHeadValue__())
for i in range(m):
    command = input()
    if command == '1':
        list_of_seen_boxes.append(boxes_list.__delete_headValue__())
    elif command == "3":
        box = boxes_list.__go_next_box__()
        if box != None:
            list_of_seen_boxes.append(box)
    elif command == "4":
        box = boxes_list.__go_prev_box__()
        if box != None:
            list_of_seen_boxes.append(box)
    elif len(command.split(" ")) > 1 and command.split(" ")[0] == "2":
        count_of_chocolate = int(command.split(" ")[1])
        boxes_list.__add_box__(count_of_chocolate, box_id)
        box_id += 1


maximum_stack = []
the_correspond_box = []
maximum_stack.append(list_of_seen_boxes[0])
for i in range(1, len(list_of_seen_boxes)):
    next = list_of_seen_boxes[i]
    if maximum_stack:
        element = maximum_stack.pop()
        while element.count_of_chocolate < next.count_of_chocolate:
            next.point += 2
            if not maximum_stack:
                break
            element = maximum_stack.pop()

        if element.count_of_chocolate >= next.count_of_chocolate:
            maximum_stack.append(element)

    maximum_stack.append(next)
minimum_stack = []
minimum_stack.append(list_of_seen_boxes[len(list_of_seen_boxes) - 1])
for i in reversed(range(0, len(list_of_seen_boxes) - 1)):
    next = list_of_seen_boxes[i]
    if minimum_stack:
        element = minimum_stack.pop()
        while element.count_of_chocolate > next.count_of_chocolate:
            next.point += 1
            if not minimum_stack:
                break
            element = minimum_stack.pop()

        if element.count_of_chocolate <= next.count_of_chocolate:
            minimum_stack.append(element)

    minimum_stack.append(next)

max_point = 0
max_chocolate = 0
for box in list_of_seen_boxes:
    if box.point > max_point:
        max_point = box.point
        max_chocolate = box.count_of_chocolate
    elif box.point == max_point and max_chocolate < box.count_of_chocolate:
        max_chocolate = box.count_of_chocolate
print(max_chocolate)