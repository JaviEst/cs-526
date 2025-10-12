class ArrayStack:
    """Stack implemented as an array"""
    def __init__(self):
        self.items: list[int] = []
    
    def push(self, item: int) -> None:
        self.items.append(item)
    
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def size(self) -> int:
        return len(self.items)
    
    def to_list(self) -> list[int]:
        return self.items.copy()


def reverse_array_stack_recursive(stack: ArrayStack) -> ArrayStack:
    """
    Recursively reverse a stack implemented as an array.
    
    Args:
        stack: ArrayStack to reverse
        
    Returns:
        New reversed ArrayStack
    """
    def reverse_helper(original: ArrayStack, reversed_stack: ArrayStack) -> ArrayStack:
        # Base case: if original stack is empty, return the reversed stack
        if original.is_empty():
            return reversed_stack
        
        # Recursive case: move top element from original to reversed
        item = original.pop()
        reversed_stack.push(item)
        return reverse_helper(original, reversed_stack)
    
    # Create a copy to avoid modifying the original
    stack_copy = ArrayStack()
    for item in stack.to_list():
        stack_copy.push(item)
    
    reversed_stack = ArrayStack()
    return reverse_helper(stack_copy, reversed_stack)