import pytest
class node : 
    def __init__(self , data):
        self.data = data
        self.next = None # Here when we initialize the linked list the next points to null 



class linked_list :
    def __init__(self):
        self.head = None # Here we wanna head points to null when the linked list is empty






    def insertToHead(self,value):
        self.head = node(value)
        self.head.data = value
        self.head.next = None


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



if __name__=="__main__" :
    LL = linked_list()
    LL.insertToHead(7)
    LL.insertToHead(3)
    LL.insertToHead(8)
    LL.insertToHead(3)
    LL.insertToHead(8)

    print(LL.head.data)
    print(LL.ifExist(3))
    ll = linked_list()
    ll.insertToHead(3)
    ll.insertToHead(2)
    ll.insertToHead(1)
    print(ll.__str__())
    



 




