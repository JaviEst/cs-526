from typing import List, Tuple
from geometry import Point


def parse_input_line(line: str) -> Tuple[List[Point], List[Point]]:
    """
    Parse a line of input to extract Ghostbuster and Ghost positions.
    
    Expected format: "B x1 y1 G x2 y2" or multiple B/G pairs
    
    Args:
        line: Input line containing B and G positions
        
    Returns:
        Tuple of (ghostbusters, ghosts) lists of Points
    """
    ghostbusters: List[Point] = []
    ghosts: List[Point] = []
    
    tokens = line.strip().split()
    i = 0
    
    while i < len(tokens):
        if tokens[i] == 'B':
            # Next two tokens should be x and y coordinates
            if i + 2 < len(tokens):
                try:
                    x = float(tokens[i + 1])
                    y = float(tokens[i + 2])
                    ghostbusters.append(Point(x, y))
                    i += 3
                except ValueError:
                    # Skip invalid coordinates
                    i += 3
            else:
                break
        elif tokens[i] == 'G':
            # Next two tokens should be x and y coordinates
            if i + 2 < len(tokens):
                try:
                    x = float(tokens[i + 1])
                    y = float(tokens[i + 2])
                    ghosts.append(Point(x, y))
                    i += 3
                except ValueError:
                    # Skip invalid coordinates
                    i += 3
            else:
                break
        else:
            i += 1
    
    return ghostbusters, ghosts


def parse_ghostbusters_input(input_data: List[str]) -> Tuple[List[Point], List[Point], str]:
    """
    Parse the complete input for the Ghostbusters problem.
    
    Args:
        input_data: List of strings representing the input
        
    Returns:
        Tuple of (ghostbusters, ghosts, error_message)
        If error_message is not empty, there was a parsing error
    """
    if not input_data:
        return [], [], "No input provided"
    
    try:
        n = int(input_data[0].strip())
        
        if n == 0:
            return [], [], ""  # No error, just no ghosts to eliminate
        
        if len(input_data) < n + 1:
            return [], [], f"Expected {n + 1} lines, got {len(input_data)}"
        
        all_ghostbusters: List[Point] = []
        all_ghosts: List[Point] = []
        
        # Parse each line to extract positions
        for i in range(1, n + 1):
            if i < len(input_data):
                ghostbusters, ghosts = parse_input_line(input_data[i])
                all_ghostbusters.extend(ghostbusters)
                all_ghosts.extend(ghosts)
        
        if len(all_ghostbusters) != n:
            return [], [], f"Expected {n} ghostbusters, found {len(all_ghostbusters)}"
        
        if len(all_ghosts) != n:
            return [], [], f"Expected {n} ghosts, found {len(all_ghosts)}"
        
        return all_ghostbusters, all_ghosts, ""
        
    except (ValueError, IndexError) as e:
        return [], [], f"Parse error: {e}"