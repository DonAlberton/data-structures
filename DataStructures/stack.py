

class Node:
    def __init__(self, value):
        self.value = value
        self.last = None


class Stack:
    def __init__(self):
        self.head = None
        self.__size = 0

    def push(self, value):
        self.__size += 1

        if self.head is None:
            self.head = Node(value)
        else:
            temp = self.head
            self.head = Node(value)
            self.head.last = temp

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        else:
            popped = self.head.value
            self.head = self.head.last
            return popped

    def traversal(self):
        stack_traversal = []

        def __traversal(current_node):
            if current_node is not None:
                stack_traversal.append(current_node.value)
                __traversal(current_node.last)

        __traversal(self.head)
        return stack_traversal
