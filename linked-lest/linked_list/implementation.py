import pytest
class node : 
    def __init__(self , data):
        self.data = data
        self.next = None # Here when we initialize the linked list the next points to null 



class linked_list :
    def __init__(self):
        self.head = None # Here we wanna head points to null when the linked list is empty






    def insertToHead(self,value):
        new_node = node(value)
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
                """
    1- Create a new node with the given value.
    2-Check if the linked list is empty by verifying if self.head is None.
    3-If the linked list is empty, set self.head to the new node.
    4-If the linked list is not empty, traverse the linked list until the last node is reached. This is done by starting at self.head and following the next pointer until temp.next is None.
    5-Once the last node is reached, set temp.next to the new node, effectively appending it to the linked list. 
         
        """
        new_node = node(value)
        if self.head is None: # This means the list is empty
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None: # because here we wanna make temp.next = None (means the least element in list)
                temp = temp.next
            temp.next = new_node


    

    def insert_before(self, target, value):
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
        new_node = node(value)
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
        new_node = node(value)
        current = self.head
        while current.next is not None:
            if current.next.data == target:
                current = current.next
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            







    def kthFromEnd(self , k) : 
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




