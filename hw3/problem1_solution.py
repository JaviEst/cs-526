def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.
    Ignores spaces and is case-insensitive.
    """

    cleaned = s.replace(' ', '').lower()
    
    # Check if the string reads the same forwards and backwards
    return cleaned == cleaned[::-1]


def process_palindromes(input_file: str, output_file: str = ""):
    """
    Process an input file and determine palindromes.
    
    Args:
        input_file: Path to the input file
        output_file: Optional path to output file (if empty, prints to stdout)
    """
    palindrome_count = 0
    results: list[str] = []
    
    try:
        with open(input_file, 'r') as f:
            for line in f:
                string = line.strip()
                
                # Skip empty lines
                if not string:
                    continue
                
                is_pal = is_palindrome(string)
                results.append(str(is_pal))
                
                if is_pal:
                    palindrome_count += 1
        
        results.append(str(palindrome_count))
        
        if output_file:
            with open(output_file, 'w') as f:
                for result in results:
                    f.write(result + '\n')
        else:
            for result in results:
                print(result)
                
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")


def main():
    """
    Main function to run the palindrome checker.
    Can be used with command line arguments or interactively.
    """
    import sys
    
    if len(sys.argv) > 1:
        # Command line usage
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else ""
        process_palindromes(input_file, output_file)
    else:
        # Interactive usage
        input_file = input("Enter the input file path: ")
        output_choice = input("Output to file? (y/n): ").lower()
        output_file = ""
        if output_choice == 'y':
            output_file = input("Enter the output file path: ")

        process_palindromes(input_file, output_file)


if __name__ == "__main__":
    main()
