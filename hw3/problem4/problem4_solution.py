from typing import List
from input_parser import parse_ghostbusters_input
from ghostbusters_solver import solve_ghostbusters_problem


def solve_ghostbusters_from_input(input_data: List[str]) -> str:
    """
    Solve the Ghostbusters problem given input data.
    
    Args:
        input_data: List of strings representing the input
        
    Returns:
        Result string indicating if all ghosts were eliminated
    """
    ghostbusters, ghosts, error = parse_ghostbusters_input(input_data)
    
    if error:
        return f"All Ghosts: were not eliminated ({error})"
    
    return solve_ghostbusters_problem(ghostbusters, ghosts)


def process_ghostbusters_file(input_file: str, output_file: str = "") -> None:
    """
    Process an input file and solve the Ghostbusters problem.
    
    Args:
        input_file: Path to the input file
        output_file: Optional path to output file (if empty, prints to stdout)
    """
    results: List[str] = []
    
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        # Process the entire file as one test case
        input_data = [line.strip() for line in lines if line.strip()]
        
        if input_data:
            result = solve_ghostbusters_from_input(input_data)
            print(result)
            results.append(result)
        else:
            print("All Ghosts: were not eliminated (empty file)")
            results.append("All Ghosts: were not eliminated (empty file)")
        
        # Output results to file if specified
        if output_file:
            with open(output_file, 'w') as f:
                for result in results:
                    f.write(result + '\n')
                
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")


def main():
    """
    Main function to run the Ghostbusters problem solver.
    Can be used with command line arguments or interactively.
    """
    import sys
    
    if len(sys.argv) > 1:
        # Command line usage
        if sys.argv[1] == "-t" or sys.argv[1] == "--test":
            # Test with example data
            test_data = [
                "3",
                "B 0 0 G 2 2",
                "B 1 0 G 1 2", 
                "B 2 0 G 0 2"
            ]
            result = solve_ghostbusters_from_input(test_data)
            print("Test case result:", result)
        else:
            # File input
            input_file = sys.argv[1]
            output_file = sys.argv[2] if len(sys.argv) > 2 else ""
            process_ghostbusters_file(input_file, output_file)


if __name__ == "__main__":
    main()
