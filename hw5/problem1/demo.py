import random
from bst import BinarySearchTree


def print_separator(title: str = "") -> None:
    """Print a visual separator with optional title."""
    if title:
        print("\n" + "█" * 80)
        print(f"  {title}")
        print("█" * 80)
    else:
        print("\n" + "─" * 80)


def main():
    print("=" * 80)
    print(" " * 20 + "BINARY SEARCH TREE DEMONSTRATION")
    print("=" * 80)
    
    random.seed()
    set_size = random.randint(5, 50)
    input_set = [random.randint(1, 1000) for _ in range(set_size)]
    
    print(f"\n📊 Generated Input Set (Size: {set_size}):")
    print(f"   {input_set}")
    
    print_separator("BUILDING INITIAL TREE")
    bst = BinarySearchTree()
    
    print(f"\nAdding {len(input_set)} values to the tree...")
    for value in input_set:
        bst.add_node(value)
    
    print(f"\n✓ Initial tree created with {bst.size()} nodes")
    bst.print_tree()
    
    existing_values: list[int] = []
    print_separator("DEMONSTRATING ADD OPERATIONS")
    for _ in range(3):
        new_value = random.randint(1, 1000)
        print(f"\n➤ Adding node with value: {new_value}")
        bst.add_node(new_value)
        print(f"   Tree now has {bst.size()} nodes")
        bst.print_tree()
        existing_values.append(new_value)
    
    print_separator("DEMONSTRATING DELETE OPERATIONS")
    all_values = input_set.copy()
    for _ in range(min(3, len(all_values))):
        if all_values:
            value_to_delete = random.choice(all_values)
            all_values.remove(value_to_delete)
            
            print(f"\n➤ Deleting node with value: {value_to_delete}")
            deleted = bst.delete_node(value_to_delete)
            if deleted:
                print(f"   ✓ Successfully deleted. Tree now has {bst.size()} nodes")
            else:
                print(f"   ✗ Value not found in tree")
            bst.print_tree()
    
    print_separator("DEMONSTRATING FIND OPERATIONS")
    print("POSITIVE CASES (searching for existing values):")
    print("-" * 60)    
    for value in existing_values:
        found = bst.find_node(value)
        status = "✓ FOUND" if found else "✗ NOT FOUND"
        print(f"   Searching for {value:4d}: {status}")
    
    print("\nNEGATIVE CASES (searching for non-existing values):")
    print("-" * 60)
    for _ in range(3):
        search_value = random.randint(1, 1000)
        
        attempts = 0
        while bst.find_node(search_value) and attempts < 10:
            search_value = random.randint(1, 1000)
            attempts += 1
        
        found = bst.find_node(search_value)
        status = "✓ FOUND" if found else "✗ NOT FOUND"
        print(f"   Searching for {search_value:4d}: {status}")


if __name__ == "__main__":
    main()
