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
        return self.x == other.x and self.y == other.y


class LineSegment:
    """Represents a line segment between two points"""
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    
    def __str__(self) -> str:
        return f"Line from {self.p1} to {self.p2}"
    
    def __repr__(self) -> str:
        return f"LineSegment({self.p1}, {self.p2})"