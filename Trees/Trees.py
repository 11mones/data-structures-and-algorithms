class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def pre_order(self, root):
        result = []
        if root:
            result.append(root.data)
            result += self.pre_order(root.left)
            result += self.pre_order(root.right)
        return result

    def in_order(self, root):
        result = []
        if root:
            result += self.in_order(root.left)
            result.append(root.data)
            result += self.in_order(root.right)
        return result

    def post_order(self, root):
        result = []
        if root:
            result += self.post_order(root.left)
            result += self.post_order(root.right)
            result.append(root.data)
        return result

class BST(BinaryTree) : 
    def add(self, value):
        if self.root is None:
            self.root = Node(value, None, None)
        else:
            self._add_helper(self.root, value)

    def _add_helper(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = Node(value, None, None)
            else:
                self._add_helper(node.left, value)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value, None, None)
            else:
                self._add_helper(node.right, value)

    def contains(self, value):
        return self._contains_helper(self.root, value)

    def _contains_helper(self, node, value):
        if node is None:
            return False
        if value == node.data:
            return True
        elif value < node.data:
            return self._contains_helper(node.left, value)
        else:
            return self._contains_helper(node.right, value)
        

