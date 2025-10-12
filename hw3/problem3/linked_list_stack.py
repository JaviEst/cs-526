from typing import Optional


class ListNode:
    """Node for singly linked list"""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class LinkedListStack:
    """Stack implemented as a linked list"""
    def __init__(self):
        self.head: Optional[ListNode] = None
        self._size = 0
    
    def push(self, item: int) -> None:
        new_node = ListNode(item)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def pop(self) -> int:
        if self.is_empty() or self.head is None:
            raise IndexError("Stack is empty")

        val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return val
    
    def peek(self) -> int:
        if self.is_empty() or self.head is None:
            raise IndexError("Stack is empty")
        return self.head.val
    
    def is_empty(self) -> bool:
        return self.head is None
    
    def size(self) -> int:
        return self._size
    
    def to_list(self) -> list[int]:
        result: list[int] = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result


def reverse_linked_list_stack_recursive(stack: LinkedListStack) -> LinkedListStack:
    """
    Recursively reverse a stack implemented as a linked list.
    
    Args:
        stack: LinkedListStack to reverse
        
    Returns:
        New reversed LinkedListStack
    """
    def reverse_helper(original: LinkedListStack, reversed_stack: LinkedListStack) -> LinkedListStack:
        # Base case: if original stack is empty, return the reversed stack
        if original.is_empty():
            return reversed_stack
        
        # Recursive case: move top element from original to reversed
        item = original.pop()
        reversed_stack.push(item)
        return reverse_helper(original, reversed_stack)
    
    # Create a copy to avoid modifying the original
    stack_copy = LinkedListStack()
    items = stack.to_list()
    for item in reversed(items):  # Reverse to maintain original order in copy
        stack_copy.push(item)
    
    reversed_stack = LinkedListStack()
    return reverse_helper(stack_copy, reversed_stack)