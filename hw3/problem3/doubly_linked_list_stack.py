from typing import Optional


class DoublyListNode:
    """Node for doubly linked list"""
    def __init__(self, val: int = 0, next: Optional['DoublyListNode'] = None, prev: Optional['DoublyListNode'] = None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedListStack:
    """Stack implemented as a doubly linked list"""
    def __init__(self):
        self.head: Optional[DoublyListNode] = None
        self.tail: Optional[DoublyListNode] = None
        self._size = 0
    
    def push(self, item: int) -> None:
        new_node = DoublyListNode(item)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            if self.tail is not None:
                self.tail.next = new_node
            self.tail = new_node
        self._size += 1
    
    def pop(self) -> int:
        if self.is_empty() or self.tail is None:
            raise IndexError("Stack is empty")

        val = self.tail.val
        if self._size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
        self._size -= 1
        return val
    
    def peek(self) -> int:
        if self.is_empty() or self.tail is None:
            raise IndexError("Stack is empty")
        return self.tail.val
    
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


def reverse_doubly_linked_list_stack_recursive(stack: DoublyLinkedListStack) -> DoublyLinkedListStack:
    """
    Recursively reverse a stack implemented as a doubly linked list.
    
    Args:
        stack: DoublyLinkedListStack to reverse
        
    Returns:
        New reversed DoublyLinkedListStack
    """
    def reverse_helper(original: DoublyLinkedListStack, reversed_stack: DoublyLinkedListStack) -> DoublyLinkedListStack:
        # Base case: if original stack is empty, return the reversed stack
        if original.is_empty():
            return reversed_stack
        
        # Recursive case: move top element from original to reversed
        item = original.pop()
        reversed_stack.push(item)
        return reverse_helper(original, reversed_stack)
    
    # Create a copy to avoid modifying the original
    stack_copy = DoublyLinkedListStack()
    for item in stack.to_list():
        stack_copy.push(item)
    
    reversed_stack = DoublyLinkedListStack()
    return reverse_helper(stack_copy, reversed_stack)