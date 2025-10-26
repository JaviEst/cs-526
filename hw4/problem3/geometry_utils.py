import math


class Point:
    """Represents a 2D point with x and y coordinates"""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)
    
    def __hash__(self) -> int:
        return hash((round(self.x, 10), round(self.y, 10)))


def calculate_angle(origin: Point, point: Point) -> float:
    """
    Calculate the angle (in radians) from the origin to the point.
    Uses atan2 to get the angle relative to the positive x-axis.
    
    Args:
        origin: The reference point (origin)
        point: The point to calculate angle to
        
    Returns:
        Angle in radians [0, 2π)
    """
    dx = point.x - origin.x
    dy = point.y - origin.y
    
    # atan2 returns angle in range [-π, π]
    angle = math.atan2(dy, dx)
    
    # Normalize to [0, 2π)
    if angle < 0:
        angle += 2 * math.pi
    
    return angle
