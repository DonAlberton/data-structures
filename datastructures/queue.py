

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def enqueue(self, value: int) -> None:
        self.__size += 1

        if self.head is None:
            self.head = Node(value)
        elif self.tail is None:
            self.tail = Node(value)
            self.head.next = self.tail
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def dequeue(self) -> Node:
        if self.head is not None:
            self.__size -= 1
            head_node = self.head
            self.head = self.head.next

            head_node.next = None

            return head_node.value
        else:
            raise IndexError("dequeue from empty queue")

    def search(self, value) -> bool:
        def search_node(current_node):
            if current_node is None:
                return False

            if current_node.value == value:
                return True
            return search_node(current_node.next)

        return search_node(self.head)

    def traversal(self) -> list:
        queue_traversal = []

        def recursive_traversal(current_node):
            if current_node is not None:
                queue_traversal.append(current_node.value)
                recursive_traversal(current_node.next)

        recursive_traversal(self.head)
        return queue_traversal
