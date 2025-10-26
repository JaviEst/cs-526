import sys

from typing import List

from geometry_utils import Point
from triangle_counter import count_right_triangles_optimized
import time


def solve_from_input(input_data: List[str]) -> int:
    """
    Parse input data and solve the problem.
    
    Args:
        input_data: List of strings containing input
        
    Returns:
        Number of right triangles
    """
    if not input_data:
        raise ValueError("Empty input data")
    
    n = int(input_data[0].strip())
    
    if len(input_data) < n + 1:
        raise ValueError(f"Expected {n + 1} lines, got {len(input_data)}")
    
    points: List[Point] = []
    for i in range(1, n + 1):
        parts = input_data[i].strip().split()
        if len(parts) != 2:
            raise ValueError(f"Line {i + 1}: Expected 2 coordinates, got {len(parts)}")
        
        x = float(parts[0])
        y = float(parts[1])
        points.append(Point(x, y))
    
    if len(points) != n:
        raise ValueError(f"Expected {n} points, parsed {len(points)}")
    
    start_time = time.time()
    count = count_right_triangles_optimized(points)
    stop_time = time.time()
    elapsed_time = stop_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")

    return count


def process_file(input_file: str, output_file: str = "") -> None:
    """
    Process an input file and count right triangles.
    
    Args:
        input_file: Path to the input file
        output_file: Optional path to output file (if empty, prints to stdout)
    """
    results: List[str] = []
    
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        count = solve_from_input(lines)
        
        # Format output as specified
        result = f"The number of right triangles is: {count}"
        
        print(result)
        results.append(result)
        
        # Output to file if specified
        if output_file:
            with open(output_file, 'w') as f:
                for result_line in results:
                    f.write(result_line + '\n')
                
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")


def process_stdin() -> None:
    """
    Process input from stdin.
    """
    try:
        lines = sys.stdin.readlines()
        count = solve_from_input(lines)
        
        # Format output as specified
        result = f"The number of right triangles is: {count}"
        
        print(result)
        
    except Exception as e:
        print(f"Error processing input: {e}")


def main():
    """
    Main function to count right triangles.
    Can be used with command line arguments or interactively.
    """
    if len(sys.argv) > 1:
        # Command line usage
        if sys.argv[1] == "-s" or sys.argv[1] == "--stdin":
            # Stdin input
            process_stdin()
        else:
            # File input
            input_file = sys.argv[1]
            output_file = sys.argv[2] if len(sys.argv) > 2 else ""
            process_file(input_file, output_file)
    else:
        # Interactive usage
        choice = input("Process (f)ile or (i)nput directly? ").lower()
        
        if choice == 'i' or choice == 'input':
            print("Enter number of points:")
            n = int(input().strip())
            
            print("Enter points (x y coordinates, one per line):")
            input_data = [str(n)]
            
            for i in range(n):
                line = input(f"Point {i + 1}: ")
                input_data.append(line)
            
            try:
                count = solve_from_input(input_data)
                result = f"The number of right triangles is: {count}"
                print(result)
            except ValueError as e:
                print(f"Error: {e}")
                return
        else:
            input_file = input("Enter the input file path: ")
            output_choice = input("Output to file? (y/n): ").lower()
            output_file = ""
            if output_choice == 'y':
                output_file = input("Enter the output file path: ")
            
            process_file(input_file, output_file)


if __name__ == "__main__":
    main()