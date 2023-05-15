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
    

    



    



 




