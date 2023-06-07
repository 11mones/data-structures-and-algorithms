class Stack:
    def __init__(self,top=None):
        self.top = top

    def push(self,value):
        """
    Pushes a value onto the top of the stack.
    Argument : The value to be pushed onto the stack.

        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
    Removes and returns the value from the top of the stack.
    Returns The value that was removed from the top of the stack.
    Raises Exception: If the stack is empty and there is nothing to pop.

        """
        #check if the statck is empty :
        if self.top == None: 
            raise Exception("The stack is empty you can not pop from it")
        else :
            temp= self.top
            self.top = temp.next
            temp.next = None
            return temp.data

    def peek(self):
        """
    Returns the value from the top of the stack without removing it.
    Returns The value at the top of the stack.
    Raises Exception: If the stack is empty and there is nothing to peek.

        """
        if self.top == None: 
            raise Exception("The stack is empty you can not peek from it")
        else : 
            return self.top.data
        
    def is_empty(self):
        if self.top == None: 
            return  "stack is empty"



    def validate_brackets(string):
        
        """
        Check if the brackets in the given string are balanced.

        Arguments:
        - string: A string containing brackets to be validated.

        Returns:
        - A boolean value indicating whether the brackets are balanced (True) or not (False).

        Description:
        This function checks if the brackets in the given string are balanced, meaning that each opening bracket has a corresponding closing bracket in the correct order. The function supports three types of brackets: round brackets '()', square brackets '[]', and curly brackets '{}'.

        Examples:
        - validate_brackets('{}')  # Returns True
        - validate_brackets('[({}]')  # Returns False

        """
        stack = Stack()
        
        for char in string:
            if char in ["(", "{", "["]:
                stack.push(Node(char))  
            elif char in [")", "}", "]"]:
                if stack.is_empty():
                    return False  
                top = stack.pop().data 
                if (char == ")" and top != "(") or (char == "}" and top != "{") or (char == "]" and top != "["):
                    return False  
            else:
                continue  
        if stack.is_empty() :

            return True
        else : 
            return False 