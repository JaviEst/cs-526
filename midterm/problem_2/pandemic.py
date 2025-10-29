def pandemic_simulation(current_board: list[list[int]]) -> tuple[list[list[int]], str]:
    """
    Simulates the spread of a pandemic over a board of counties.

    Args:
        current_board: A 2D list representing the current state of the board.

    Returns:
        A string indicating whether there are any healthy counties left.
    """
    
    new_board = [row[:] for row in current_board]
    board_changed = True
    while board_changed:
        board_changed = False
        for i, row in enumerate(current_board):
            for j, cell in enumerate(row):
                # Check if neighbors are infected and update new_board accordingly
                if cell == 0:  # Only check healthy counties
                    # Check all four directions: up, down, left, right
                    neighbors = [
                        (i-1, j),  # up
                        (i+1, j),  # down
                        (i, j-1),  # left
                        (i, j+1)   # right
                    ]
                    
                    # Count infected neighbors
                    infected_neighbor_count = 0
                    for ni, nj in neighbors:
                        if (0 <= ni < len(current_board) and 
                            0 <= nj < len(current_board[0]) and 
                            current_board[ni][nj] == 1):
                            infected_neighbor_count += 1
                    
                    # County becomes infected if 2 or more neighbors are infected
                    if infected_neighbor_count >= 2:
                        new_board[i][j] = 1
                        board_changed = True
                

        current_board = [row[:] for row in new_board]

    if all(cell == 1 for row in new_board for cell in row):
        return new_board, "There are no healthy counties left."
    else:
        return new_board, "There are healthy counties left."