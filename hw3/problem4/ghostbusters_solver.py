from typing import List
from geometry import Point, LineSegment
from line_intersection import lines_intersect


def can_eliminate_all_ghosts(ghostbusters: List[Point], ghosts: List[Point]) -> bool:
    """
    Determine if all ghosts can be eliminated without streams crossing.
    
    This function checks if there exists a pairing between ghostbusters and ghosts
    such that no two line segments (streams) intersect.
    
    For this implementation, we assume the pairing is given in order:
    - 1st ghostbuster paired with 1st ghost
    - 2nd ghostbuster paired with 2nd ghost
    - etc.
    
    Args:
        ghostbusters: List of Ghostbuster positions
        ghosts: List of Ghost positions
        
    Returns:
        True if all ghosts can be eliminated, False if streams would cross
    """
    n = len(ghostbusters)
    if n != len(ghosts):
        return False
    if n <= 1:
        return True
    
    # Create line segments (streams) for each ghostbuster-ghost pair
    streams: List[LineSegment] = []
    for i in range(n):
        stream = LineSegment(ghostbusters[i], ghosts[i])
        streams.append(stream)
    
    # Check if any two streams intersect (using infinite lines)
    for i in range(n):
        for j in range(i + 1, n):
            if lines_intersect(streams[i], streams[j]):
                return False
    
    return True


def solve_ghostbusters_problem(ghostbusters: List[Point], ghosts: List[Point]) -> str:
    """
    Solve the Ghostbusters problem and return the result message.
    
    Args:
        ghostbusters: List of Ghostbuster positions
        ghosts: List of Ghost positions
        
    Returns:
        Result string indicating if all ghosts were eliminated
    """
    if not ghostbusters and not ghosts:
        return "All Ghosts: were eliminated (no ghosts to eliminate)"
    
    if len(ghostbusters) != len(ghosts):
        return "All Ghosts: were not eliminated (unequal numbers of ghostbusters and ghosts)"
    
    can_eliminate = can_eliminate_all_ghosts(ghostbusters, ghosts)
    
    if can_eliminate:
        return "All Ghosts: were eliminated"
    else:
        return "All Ghosts: were not eliminated"