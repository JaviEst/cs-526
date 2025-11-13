from typing import Optional


class Node:
    """
    Node Abstract Data Type for Binary Search Tree.
    
    Attributes:
        value: The integer value stored in this node
        left: Reference to the left child node (or None)
        right: Reference to the right child node (or None)
    """
    
    def __init__(self, value: int):
        """
        Initialize a new node with the given value.
        
        Args:
            value: The integer value to store in this node
        """
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __str__(self) -> str:
        """String representation of the node."""
        return str(self.value)
    
    def __repr__(self) -> str:
        """Detailed string representation for debugging."""
        return f"Node({self.value})"
