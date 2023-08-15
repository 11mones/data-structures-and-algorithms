
from functools import reduce
from operator import add

class Node:
  '''
  A class represent a node in a linked list or other data structure each node has two main componenet the value of the node and the reference to the next node.
  args: value
  return : nothing
  '''
  def __init__(self, value):
      self.next=None 
      self.value=value


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




class LinkedList:
    '''
    A class representing a singly linked list data structure
    '''
    def __init__(self):
        self.head = None

    def insert(self, value):
        '''
        insert a new node with the given value at the beginning of the linked list.
        args: value
        output: none
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

class HashTable:
  '''
  what : data structure that store key-value pairs of data using buckets to increace data accessing efficiency 
  
  '''
  def __init__(self,size=1024):
    self.__size=size
    self.__buckets=[None] *size
    self.keys = []
    
  
  def __hash(self,key):
    '''
    A method to return the hash code of the given key
    arg : key
    output: hash code of the key(index)
    '''
    # code = 0
   
    # for char in key:
    #   code += ord(str(char)) # * weight
    # code *= 255
    # code = code % 1024
    # return code
    return reduce(add, [ord(str(char)) for char in key]) * 283 % self.__size
    return sum([ord(str(char)) for char in key]) * 283 % self.__size

  
    
  def set(self,key,value):
    '''
    Set a key-value pair in the bucket, handling collisions as              needed.
    Arguments:
    key : The key to be hashed and used as the identifier for the           value.
    value : the value that is aassociated with the key
    Returns: None
    '''
    index = self.__hash(key)
    if self.__buckets[index] is None:
      ll = LinkedList()
      self.__buckets[index] = ll
     
    self.__buckets[index].insert([key,value])
    self.keys.append(key)
    
    

 

  def get(self,key):
    '''
    Retrieve the value with the given key from the hashtable
    arg : key
    return : value or None 
    '''
    index=self.__hash(key)
    bucket = self.__buckets[index]
    if bucket is not None : 
      curr = bucket.head
      while curr :
        if curr.value[0] == key :
          return curr.value[1]
        curr = curr.next  
    return None  
    
    

  def has(self, key):
    '''
    A method to check if the given key exist in the hashtable.
    arg: key
    output: boolean
    '''
    # index=self.__hash(key)
    # bucket = self.__buckets[index]
    # if bucket is not None : 
    #   curr = bucket.head
    #   while curr :
    #     if curr.value[0] == key :
    #       return True
    #     curr = curr.next  
    #   return False  
    if self.get(key):
      return True
    return False  

    

  def keys(self):
    '''
    args : none
    Returns a list of all the  keys present in the Hashtable.
    '''
    return self.keys



def intersection(t1,t2) :
    hash_table = HashTable()
    l = []
    if(t1.root == None or t2.root ==None):
        return l
    
    def traverse(t1):
        
        if(t1 != None):
            hash_table.set(t1.root.data)
            traverse(t1.right)
            traverse(t1.left)
        
    traverse(t1)
    
    def traverse2(t2):
        if(t2 != None):
            if(hash_table.has(t2.root)):
                l.append(t2.data)
            traverse2(t2.right)
            traverse(t2.left)
    traverse(t2)
    
    return l