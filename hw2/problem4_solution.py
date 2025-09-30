class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def sum_of_three_middle_nodes(head):
    """
    Find the sum of the three middle nodes in a doubly linked list of sorted integers.
    Assumes the doubly linked list has an odd length and is sorted.
    
    Args:
        head: The head node of the doubly linked list
        
    Returns:
        int: The sum of the three middle nodes
    """
    if not head:
        return 0
    
    # Find the length of the list
    current = head
    length = 0
    while current:
        length += 1
        current = current.next
    
    # Find the middle index
    middle_index = length // 2
    
    # Navigate to the middle node
    current = head
    for i in range(middle_index):
        current = current.next
    
    # Calculate the sum of the three middled nodes
    middle_sum = 0
    if current.prev:
        middle_sum += current.prev.value
    
    middle_sum += current.value
    
    if current.next:
        middle_sum += current.next.value
    
    return middle_sum

def create_doubly_linked_list(values):
    """
    Create a doubly linked list from a list of values.
    
    Args:
        values: List of values to create nodes from
        
    Returns:
        The head of the created doubly linked list
    """
    if not values:
        return None
    
    # Create the head node
    head = DoublyLinkedListNode(values[0])
    current = head
    
    # Create and link the remaining nodes
    for i in range(1, len(values)):
        new_node = DoublyLinkedListNode(values[i])
        current.next = new_node
        new_node.prev = current
        current = new_node
    
    return head

if __name__ == "__main__":
    test_values = [2, 4, 8, 10, 15, 29, 41]
    
    print("Creating doubly linked list with values:", test_values)
    head = create_doubly_linked_list(test_values)
    
    result = sum_of_three_middle_nodes(head)
    print("The sum of the three linked list middle nodes is: ", result)
