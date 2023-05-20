## Can successfully instantiate an empty linked list
import pytest
from linked_list.implementation import linked_list , Stack , Queue



   
def test_empty_ll_when_initalize():
    ll = linked_list()
    actual = ll.head
    expected = None
    assert actual == expected


# Can properly insert into the linked list

def test_insert_head():
    ll = linked_list()
    ll.insertToHead(5)
    temp = ll.head.data
    actual = temp
    expected = 5
    assert actual == expected







##The head property will properly point to the first node in the linked list
#here what i am doing is inserting multiple values to the list to check if the head will point to the last one we have added
#witch is the first because we are inserting in the head


def test_check_first():
    ll = linked_list()
    ll.insertToHead(5)
    ll.insertToHead(6)
    ll.insertToHead(7)
    ll.insertToHead(8)
    temp = ll.head.data
    actual = temp
    expected = 8
    assert actual == expected






## Can properly insert multiple nodes into the linked list
def test_insert_multiple():
    ll = linked_list()
    ll.insertToHead(5)
    ll.insertToHead(6)
    ll.insertToHead(7)
    ll.insertToHead(8)
    temp = []
    node = ll.head
    while node is not None:
        temp.append(node.data)
        node = node.next
    actual = temp
    expected = [8, 7, 6, 5]
    assert actual == expected





# Will return true when finding a value within the linked list that exists
def test_existence():
    ll = linked_list()
    ll.insertToHead(8)
    ll.insertToHead(6)
    ll.insertToHead(7)
    ll.insertToHead(5)
    temp  = ll.ifExist(7)
    actual = temp
    expected = True
    assert actual == expected





# Will return false when searching for a value in the linked list that does not exist
def test_not_existence():
    ll = linked_list()
    ll.insertToHead(5)
    ll.insertToHead(6)
    ll.insertToHead(7)
    ll.insertToHead(8)
    temp  = ll.ifExist(15)
    actual = temp
    expected = False
    assert actual == expected



# Can properly return a collection of all the values that exist in the linked list
def test_formating_string():
    ll = linked_list()
    ll.insertToHead(5)
    ll.insertToHead(6)
    ll.insertToHead(7)
    ll.insertToHead(8)
    temp  = ll.__str__()
    actual = temp
    expected = "{ 8 } -> { 7 } -> { 6 } -> { 5 } -> NULL"
    assert actual == expected




# Can successfully add a node to the end of the linked list
# Can successfully add multiple nodes to the end of a linked list
def test_end():
    ll = linked_list()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    temp = []
    node = ll.head
    while node is not None:
        temp.append(node.data)
        node = node.next
    actual = temp
    expected = [5, 6, 7, 8]
    assert actual == expected




#Can successfully insert a node before a node located i the middle of a linked list

def test_before():
    ll = linked_list()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    # now i have : head -> {5} -> {6} -> {7} -> {8} -> X
    ll.insert_before(7,90)
    # i should have this now : head -> {5} -> {6} -> {90} -> {7} -> {8} -> X
    temp = []
    node = ll.head
    while node is not None:
        temp.append(node.data)
        node = node.next
    actual = temp
    expected = [5, 6, 90 ,7, 8]
    assert actual == expected






#Can successfully insert a node before the first node of a linked list
def test_before_first():
    ll = linked_list()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    # now i have : head -> {5} -> {6} -> {7} -> {8} -> X
    ll.insert_before(5,90)
    # i should have this now : head -> {5} -> {6} -> {90} -> {7} -> {8} -> X
    temp = []
    node = ll.head
    while node is not None:
        temp.append(node.data)
        node = node.next
    actual = temp
    expected = [90, 5, 6 ,7, 8]
    assert actual == expected





#Can successfully insert after a node in the middle of the linked list
def test_after():
    ll = linked_list()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    # now i have : head -> {5} -> {6} -> {7} -> {8} -> X
    ll.insert_after(7,90)
    # i should have this now : head -> {5} -> {6} -> {7} -> {90} -> {8} -> X
    temp = []
    node = ll.head
    while node is not None:
        temp.append(node.data)
        node = node.next
    actual = temp
    expected = [5, 6, 7 ,90, 8]
    assert actual == expected

# Can successfully insert a node after the last node of the linked list
def test_after_last():
    ll = linked_list()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    # now i have : head -> {5} -> {6} -> {7} -> {8} -> X
    ll.insert_after(8,90)
    # i should have this now : head -> {5} -> {6} -> {7} -> {90} -> {8} -> X
    temp = []
    node = ll.head
    while node is not None:
        temp.append(node.data)
        node = node.next
    actual = temp
    expected = [5, 6, 7 ,8, 90]
    assert actual == expected






# Code challenge 07 : 
#Where k is greater than the length of the linked list

def test_out_of_range():
    ll = linked_list()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    # now i have : head -> {5} -> {6} -> {7} -> {8} -> X
    ll.kthFromEnd(20)
    temp = []
    node = ll.head
    while node is not None:
        temp.append(node.data)
        node = node.next
    if 20 > len(temp) : 
        raise IndexError("Index out of range")
    





# Where k and the length of the list are the same

def test_k_and_list_same():
    #this one should return the last element
    ll = linked_list()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    # now i have : head -> {5} -> {6} -> {7} -> {8} -> X
    ll.kthFromEnd(3)
    temp = []
    node = ll.head
    while node is not None:
        temp.insert(0,node.data)
        node = node.next
    
    actual = temp[len(temp) - 1]
    expected = 5
    assert actual == expected




