# data-structures-and-algorithms

The challenge is we have to write a function that take an array and return it in reverse order.

## Whiteboard Process

## Approach & Efficiency
looping through the array n/2 times, and each time i am switching two elements of the array to be reversed finally when the iteration is done, it is O(n) complexity

## Solution
Here is the code, and you have just to pass the array to the function.

def reverse(arr):
	temp = 0
	for x/2 in arr:
		temp = arr[x]
		arr[x] = arr[len(arr)]
		arr[len(arr)-x-1] = temp;

	return arr