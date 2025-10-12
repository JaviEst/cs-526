from geometry import LineSegment


def lines_intersect(line1: LineSegment, line2: LineSegment) -> bool:
    """
    Check if two infinite lines (defined by line segments) intersect.
    
    Since the streams continue infinitely in both directions, we need to check
    if the infinite lines intersect, not just the line segments.
    
    Args:
        line1: First line segment (defines the infinite line)
        line2: Second line segment (defines the infinite line)
        
    Returns:
        True if the infinite lines intersect, False if they are parallel
    """
    # Get points defining the lines
    p1, q1 = line1.p1, line1.p2
    p2, q2 = line2.p1, line2.p2
    
    # Calculate direction vectors
    dx1 = q1.x - p1.x
    dy1 = q1.y - p1.y
    dx2 = q2.x - p2.x
    dy2 = q2.y - p2.y
    
    # Calculate the determinant (cross product of direction vectors)
    det = dx1 * dy2 - dy1 * dx2
    
    # If determinant is 0, lines are parallel (or coincident)
    if abs(det) < 1e-10:
        return False
    
    # Lines intersect somewhere (since they're infinite)
    return True
