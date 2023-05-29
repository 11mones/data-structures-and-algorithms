# Implement a Queue using two Stacks.
**we need to implement queue using two stacks.**

## Whiteboard Process
**enqueue :**
![algo (14)](https://github.com/11mones/data-structures-and-algorithms/assets/72322641/bc6dbde1-b0bb-4627-a6bc-102baaa2d119)
**dequeue :**
![algo (15)](https://github.com/11mones/data-structures-and-algorithms/assets/72322641/dba04711-21a8-4aab-bd1d-b6753f112b7a)

## Approach & Efficiency
it is implemented in the right way and do all the functionalities required (enqueue and dequeue)

## Solution
We will initialize two stacks in pseudo queue class and in enqueue method we will just use stack push to enqueue the value in stack1 cause it is the same of the 
enqueue,




In the dequeue method we will first push all values in stack1 to stack2 and then we will pop from stack2 and return the pop value, this will be similar to dequeue.
