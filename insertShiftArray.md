# Insert shift array 

The challenge is we have to write a function that take an array and number and return an array with that number in the middle of it.

## Whiteboard Process
![Alt text](Untitled%20(1).jpg)

## Approach & Efficiency
We loop through the array, and if the index we standing on is equal to len(array)/2, we will insert our number in the array., it is O(n) complexity

## Solution
Here is the code, and you have just to pass the array and the number to the function.





    def insertShiftArray (arr , input):
    
        length = int(len(arr))
        print(length)
        if length % 2 == 0:
            arr.insert(length//2, input)
        else : 
        arr.insert(length//2 + 1, input)
        return arr


