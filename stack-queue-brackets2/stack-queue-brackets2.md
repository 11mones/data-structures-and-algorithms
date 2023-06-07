# Validate brackets
Writing a boolean function called validate brackets that takes a string input and checks if the brackets that are in the string is balanced or not .
## Whiteboard Process
![algo (19)](https://github.com/11mones/data-structures-and-algorithms/assets/72322641/283c28cf-4a82-4715-9891-d8065c834c8f)


## Approach & Efficiency
The code is working well at all the cases and there is 8 tests you can run it by : 
        implementation_test.py

## Solution
algorithm : Creating an empty stack, and iterate through each character in the string, and if the character is an opening bracket, push it onto the stack,
and If the character is a closing bracket we will check if the stack is empty or the top element does not match the current closing bracket, return False and pop
the top element from the stack and after iterating through all characters, return True if the stack is empty (all brackets are balanced), False otherwise.




The code itself is pushed and i put it in whiteboard too 




It is in link lest directory in implementation.py in line 394






And there is tests too check them
