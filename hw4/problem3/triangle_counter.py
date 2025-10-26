import math

from collections import defaultdict

from geometry_utils import Point, calculate_angle


def count_right_triangles_optimized(points: list[Point]) -> int:
    """
    Count the number of right triangles that can be formed from the given points.
    
    Optimization: For each point as the origin (potential right angle vertex),
    calculate angles to all other points. Two points form a right triangle with
    the origin if their angles differ by 90 degrees.
    
    Time Complexity: O(n²) where n is the number of points
    Space Complexity: O(n) for storing angles
    
    Args:
        points: List of Point objects
        
    Returns:
        Number of unique right triangles
    """
    n = len(points)
    if n < 3:
        return 0
    
    total_count = 0
    
    # For each point, treat it as the potential right angle vertex
    for i in range(n):
        origin = points[i]
        
        # Calculate angles from origin to all other points
        angle_map: dict[int, list[int]] = defaultdict(list)
        
        for j in range(n):
            if i == j:
                continue
            
            angle = calculate_angle(origin, points[j])
            # Convert to degrees for cleaner arithmetic and better precision
            angle_degrees = math.degrees(angle)
            # Convert to integer by scaling - avoids floating point rounding issues
            # Scale by 10^9 to preserve precision, then convert to int
            angle_key = int(round(angle_degrees * 1_000_000_000))
            angle_map[angle_key].append(j)
        
        angles = list(angle_map.keys())
        
        for angle in angles:
            # Calculate perpendicular angle: add 90 degrees (in integer form)
            # 90 degrees * 10^9 = 90_000_000_000
            perp_key = angle + 90_000_000_000
            
            # Normalize angle to [0, 360) degrees in integer form
            # 360 degrees * 10^9 = 360_000_000_000
            if perp_key >= 360_000_000_000:
                perp_key -= 360_000_000_000
            
            # Count combinations with perpendicular angles
            count_at_angle = len(angle_map.get(angle, []))
            count_at_perp = len(angle_map.get(perp_key, []))

            # Each point at current angle can pair with each point at perpendicular angle
            total_count += count_at_angle * count_at_perp
    
    return total_count