# Where k is not a positive integer 

def test_not_positive():
    #this one should return the last element
    ll = linked_list()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)  
    # now i have : head -> {5} -> {6} -> {7} -> {8} -> X
    ll.kthFromEnd(-2)
    temp = []
    node = ll.head
    while node is not None:
        temp.insert(0,node.data)
        node = node.next    
    actual = temp[-2]
    expected = 6
    assert actual == expected






# Where the linked list is of a size 1


def test_size_one():
    #this one should return the last element
    ll = linked_list()
    ll.append(5)
    # now i have : head -> {5} -> X
    ll.kthFromEnd(8)
    temp = []
    node = ll.head
    while node is not None:
        temp.insert(0,node.data)
        node = node.next    
    actual = temp[0]
    expected = 5
    assert actual == expected







# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_happy():
    ll = linked_list()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    # now i have : head -> {5} -> {6} -> {7} -> {8} -> X
    ll.kthFromEnd(2)
    temp = []
    node = ll.head
    while node is not None:
        temp.insert(0,node.data)
        node = node.next

    actual = temp[2]
    expected = 6
    assert actual == expected




    # Code challenge 08 


# Can successfully push onto a stack
# Can successfully push multiple values onto a stack

def test_pushing():
    s = Stack()
    s.push("ali")
    s.push("mohammed")
    s.push("sarah")
    s.push("alia")
    s.push("leo messi")

    # now i have : leo messi -> alia -> sarah -> mohammed -> ali -> None
    count = 0
    current = s.top
    while current : 
        current = current.next
        count+= 1 
    actual = count
    expected = 5
    assert actual == expected




# Can successfully pop off the stack
def test_popping():
    s = Stack()
    s.push("ali")
    s.push("mohammed")
    s.push("sarah")
    s.push("alia")
    s.push("leo messi")

    # now i have : leo messi -> alia -> sarah -> mohammed -> ali -> None
    count = 0
    current = s.top
    while current : 
        current = current.next
        count+= 1 
    s.pop()
    count-=1
    actual = count
    expected = 4
    assert actual == expected



# Can successfully empty a stack after multiple pops

def test_popping_till_empty():
    s = Stack()
    s.push("ali")
    s.push("mohammed")
    s.push("sarah")
    s.push("alia")
    s.push("leo messi")

    # now i have : leo messi -> alia -> sarah -> mohammed -> ali -> None
    count = 5
    current = s.top


    s.pop()
    count-=1
    s.pop()
    count-=1
    s.pop()
    count-=1
    s.pop()
    count-=1
    s.pop()
    count-=1

    actual = count
    expected = 0
    assert actual == expected


# Can successfully peek the next item on the stack

def test_peek():
    s = Stack()
    s.push("ali")
    s.push("mohammed")
    s.push("sarah")
    s.push("alia")
    s.push("leo messi")

    # now i have : leo messi -> alia -> sarah -> mohammed -> ali -> None

    ac= s.peek()

    actual = ac
    expected = "leo messi"
    assert actual == expected



# Can successfully instantiate an empty stack


def test_instantiate_empty():
    s = Stack()
    ac = s.top
    actual = ac
    expected = None
    assert actual == expected



# Calling pop or peek on empty stack raises exception
def test_peek_empty():
    s = Stack()
    ac = s.peek()

    actual = ac
    expected = "Mones"
    assert actual == expected










# Can successfully enqueue into a queue
# Can successfully enqueue multiple values into a queue
def test_enqueue():
    q = Queue()
    q.enqueue("Mones")
    q.enqueue("Mohammed")
    q.enqueue("Mary")
    q.enqueue("Jennifer aniston")
    q.enqueue("mark walberg")

    actual = q.back.data
    expected = "mark walberg"
    assert actual == expected


# Can successfully dequeue out of a queue the expected value
def test_denqueue():
    q = Queue()
    q.enqueue("Mones")
    q.enqueue("Mohammed")
    q.enqueue("Mary")
    q.enqueue("Jennifer aniston")
    q.enqueue("mark walberg")
    
    q.dequeue()

    actual = q.front.data
    expected = "Mohammed"
    assert actual == expected



# Can successfully peek into a queue, seeing the expected value
def test_denqueue_peek():
    q = Queue()
    q.enqueue("Mones")
    q.enqueue("Mohammed")
    q.enqueue("Mary")
    q.enqueue("Jennifer aniston")
    q.enqueue("mark walberg")
    


    actual = q.peek()
    expected = "Mones"
    assert actual == expected



# Can successfully empty a queue after multiple dequeues
def test_denqueue_till_empty():
    q = Queue()
    q.enqueue("Mones")
    q.enqueue("Mohammed")
    q.enqueue("Mary")
    q.enqueue("Jennifer aniston")
    q.enqueue("mark walberg")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()


    actual = q.front
    expected = None
    assert actual == expected


# Can successfully instantiate an empty queue
def test_instantiate_empty():
    q = Queue()
    ac = q.front
    actual = ac
    expected = None
    assert actual == expected



# Calling dequeue or peek on empty queue raises exception
def test_calling_empty():
    q = Queue()
    ac = q.dequeue()
    actual = ac
    expected = None
    assert actual == expected


