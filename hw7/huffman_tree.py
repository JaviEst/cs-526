import heapq

from dataclasses import dataclass
from typing import Optional


@dataclass
class HuffmanNode:
    frequency: int
    char: Optional[str] = None
    left: Optional[HuffmanNode] = None
    right: Optional[HuffmanNode] = None

    def is_leaf(self) -> bool:
        return self.char is not None

    def __lt__(self, other: HuffmanNode) -> bool:
        return self.frequency < other.frequency

    def __repr__(self) -> str:
        if self.is_leaf():
            return f"Node({repr(self.char)}: {self.frequency})"
        return f"Node(freq={self.frequency})"


def build_frequency_map(text: str) -> dict[str, int]:
    freq_map: dict[str, int] = {}
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1
    return freq_map


def build_huffman_tree(freq_map: dict[str, int]) -> Optional[HuffmanNode]:
    if not freq_map:
        return None
    
    heap = [HuffmanNode(frequency=freq, char=char) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        parent = HuffmanNode(
            frequency=left.frequency + right.frequency,
            left=left,
            right=right
        )
        heapq.heappush(heap, parent)

    return heap[0] if heap else None


def build_encoding_table(root: Optional[HuffmanNode]) -> dict[Optional[str], str]:
    if root is None:
        return {}
    
    encoding: dict[Optional[str], str] = {}
    
    def traverse(node: HuffmanNode, code: str) -> None:
        if node.is_leaf():
            # Special case: single character tree
            encoding[node.char] = code if code else "0"
        else:
            if node.left:
                traverse(node.left, code + "0")
            if node.right:
                traverse(node.right, code + "1")
    
    traverse(root, "")
    return encoding


def print_tree(root: Optional[HuffmanNode], prefix: str = "", is_left: bool = True) -> None:
    if root is None:
        return
    
    connector = "├── " if is_left else "└── "
    if prefix == "":
        connector = ""
    
    if root.is_leaf():
        char_repr = repr(root.char) if root.char != ' ' else "'<space>'"
        print(f"{prefix}{connector}{char_repr}: {root.frequency}")
    else:
        print(f"{prefix}{connector}[{root.frequency}]")
    
    if not root.is_leaf():
        extension = "│   " if is_left else "    "
        new_prefix = prefix + extension if prefix else ""
        
        if root.left:
            print_tree(root.left, new_prefix, True)
        if root.right:
            print_tree(root.right, new_prefix, False)
