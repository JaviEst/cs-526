def smallest_elements_exceeding_target(arr: list[int], target: int) -> int:
    """
    Find the smallest number of elements from array whose sum exceeds the target.
    
    Strategy: Greedy approach - sort array in descending order and pick largest
    elements first until the sum exceeds the target.
    
    Args:
        arr: List of integers
        target: Target value to exceed
        
    Returns:
        Minimum number of elements needed
    """
    # Sort array in descending order to pick largest elements first
    sorted_arr = sorted(arr, reverse=True)
    
    current_sum = 0
    count = 0
    
    # Keep adding elements until sum exceeds target
    for num in sorted_arr:
        current_sum += num
        count += 1
        
        # Check if we've exceeded the target
        if current_sum > target:
            return count
    
    # If we've used all elements and still haven't exceeded target
    # (though problem states sum of all elements > T, so this shouldn't happen)
    return count


def solve_from_input(input_data: list[str]) -> tuple[list[int], int, int]:
    """
    Parse input data and solve the problem.
    
    Args:
        input_data: List of strings containing input
        
    Returns:
        Tuple of (array, target, answer)
    """
    if len(input_data) < 3:
        raise ValueError("Insufficient input data")
    
    n = int(input_data[0].strip())
    target = int(input_data[1].strip())
    arr = [int(x) for x in input_data[2].strip().split()]
    
    if len(arr) != n:
        raise ValueError(f"Expected {n} elements, got {len(arr)}")
    
    answer = smallest_elements_exceeding_target(arr, target)
    
    return arr, target, answer


def process_file(input_file: str, output_file: str = "") -> None:
    """
    Process an input file and solve the smallest number problem.
    
    Args:
        input_file: Path to the input file
        output_file: Optional path to output file (if empty, prints to stdout)
    """
    results: list[str] = []
    
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        arr, target, answer = solve_from_input(lines)
        
        # Format output as specified
        arr_str = ','.join(map(str, arr))
        result = f"Input: {arr_str} Target: {target} Answer: {answer}"
        
        print(result)
        results.append(result)
        
        # Output to file if specified
        if output_file:
            with open(output_file, 'w') as f:
                for result_line in results:
                    f.write(result_line + '\n')
                
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")


def process_stdin() -> None:
    """
    Process input from stdin.
    """
    import sys
    
    try:
        lines = sys.stdin.readlines()
        arr, target, answer = solve_from_input(lines)
        
        # Format output as specified
        arr_str = ','.join(map(str, arr))
        result = f"Input: {arr_str} Target: {target} Answer: {answer}"
        
        print(result)
        
    except Exception as e:
        print(f"Error processing input: {e}")


def main():
    """
    Main function to run the smallest number solver.
    Can be used with command line arguments or interactively.
    """
    import sys
    
    if len(sys.argv) > 1:
        # Command line usage
        if sys.argv[1] == "-s" or sys.argv[1] == "--stdin":
            # Stdin input
            process_stdin()
        else:
            # File input
            input_file = sys.argv[1]
            output_file = sys.argv[2] if len(sys.argv) > 2 else ""
            process_file(input_file, output_file)
    else:
        # Interactive usage
        choice = input("Process (f)ile or (i)nput directly? ").lower()
        
        if choice == 'i' or choice == 'input':
            print("Enter number of elements:")
            n = int(input().strip())
            
            print("Enter target value:")
            target = int(input().strip())
            
            print("Enter space-separated array elements:")
            arr = [int(x) for x in input().strip().split()]
            
            if len(arr) != n:
                print(f"Error: Expected {n} elements, got {len(arr)}")
                return
            
            answer = smallest_elements_exceeding_target(arr, target)
            
            # Format output as specified
            arr_str = ','.join(map(str, arr))
            result = f"Input: {arr_str} Target: {target} Answer: {answer}"
            
            print(result)
        else:
            input_file = input("Enter the input file path: ")
            output_choice = input("Output to file? (y/n): ").lower()
            output_file = ""
            if output_choice == 'y':
                output_file = input("Enter the output file path: ")
            
            process_file(input_file, output_file)


if __name__ == "__main__":
    main()