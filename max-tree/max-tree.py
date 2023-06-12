class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, front=None, back=None):
        self.front = front  
        self.back = back  

    def enqueue(self, value):
        node = QueueNode(value)
        if self.front is None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    def dequeue(self):
        if self.front is None:
            raise Exception("The queue is empty, you cannot dequeue from it")
        else:
            temp = self.front
            self.front = temp.next
            if self.front is None:
                self.back = None
            temp.next = None
            return temp.data

    def is_empty(self):
        return self.front is None


class Tnode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def max(self):


        """
    Finds the maximum value in the binary tree.

    Returns:
        The maximum value in the tree. None if the tree is empty.

        This method performs a breadth-first search (BFS) traversal of the binary tree
        to find the maximum value. It starts from the root and iterates over the tree
        level by level. It uses a queue to enqueue the nodes. At each step, it compares
        the value of the current node with the current maximum. After traversing the
        entire tree, it returns the maximum value found.

    Complexity:
        O(n)
        """

        if not self.root:
            return self.root

        output = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():

            front = queue.dequeue()
            output.append(front.value)

            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)
        max = output[0]
        for element in output:
            if element>max:
                max = element

        return max





class BST(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Tnode(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left:
                self._add_recursive(node.left, value)
            else:
                node.left = Tnode(value)
        else:
            if node.right:
                self._add_recursive(node.right, value)
            else:
                node.right = Tnode(value)




