import sys
from pathlib import Path
from shopping_cart import shopping_cart


def parse_input(file_path: str) -> list[str]:
    """
    Parse the input file and return the list of aisle categories.
    
    Args:
        file_path: Path to the input file
        
    Returns:
        List of strings representing aisle categories
    """
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    
    # First line contains the number of aisles
    n = int(lines[0])
    
    # Second line contains the comma-separated categories
    categories = lines[1].split(',')
    
    # Remove any whitespace from category names
    categories = [category.strip() for category in categories]
    
    # Validate that we have the correct number of categories
    if len(categories) != n:
        raise ValueError(f"Expected {n} categories, but got {len(categories)}")
    
    return categories


def main():
    """
    Main function to handle command line arguments and process the shopping cart problem.
    """
    if len(sys.argv) != 2:
        print("Usage: python handle_inputs.py <input_file_path>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Check if file exists
    if not Path(input_file).exists():
        print(f"Error: File '{input_file}' does not exist.")
        sys.exit(1)
    
    try:
        # Parse the input file
        aisle_categories = parse_input(input_file)
        
        # Run the shopping cart algorithm
        result = shopping_cart(aisle_categories)

        print(f"Input: {aisle_categories} -> {result}")
        
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()