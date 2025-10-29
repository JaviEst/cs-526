import sys
from pathlib import Path
from symbol_puzzle_game import symbol_puzzle_game


def parse_input(file_path: str) -> tuple[list[list[str]], list[str]]:
    """
    Parse the input file and return the board and symbols list.
    
    Args:
        file_path: Path to the input file
        
    Returns:
        Tuple containing:
        - 2D list representing the puzzle board
        - List of symbols to search for
    """
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    
    # First line contains the board size
    n = int(lines[0])
    
    # Second line contains the comma-separated symbols to search for
    symbols = [symbol.strip() for symbol in lines[1].split(',')]
    
    # Initialize board
    board: list[list[str]] = []
    
    # Process the next n lines to build the board
    for i in range(2, 2 + n):
        if i < len(lines):
            row = [cell.strip() for cell in lines[i].split(',')]
            # Validate row length
            if len(row) != n:
                raise ValueError(f"Row {i-1} has {len(row)} cells, expected {n}")
            board.append(row)
        else:
            raise ValueError(f"Expected {n} board rows, but only found {len(lines) - 2}")
    
    # Validate we have the correct number of rows
    if len(board) != n:
        raise ValueError(f"Expected {n} board rows, but got {len(board)}")
    
    return board, symbols


def print_board(board: list[list[str]]) -> None:
    """
    Print the board in a readable format.
    
    Args:
        board: 2D list representing the puzzle board
    """
    for row in board:
        print(' '.join(row))


def main():
    """
    Main function to handle command line arguments and process the symbol puzzle game.
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
        board, symbols = parse_input(input_file)
        
        print(f"Board size: {len(board)}x{len(board[0])}")
        print(f"Symbols: {symbols}")
        print("\nBoard:")
        print_board(board)
        print()
        
        # Run the symbol puzzle game algorithm
        result = symbol_puzzle_game(board, symbols)
        
        filename = Path(input_file).name
        print(f"{filename} -> {result}")
        
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()