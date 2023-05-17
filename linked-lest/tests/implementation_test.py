## Can successfully instantiate an empty linked list
import pytest
from linked_list.implementation import linked_list



   
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

# def test_out_of_range():
#     ll = linked_list()
#     ll.append(5)
#     ll.append(6)
#     ll.append(7)
#     ll.append(8)
#     # now i have : head -> {5} -> {6} -> {7} -> {8} -> X
#     ll.kthFromEnd(20)
#     temp = []
#     node = ll.head
#     while node is not None:
#         temp.append(node.data)
#         node = node.next
#     if 20 > len(temp) : 
#         raise IndexError("Index out of range")
    





# Where k and the length of the list are the same

def test_k_and_list_same2222():
    #this one should return the last element
    ll = linked_list()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    # now i have : head -> {5} -> {6} -> {7} -> {8} -> X
    ll.kthFromEnd(1)
    temp = []
    node = ll.head
    while node is not None:
        temp.insert(0,node.data)
        node = node.next
    if 4 == len(temp) : 
        return temp[0]


def test_k_and_list_same():
    #this one should return the last element
    ll = linked_list()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    # now i have : head -> {5} -> {6} -> {7} -> {8} -> X
    ll.kthFromEnd(1)
    temp = []
    node = ll.head
    while node is not None:
        temp.insert(0,node.data)
        node = node.next

    actual = temp[1]
    expected = 7
    assert actual == expected