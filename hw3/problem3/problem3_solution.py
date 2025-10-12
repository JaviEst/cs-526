from array_stack import ArrayStack, reverse_array_stack_recursive
from linked_list_stack import LinkedListStack, reverse_linked_list_stack_recursive
from doubly_linked_list_stack import DoublyLinkedListStack, reverse_doubly_linked_list_stack_recursive


def demonstrate_stack_reversal(numbers: list[int]) -> None:
    """
    Demonstrate stack reversal for all three implementations.
    
    Args:
        numbers: List of numbers to add to stacks
    """
    print(f"Input: {', '.join(map(str, numbers))}")
    
    # Array Stack
    print("\n=== Array Stack ===")
    array_stack = ArrayStack()
    for num in numbers:
        array_stack.push(num)
    
    print(f"Original stack (top to bottom): {', '.join(map(str, reversed(array_stack.to_list())))}")
    reversed_array_stack = reverse_array_stack_recursive(array_stack)
    print(f"Reversed stack (top to bottom): {', '.join(map(str, reversed(reversed_array_stack.to_list())))}")
    
    # Linked List Stack
    print("\n=== Linked List Stack ===")
    linked_stack = LinkedListStack()
    for num in numbers:
        linked_stack.push(num)
    
    print(f"Original stack (top to bottom): {', '.join(map(str, linked_stack.to_list()))}")
    reversed_linked_stack = reverse_linked_list_stack_recursive(linked_stack)
    print(f"Reversed stack (top to bottom): {', '.join(map(str, reversed_linked_stack.to_list()))}")
    
    # Doubly Linked List Stack
    print("\n=== Doubly Linked List Stack ===")
    doubly_stack = DoublyLinkedListStack()
    for num in numbers:
        doubly_stack.push(num)
    
    print(f"Original stack (top to bottom): {', '.join(map(str, reversed(doubly_stack.to_list())))}")
    reversed_doubly_stack = reverse_doubly_linked_list_stack_recursive(doubly_stack)
    print(f"Reversed stack (top to bottom): {', '.join(map(str, reversed(reversed_doubly_stack.to_list())))}")


def process_stack_file(input_file: str, output_file: str = "") -> None:
    """
    Process an input file and demonstrate stack reversal for each line.
    
    Args:
        input_file: Path to the input file
        output_file: Optional path to output file (if empty, prints to stdout)
    """
    results: list[str] = []
    
    try:
        with open(input_file, 'r') as f:
            for line in f:
                line = line.strip()
                
                if not line:
                    continue
                
                try:
                    numbers = [int(x.strip()) for x in line.split(',')]
                    
                    print(f"\n\nProcessing: {', '.join(map(str, numbers))}")
                    results.append(f"Input: {', '.join(map(str, numbers))}")
                    
                    demonstrate_stack_reversal(numbers)
                    
                    results.append(f"Output: {', '.join(map(str, reversed(numbers)))}")
                    results.append("")
                    
                except ValueError:
                    print(f"Error: Could not parse numbers from line: {line}")
                    results.append(f"Error: Could not parse numbers from line: {line}")
        
        if output_file:
            with open(output_file, 'w') as f:
                for result in results:
                    f.write(result + '\n')
                
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")


def main():
    """
    Main function to run the stack reversal demonstrations.
    Can be used with command line arguments or interactively.
    """
    import sys
    
    if len(sys.argv) > 1:
        # Command line usage
        if sys.argv[1] == "-n" or sys.argv[1] == "--numbers":
            # Direct number input
            if len(sys.argv) > 2:
                try:
                    numbers = [int(x.strip()) for x in sys.argv[2].split(',')]
                    demonstrate_stack_reversal(numbers)
                except ValueError:
                    print("Error: Please provide comma-separated numbers")
            else:
                print("Error: Please provide comma-separated numbers after -n or --numbers flag")
        else:
            # File input
            input_file = sys.argv[1]
            output_file = sys.argv[2] if len(sys.argv) > 2 else ""
            process_stack_file(input_file, output_file)
    else:
        # Interactive usage
        choice = input("Process (f)ile or (n)umbers? ").lower()
        
        if choice == 'n' or choice == 'numbers':
            input_numbers = input("Enter comma-separated numbers: ")
            try:
                numbers = [int(x.strip()) for x in input_numbers.split(',')]
                demonstrate_stack_reversal(numbers)
            except ValueError:
                print("Error: Please provide valid comma-separated numbers")
        else:
            input_file = input("Enter the input file path: ")
            output_choice = input("Output to file? (y/n): ").lower()
            output_file = ""
            if output_choice == 'y':
                output_file = input("Enter the output file path: ")
            
            process_stack_file(input_file, output_file)


if __name__ == "__main__":
    main()
