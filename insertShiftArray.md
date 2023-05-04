# Insert shift array 

The challenge is we have to write a function that take an array and number and return an array with that number in the middle of it.

## Whiteboard Process
![Alt text](Untitled%20(1).jpg)

## Approach & Efficiency
We loop through the array, and if the index we standing on is equal to len(array)/2, we will insert our number in the array., it is O(n) complexity

## Solution
Here is the code, and you have just to pass the array and the number to the function.



def insertShiftArray (arr , input):





    temp = int(len(arr)/2)




    for x in arr :





        if x == temp :






            arr.insert(x, input)




            
            
    return arr


