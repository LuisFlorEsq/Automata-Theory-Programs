
# File to define a simple stack structure


class Stack():
    
    
    def __init__(self):
        """
        Initialize the empty stack, for this purpose a stack will be empty when it has reached the 'Z0' which is the start symbol.
        """
        
        self.items = ['Z0'] 
        
    def is_empty(self):
        """
        Return a Boolean value to see if the stack is empty.
        Check if the only symbol in the stack is the start symbol 'Z0'
        """
        
        return True if self.peek() == 'Z0' else False
        
    
    def push(self, item):
        """
        Push the item in the stack.
        """
        
        self.items.append(item)
        
    def pop(self):
        """
        Pop the first element in the stack.
        """
        
        popped_element = self.items[-1]
        self.items = self.items[:-1]
        
        return popped_element
        
    def peek(self):
        """
        Find the element in the stack's peek.
        """
        
        return self.items[-1]
    
    def size(self):
        """
        Calculate the size of the stack, it won't count the start symbol.
        """
        
        if(self.is_empty()):
            
            return 0
        
        else:
            
            stack_size = len(self.items)
            
            return stack_size - 1