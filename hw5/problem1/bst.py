from typing import Optional
from node import Node


class BinarySearchTree:
    """
    Binary Search Tree Abstract Data Type.
    
    A BST maintains the invariant: for any node,
    all values in the left subtree < node value < all values in right subtree
    
    Attributes:
        root: The root node of the tree (or None if tree is empty)
    """
    
    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root: Optional[Node] = None
    
    def add_node(self, value: int) -> None:
        """
        Add a new node with the given value to the BST.
        
        Algorithm: Recursively traverse the tree following BST property:
        - If value < current node, go left
        - If value > current node, go right
        - If value equals current node, do nothing (no duplicates)
        
        Time Complexity: O(h) where h is the height of the tree
        
        Args:
            value: The integer value to add to the tree
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)
    
    def _add_recursive(self, node: Node, value: int) -> None:
        """
        Recursive helper method to add a value to the tree.
        
        Args:
            node: Current node in the traversal
            value: Value to add
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)
        # If value == node.value, don't add duplicates
    
    def delete_node(self, value: int) -> bool:
        """
        Delete a node with the given value from the BST.
        
        Algorithm: Three cases to handle:
        1. Node has no children (leaf): Simply remove it
        2. Node has one child: Replace node with its child
        3. Node has two children: Replace with in-order successor (smallest in right subtree)
        
        Time Complexity: O(h) where h is the height of the tree
        
        Args:
            value: The value to delete from the tree
            
        Returns:
            True if the value was found and deleted, False otherwise
        """
        self.root, deleted = self._delete_recursive(self.root, value)
        return deleted
    
    def _delete_recursive(self, node: Optional[Node], value: int) -> tuple[Optional[Node], bool]:
        """
        Recursive helper method to delete a value from the tree.
        
        Args:
            node: Current node in the traversal
            value: Value to delete
            
        Returns:
            Tuple of (updated node reference, whether deletion occurred)
        """
        if node is None:
            return None, False
        
        deleted = False
        
        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
        else:
            deleted = True
            
            # Case 1: Node has no children (leaf node)
            if node.left is None and node.right is None:
                return None, True
            
            # Case 2a: Node has only right child
            elif node.left is None:
                return node.right, True
            
            # Case 2b: Node has only left child
            elif node.right is None:
                return node.left, True
            
            # Case 3: Node has two children
            else:
                # Find the in-order successor (smallest value in right subtree)
                successor = self._find_min(node.right)
                # Replace current node's value with successor's value
                node.value = successor.value
                # Delete the successor from the right subtree
                node.right, _ = self._delete_recursive(node.right, successor.value)
        
        return node, deleted
    
    def _find_min(self, node: Node) -> Node:
        """
        Find the node with minimum value in the subtree rooted at node.
        
        Args:
            node: Root of the subtree
            
        Returns:
            Node with the minimum value
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def find_node(self, value: int) -> bool:
        """
        Search for a node with the given value in the BST.
        
        Algorithm: Follow BST property to traverse:
        - If value < current node, search left
        - If value > current node, search right
        - If value == current node, found it
        
        Time Complexity: O(h) where h is the height
        
        Args:
            value: The value to search for
            
        Returns:
            True if the value exists in the tree, False otherwise
        """
        return self._find_recursive(self.root, value)
    
    def _find_recursive(self, node: Optional[Node], value: int) -> bool:
        """
        Recursive helper method to search for a value.
        
        Args:
            node: Current node in the traversal
            value: Value to search for
            
        Returns:
            True if value found, False otherwise
        """
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._find_recursive(node.left, value)
        else:
            return self._find_recursive(node.right, value)
    
    def print_tree(self) -> None:
        """
        Print the tree structure in a visual format.
        
        Uses in-order, pre-order, and post-order traversals, plus a visual tree structure.
        """
        if self.root is None:
            print("Tree is empty")
            return
        
        print("\n" + "="*60)
        print("TREE STRUCTURE:")
        print("="*60)
        self._print_tree_structure(self.root, "", True)
        
        print("\n" + "="*60)
        print("TRAVERSALS:")
        print("="*60)
        
        print("In-order (Left-Root-Right):  ", end="")
        self._print_inorder(self.root)
        print()
        
        print("Pre-order (Root-Left-Right): ", end="")
        self._print_preorder(self.root)
        print()
        
        print("Post-order (Left-Right-Root):", end="")
        self._print_postorder(self.root)
        print()
        print("="*60)
    
    def _print_tree_structure(self, node: Optional[Node], prefix: str, is_tail: bool) -> None:
        """
        Print tree in a visual hierarchical structure.
        
        Args:
            node: Current node to print
            prefix: String prefix for indentation
            is_tail: Whether this node is the last child
        """
        if node is None:
            return
        
        print(prefix + ("└── " if is_tail else "├── ") + str(node.value))
        
        children: list[tuple[str, Node]] = []
        if node.left is not None:
            children.append(('L', node.left))
        if node.right is not None:
            children.append(('R', node.right))
        
        for i, (_, child) in enumerate(children):
            is_last = (i == len(children) - 1)
            extension = "    " if is_tail else "│   "
            self._print_tree_structure(child, prefix + extension, is_last)
    
    def _print_inorder(self, node: Optional[Node]) -> None:
        """In-order traversal: Left -> Root -> Right"""
        if node is not None:
            self._print_inorder(node.left)
            print(node.value, end=" ")
            self._print_inorder(node.right)
    
    def _print_preorder(self, node: Optional[Node]) -> None:
        """Pre-order traversal: Root -> Left -> Right"""
        if node is not None:
            print(node.value, end=" ")
            self._print_preorder(node.left)
            self._print_preorder(node.right)
    
    def _print_postorder(self, node: Optional[Node]) -> None:
        """Post-order traversal: Left -> Right -> Root"""
        if node is not None:
            self._print_postorder(node.left)
            self._print_postorder(node.right)
            print(node.value, end=" ")
    
    def is_empty(self) -> bool:
        """Check if the tree is empty."""
        return self.root is None
    
    def size(self) -> int:
        """Return the number of nodes in the tree."""
        return self._size_recursive(self.root)
    
    def _size_recursive(self, node: Optional[Node]) -> int:
        """Recursive helper to count nodes."""
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)
