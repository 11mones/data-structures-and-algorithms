# k-th value from the end

kthFromEnd function that returns the Kth position node in the linked list starting from the tail. 

## Whiteboard Process


## Approach & Efficiency
The approach is : create an empty list l, set current to the head of the linked list then traverse the linked list using a while loop and Insert the data of the current node at the beginning of the list l using l.insert(0, current.data), then we wanna check if k is equal to the length of the list l, If so return the first element of the list l, as it represents the kth node from the end, we want also to check if the length of the list l is equal to 1 to return the single element of linked list if it's length is 1
and outside the loop we return the element at index k in the list l, which represents the kth node from the end of the linked list.


And the time complexity is **Big(n)**


## Solution
I have pushed the code 