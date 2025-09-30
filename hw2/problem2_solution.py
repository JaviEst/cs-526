class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def doIt(node):
    if node is None:
        return

    doIt(node.next)
    print(node.value)

def create_linked_list():
    node1 = Node(12)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(2)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    return node1

if __name__ == "__main__":
    head = create_linked_list()
    
    print("Linked list structure: 12 -> 3 -> 5 -> 2\n")

    print("Output of doIt function:")
    doIt(head)
