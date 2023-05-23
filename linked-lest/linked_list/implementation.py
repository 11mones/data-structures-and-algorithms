import pytest
class Node : 
    def __init__(self , data):
        self.data = data
        self.next = None # Here when we initialize the linked list the next points to null 



class linked_list :
    def __init__(self):
        self.head = None # Here we wanna head points to null when the linked list is empty






    def insertToHead(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def ifExist(self, value):
        
        node = self.head
        while node is not None:
            if node.data == value:
                return True
            node = node.next
        return False


    


    def __str__(self):
        node = self.head
        linked_list_str = ""
        while node:
            linked_list_str += f"{{ {str(node.data)} }} -> "
            node = node.next
        linked_list_str += "NULL"
        return linked_list_str
    

    


# code challenge 06 methods 


    def append(self, value):

        new_node = Node(value)

        """
    1- Create a new node with the given value.
    2-Check if the linked list is empty by verifying if self.head is None.
    3-If the linked list is empty, set self.head to the new node.
    4-If the linked list is not empty, traverse the linked list until the last node is reached. This is done by starting at self.head and following the next pointer until temp.next is None.
    5-Once the last node is reached, set temp.next to the new node, effectively appending it to the linked list. 
         
        """
        # new_node = node(value)

        if self.head is None: # This means the list is empty
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None: # because here we wanna make temp.next = None (means the least element in list)
                temp = temp.next
            temp.next = new_node


    

    def insert_before(self, target, value):

        new_node = Node(value)

        """
    1-Create a new node with the given value.
    2-Check if the linked list is empty by verifying if self.head is None. If it is, return without making any changes.
    3-Check if the target value is equal to the data of the head node. If it is, perform the following steps:
        -Set the next pointer of the new node to the current head node.
        -Set the head of the linked list to the new node.
        -Return from the method.
    4-Traverse the linked list starting from the head node:
        -Check if the data of the next node is equal to the target value.
        -If it is, perform the following steps:
            .Set the next pointer of the new node to the next pointer of the current node.
            .Set the next pointer of the current node to the new node.
            .Return from the method.
        -If the target value is not found, move to the next node by updating the current pointer to current.next.
    5-If the target value is not found in the linked list, the method will reach the end of the list without making any changes.

        """
        # new_node = node(value)
        if self.head is None:
            return
        if self.head.data == target:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            if current.next.data == target:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

   


    def insert_after(self, target, value):

        new_node = Node(value)

        """
    1-Create a new node with the given value.
    2-Traverse the linked list starting from the head node:
        -Check if the data of the current node is equal to the target value.
        -If it is, perform the following steps:
            .Move to the next node by updating the current pointer to current.next.
            .Set the next pointer of the new node to the next pointer of the current node.
            .Set the next pointer of the current node to the new node.
            .Return from the method.
        -If the target value is not found, move to the next node by updating the current pointer to current.next.
    3-If the target value is not found in the linked list, the method will reach the end of the list without making any changes.
        """
        # new_node = node(value)

        current = self.head
        while current.next is not None:
            if current.next.data == target:
                current = current.next
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            


    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()



# Code challenge 08
    @classmethod
    def zip_lists(cls, l1, l2):
        zipped = linked_list()
        temp = zipped.head
        po1 = l1.head
        po2 = l2.head

        while po1 and po2:
            new = Node(po1.data)
            if not zipped.head:
                zipped.head = new
                temp = zipped.head
            else:
                temp.next = new
                temp = temp.next

            sec = Node(po2.data)
            temp.next = sec
            temp = temp.next

            po1 = po1.next
            po2 = po2.next

        # Thats for the remaining (if l1 is longer than l2)
        while po1:
            new = Node(po1.data)
            temp.next = new
            temp = temp.next
            po1 = po1.next

        # Thats for the remaining (if l2 is longer than l1)
        while po2:
            sec = Node(po2.data)
            temp.next = sec
            temp = temp.next
            po2 = po2.next

        return zipped








    def kthFromEnd(self , k) : 

        """
        create an empty list l, set current to the head of the linked list then traverse the linked list using a while loop and 
        Insert the data of the current node at the beginning of the list l using l.insert(0, current.data), then we wanna check if k
        is equal to the length of the list l, If so return the first element of the list l, as it represents the kth node from the end,
        we want also to check if the length of the list l is equal to 1 to return the single element of linked list if it's length is 1
        and outside the loop we return the element at index k in the list l, which represents the kth node from the end of the
          linked list.

        """
        if k <0:
            raise IndexError("Tou entered negative value")
        l = []
        current = self.head
        while current is not None:
            l.insert(0,current.data)
            current = current.next
        if k == len(l) : 
            return l[0]
        elif len(l) == 1:
            return l[0]

        return l[k]




# Code challenge 10

class Stack:
    def __init__(self,top=None):
        self.top = top

    def push(self,value):
        """
    Pushes a value onto the top of the stack.
    Argument : The value to be pushed onto the stack.

        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
    Removes and returns the value from the top of the stack.
    Returns The value that was removed from the top of the stack.
    Raises Exception: If the stack is empty and there is nothing to pop.

        """
        #check if the statck is empty :
        if self.top == None: 
            raise Exception("The stack is empty you can not pop from it")
        else :
            temp= self.top
            self.top = temp.next
            temp.next = None
            return temp.data

    def peek(self):
        """
    Returns the value from the top of the stack without removing it.
    Returns The value at the top of the stack.
    Raises Exception: If the stack is empty and there is nothing to peek.

        """
        if self.top == None: 
            raise Exception("The stack is empty you can not peek from it")
        else : 
            return self.top.data

        
class Queue:
    def __init__(self,front=None,back=None):
        self.front = front # first node in th queue
        self.back=back    # last node in queue    




    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    def dequeue(self):
        """
    Adds an element to the back of the queue.
    Argsument is the value to be added to the queue.
        """
        if self.front is None:
            raise Exception("The queue is empty, you cannot dequeue from it")
        else:
            temp = self.front
            self.front = temp.next
            if self.front is None:
                self.back = None
            temp.next = None
            return temp.data


    def peek(self):
        """
    Returns the value of the element at the front of the queue without removing it.
    Raises an Exception: If the queue is empty.
    Returns The value of the element at the front of the queue.

        """
        if self.front == None: 
            raise Exception("The queue is empty you can not peek from it")
        else : 
            return self.front.data

    
    def __str__(self):
        current=self.front
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"  

# lo = linked_list()
# lo.append(5)
# lo.append(4)
# lo.append(3)
# lo.append(2)
# lo.append(1)
# lo.append(0)
# lo.append(-1)
# lo.append(-2)
# ll = linked_list()
# ll.append(5)
# ll.append(6)
# ll.append(7)
# ll.append(8)
# ll.append(9)  
# print(ll.__str__())
# print(ll.kthFromEnd(-2))

# l1 = linked_list()
# l2 = linked_list()
# l1.append(1)
# l1.append(2)
# l1.append(3)
# l1.append(4)

# l2.append(70)
# l2.append(80)
# l2.append(90)
# l2.append(100)
# l3 = linked_list()
# l3 = l3.zip_lists(l1,l2)






