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

    def breadth_first(self):
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

        return output

    def depth_first_pre_order(self):
        result = []
        def _walk(node):
            if node:
                result.append(node.value)  
                _walk(node.left)   
                _walk(node.right)
                

        _walk(self.root)
        return result 
    def depth_first_in_order(self):
        result = []
        def _walk(node):
            if node:
                _walk(node.left)   
                result.append(node.value)  
                _walk(node.right)  
        
        _walk(self.root)
        return result 

    def depth_first_post_order(self):
        result = []
        def _walk(node):
            if node:
                _walk(node.left)   
                _walk(node.right)  
                result.append(node.value)  

        _walk(self.root)
        return result 


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

    def contains(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._contains_recursive(node.left, value)
        else:
            return self._contains_recursive(node.right, value)



