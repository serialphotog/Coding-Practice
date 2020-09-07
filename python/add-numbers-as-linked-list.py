"""
Problem:
    You are given two linked-lists representing two non-negative integers. 
    The digits are stored in reverse order and each of their nodes contain 
    a single digit. Add the two numbers and return it as a linked list.


Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807
"""

# Singly-linked list implementation
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Problem solution
def solution(list1, list2):
    # Build the numbers from the lists
    num1 = build_number_from_list(list1)
    num2 = build_number_from_list(list2)
    result = num1 + num2
    return build_list_from_number(result)

def build_list_from_number(num):
    numStr = str(num)
    i = len(numStr) - 1
    ls = Node(int(numStr[i]))
    current = ls
    while i > 0:
        i = i - 1
        current.next = Node(int(numStr[i])) 
        current = current.next
    return ls

def build_number_from_list(ls):
    sz = get_list_size(ls)
    num = 0
    for i in range(0, sz):
        num = num + (get_list_item_at(ls, sz-1).val * (10**(sz-1)))
        sz = sz - 1
    return num

def get_list_item_at(ls, idx):
    if idx == 0:
        return ls

    i = 0
    current = ls
    while current.next:
        current = current.next
        i = i + 1
        if i == idx:
            return current

def get_list_size(ls):
    current = ls
    count = 1
    while current.next:
        current = current.next
        count = count + 1
    return count

# Test the solution
if __name__ == '__main__':
    list1 = Node(2)
    list1.next = Node(4)
    list1.next.next = Node(3)

    list2 = Node(5)
    list2.next = Node(6)
    list2.next.next = Node(4)

    result = solution(list1, list2)
    while result:
        print(result.val)
        result = result.next
