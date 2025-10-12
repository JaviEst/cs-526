def find_unique_substrings_recursive(
        s: str,
        start: int = 0,
        end: int | None = None,
        substrings: set[str] | None = None
    ) -> set[str]:
    """
    Recursively find all unique substrings of a given string.
    
    Args:
        s: The input string
        start: Starting index for substring generation
        end: Ending index for substring generation (None means len(s))
        substrings: Set to store unique substrings (None creates new set)
    
    Returns:
        Set of all unique substrings
    """
    if substrings is None:
        substrings = set()
    
    if end is None:
        end = len(s)
    
    # Base case: if start >= end, no more substrings can be generated
    if start >= end:
        return substrings
    
    # Generate all substrings starting at 'start' position
    for i in range(start + 1, end + 1):
        substring = s[start:i]
        if substring:  # Only add non-empty substrings
            substrings.add(substring)
    
    # Recursive call: move to next starting position
    return find_unique_substrings_recursive(s, start + 1, end, substrings)


def print_and_count_substrings(s: str) -> int:
    """
    Print all unique substrings and return the count.
    
    Args:
        s: Input string
        
    Returns:
        Number of unique substrings
    """
    cleaned_string = s.strip()
    
    unique_substrings = find_unique_substrings_recursive(cleaned_string)
    if unique_substrings:
        print(", ".join(sorted(unique_substrings)), "->", len(unique_substrings))

    return len(unique_substrings)


def process_substring_file(input_file: str, output_file: str = ""):
    """
    Process an input file and find unique substrings for each line.
    
    Args:
        input_file: Path to the input file
        output_file: Optional path to output file (if empty, prints to stdout)
    """
    results: list[str] = []
    
    try:
        with open(input_file, 'r') as f:
            for line in f:
                string = line.strip()
                
                if not string:
                    continue
                
                print(f"Input: {string}")

                unique_substrings = find_unique_substrings_recursive(string)

                substring_list = sorted(list(unique_substrings))
                output_line = ", ".join(substring_list) + f" -> {len(substring_list)}"

                print("Output:", output_line)

                results.append(f"Input: {string}")
                results.append("Output: " + output_line)
                results.append("")
    
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
    Main function to run the substring finder.
    Can be used with command line arguments or interactively.
    """
    import sys
    
    if len(sys.argv) > 1:
        # Command line usage
        if sys.argv[1] == "-s" or sys.argv[1] == "--string":
            # Direct string input
            if len(sys.argv) > 2:
                input_string = sys.argv[2]
                print(f"Input: {input_string}")
                print("Output:", end=" ")
                print_and_count_substrings(input_string)
            else:
                print("Error: Please provide a string after -s or --string flag")
        else:
            # File input
            input_file = sys.argv[1]
            output_file = sys.argv[2] if len(sys.argv) > 2 else ""
            process_substring_file(input_file, output_file)
    else:
        # Interactive usage
        choice = input("Process (f)ile or (s)tring? ").lower()
        
        if choice == 's' or choice == 'string':
            input_string = input("Enter a string: ")
            print(f"Input: {input_string}")
            print("Output:", end=" ")
            print_and_count_substrings(input_string)
        else:
            input_file = input("Enter the input file path: ")
            output_choice = input("Output to file? (y/n): ").lower()
            output_file = ""
            if output_choice == 'y':
                output_file = input("Enter the output file path: ")
            
            process_substring_file(input_file, output_file)


if __name__ == "__main__":
    main()
