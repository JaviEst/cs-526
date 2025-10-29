import sys
from pathlib import Path
from pandemic import pandemic_simulation


def parse_input(file_path: str) -> list[list[int]]:
    """
    Parse the input file and return the initial board state.
    
    Args:
        file_path: Path to the input file
        
    Returns:
        2D list representing the board with 0 for healthy and 1 for infected counties
    """
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    
    # First line contains the board size
    n = int(lines[0])
    
    # Initialize board with all healthy counties (0)
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Process infected county coordinates
    for i in range(1, len(lines)):
        if lines[i].strip():  # Skip empty lines
            row, col = map(int, lines[i].split())
            # Validate coordinates are within bounds
            if 0 <= row < n and 0 <= col < n:
                board[row][col] = 1  # Mark as infected
            else:
                raise ValueError(f"Invalid coordinates ({row}, {col}) for board size {n}x{n}")
    
    return board


def print_board(board: list[list[int]]) -> None:
    """
    Print the board in a readable format.
    
    Args:
        board: 2D list representing the board state
    """
    for row in board:
        print(' '.join(map(str, row)))


def main():
    """
    Main function to handle command line arguments and process the pandemic problem.
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
        initial_board = parse_input(input_file)
        
        print("Initial board state:")
        print_board(initial_board)
        print()
        
        # Run the pandemic simulation
        result = pandemic_simulation(initial_board)
        
        print("Final board state:")
        print_board(result[0])
        print()
        print(result[1])

    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()