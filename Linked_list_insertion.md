# LinkedList insertion
We want to create 3 methods for the insertion in the linked list.

## Whiteboard Process
### append
![algo (9)](https://github.com/11mones/data-structures-and-algorithms/assets/72322641/1c077617-71f8-473e-9847-cca4b4e2c915)
### insert before
![algo (8)](https://github.com/11mones/data-structures-and-algorithms/assets/72322641/6b402d96-ca3d-4fed-b548-b56fc577adf4)
### insert after
![algo (7)](https://github.com/11mones/data-structures-and-algorithms/assets/72322641/2d95cf98-b7b0-43f7-8bcd-24d5bc1c71e9)










## Approach & Efficiency
Everything works correctly in the three methods and the edge cases is covered in the tests and in the methods itself, the methods is Big(n) complexity.

## Solution
**Append method :**



    1- Create a new node with the given value.
    2-Check if the linked list is empty by verifying if self.head is None.
    3-If the linked list is empty, set self.head to the new node.
    4-If the linked list is not empty, traverse the linked list until the last node is reached. This is done by starting at self.head and following the next pointer until temp.next is None.
    5-Once the last node is reached, set temp.next to the new node, effectively appending it to the linked list.




**insert before method :**



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




**insert after method :**



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
