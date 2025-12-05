import sys


def read_input(filepath: str) -> tuple[int, int, list[list[int]]]:
    with open(filepath, 'r') as f:
        lines = f.read().strip().split('\n')
    
    m = int(lines[0])
    n = int(lines[1])
    
    matrix: list[list[int]] = []
    for i in range(2, 2 + m):
        row = list(map(int, lines[i].split()))
        matrix.append(row)
    
    return m, n, matrix


def find_longest_ski_path(m: int, n: int, matrix: list[list[int]]) -> int:
    """
    Find the longest downhill path in the matrix.
    
    Each cell can move to any of its 8 neighbors (horizontal, vertical, diagonal)
    if the neighbor has a lower altitude.
    
    dp[i][j] = longest path starting from cell (i, j)
    """
    dp = [[-1] * n for _ in range(m)]
    
    # 8 directions: up, down, left, right, and 4 diagonals
    directions = [
        (-1, 0),   # up
        (1, 0),    # down
        (0, -1),   # left
        (0, 1),    # right
        (-1, -1),  # up-left
        (-1, 1),   # up-right
        (1, -1),   # down-left
        (1, 1)     # down-right
    ]
    
    def dfs(row: int, col: int) -> int:
        """
        DFS with memoization to find longest path from (row, col).
        Returns the length of the longest path starting from this cell.
        """
        if dp[row][col] != -1:
            return dp[row][col]
        
        # Base case: at minimum, the path length is 1 (the cell itself)
        max_length = 1
        current_altitude = matrix[row][col]
        
        # Try all 8 neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < m and 0 <= new_col < n:
                neighbor_altitude = matrix[new_row][new_col]
                
                if neighbor_altitude < current_altitude:
                    path_length = 1 + dfs(new_row, new_col)
                    max_length = max(max_length, path_length)
        
        dp[row][col] = max_length
        return max_length
    
    longest = 0
    for i in range(m):
        for j in range(n):
            path_length = dfs(i, j)
            longest = max(longest, path_length)
    
    return longest


def main():
    if len(sys.argv) < 2:
        print("Usage: python ski.py <input_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    m, n, matrix = read_input(filepath)
    result = find_longest_ski_path(m, n, matrix)

    # The path length counts cells, but the answer is the longest path which is cells - 1
    print(result - 1)


if __name__ == "__main__":
    main()
