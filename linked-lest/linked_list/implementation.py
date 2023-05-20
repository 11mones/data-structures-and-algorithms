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
        new_node = node(value)
        if self.head is None: # This means the list is empty
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None: # because here we wanna make temp.next = None (means the least element in list)
                temp = temp.next
            temp.next = new_node


    

    def insert_before(self, target, value):
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




