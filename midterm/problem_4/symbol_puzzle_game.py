def symbol_puzzle_game(board: list[list[str]], symbols: list[str]) -> str:
    """
    Validate if a symbol puzzle board is in a valid state.
    
    Args:
        board: 2D list representing the puzzle board
        symbols: List of symbols that appear on the board
        
    Returns:
        String indicating "The board is valid." or "The board is invalid."
    """
    n = len(board)
    sqrt_n = int(n ** 0.5)
    
    # Check if n is a perfect square
    if sqrt_n * sqrt_n != n:
        return "The board is invalid."
    
    # Validate each row
    for row in board:
        seen_symbols: set[str] = set()
        for cell in row:
            if cell != '.':  # Skip empty cells
                if cell in seen_symbols:
                    return "The board is invalid."  # Duplicate in row
                seen_symbols.add(cell)
    
    # Validate each column
    for col in range(n):
        seen_symbols = set()
        for row in range(n):
            cell = board[row][col]
            if cell != '.':  # Skip empty cells
                if cell in seen_symbols:
                    return "The board is invalid."  # Duplicate in column
                seen_symbols.add(cell)
    
    # Validate each sub-board
    for sub_row in range(0, n, sqrt_n):
        for sub_col in range(0, n, sqrt_n):
            seen_symbols = set()
            # Check each cell in the current sub-board
            for row in range(sub_row, sub_row + sqrt_n):
                for col in range(sub_col, sub_col + sqrt_n):
                    cell = board[row][col]
                    if cell != '.':  # Skip empty cells
                        if cell in seen_symbols:
                            return "The board is invalid."  # Duplicate in sub-board
                        seen_symbols.add(cell)
    
    return "The board is valid."
