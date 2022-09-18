

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def insert(self, value: int) -> None:
        self.__size += 1

        def insert_node(current_node: Node):
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(value)
                    current_node.left.parent = current_node
                else:
                    insert_node(current_node.left)
            else:
                if current_node.right is None:
                    current_node.right = Node(value)
                    current_node.right.parent = current_node
                else:
                    insert_node(current_node.right)

        if self.root is None:
            self.root = Node(value)
        else:
            insert_node(self.root)

    def search(self, value: int) -> Node or False:
        def search_node(current_node):
            if current_node is not None:
                if value == current_node.value:
                    return current_node
                if value < current_node.value:
                    return search_node(current_node.left)
                elif value > current_node.value:
                    return search_node(current_node.right)
            return False

        if self.root is None:
            return False
        else:
            return search_node(self.root)

    def delete(self, value: int) -> None:
        self.__size -= 1

        def delete_node(node: Node):
            def find_max_value_node(current_node):
                if current_node.right is None:
                    return current_node
                else:
                    return find_max_value_node(current_node.right)

            node_parent = node.parent

            node_children = (1 if node.left is not None else 0) + (1 if node.right is not None else 0)

            if node_children == 0:
                if node_parent is not None:
                    if node_parent.left == node:
                        node_parent.left = None
                    else:
                        node_parent.right = None
                    del node
                else:
                    self.root = None

            elif node_children == 1:
                if node.left is not None:
                    child = node.left
                else:
                    child = node.right

                if node_parent is not None:
                    if node_parent.left == node:
                        node_parent.left = child
                    else:
                        node_parent.right = child
                else:
                    self.root = child

                node.parent = None
                del node

                child.parent = node_parent

            elif node_children == 2:
                successor = find_max_value_node(node.left)
                node.value = successor.value

                delete_node(successor)

        found_node = self.search(value)
        if found_node is False:
            raise ValueError("Value not found")
        else:
            delete_node(found_node)

    def height(self) -> int:
        def tree_height(current_node, height):
            if current_node is None:
                return height

            left = tree_height(current_node.left, height + 1)
            right = tree_height(current_node.right, height + 1)
            return max(left, right)

        if self.root is None:
            return 0
        return tree_height(self.root, 0)

    def preorder(self) -> list:
        sorted_list = []

        def __preorder(current_node):
            if current_node is not None:
                sorted_list.append(current_node.value)
                __preorder(current_node.left)
                __preorder(current_node.right)

        __preorder(self.root)
        return sorted_list

    def inorder(self) -> list:
        sorted_list = []

        def __inorder(current_node):
            if current_node is not None:
                __inorder(current_node.left)
                sorted_list.append(current_node.value)
                __inorder(current_node.right)

        __inorder(self.root)
        return sorted_list

    def postorder(self) -> list:
        sorted_list = []

        def __postorder(current_node):
            if current_node is not None:
                __postorder(current_node.left)
                __postorder(current_node.right)
                sorted_list.append(current_node.value)

        __postorder(self.root)
        return sorted_list


def reverse(binary_tree: BinaryTree) -> None:
    def reverse_binary_tree(current_node: type[Node]):
        if current_node is None:
            return

        reverse_binary_tree(current_node.left)
        reverse_binary_tree(current_node.right)

        current_node.right, current_node.left = current_node.left, current_node.right
    reverse_binary_tree(binary_tree.root)
