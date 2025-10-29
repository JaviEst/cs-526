import sys
from pathlib import Path
from snowfall import calculate_snowfall


def parse_input(file_path: str) -> list[int]:
    """
    Parse the input file and return the snowfall data.
    
    Args:
        file_path: Path to the input file
        
    Returns:
        List of integers representing cumulative snowfall data
    """
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
        
    # First line contains the number of days
    n = int(lines[0])
    
    # Second line contains the cumulative snowfall data
    snowfall_data = list(map(int, lines[1].split()))
    
    # Validate that we have the correct number of data points
    if len(snowfall_data) != n:
        raise ValueError(f"Expected {n} data points, but got {len(snowfall_data)}")
    
    return snowfall_data


def main():
    """
    Main function to handle command line arguments and process the snowfall problem.
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
        snowfall_data = parse_input(input_file)
        
        # Calculate the result using the algorithm
        result = calculate_snowfall(snowfall_data)
        
        # Print the input data followed by the solution
        snowfall_str = ' '.join(map(str, snowfall_data))
        print(f"{snowfall_str} solution: {result.upper()}")
        
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()