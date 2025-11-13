import sys


def find_longest_alternating_sequence(A: list[int], B: list[int]) -> list[int]:
    """
    Find the longest alternating increasing subsequence from arrays A and B.
    
    Args:
        A: First sequence of integers
        B: Second sequence of integers
        
    Returns:
        Longest alternating increasing subsequence
    """
    if not A or not B:
        return []
    
    result1 = find_alternating_ab(A, B)  # Start with A
    result2 = find_alternating_ab(B, A)  # Start with B
    
    return result1 if len(result1) >= len(result2) else result2


def find_alternating_ab(A: list[int], B: list[int]) -> list[int]:
    """
    Find longest alternating sequence starting with an element from A.
    
    KEY CONSTRAINT (synchronized indices):
    - When at A[i], look for B[j] where j >= i+1 and B[j] > A[i]
    - When at B[j], look for A[i] where i >= j+1 and A[i] > B[j]
    """
    n, m = len(A), len(B)
    
    # Memoization: memo_a[i] = (max_length, next_index) for sequences starting at A[i]
    # memo_b[j] = (max_length, next_index) for sequences starting at B[j]
    memo_a: dict[int, tuple[int, int, str]] = {}
    memo_b: dict[int, tuple[int, int, str]] = {}
    
    def dp_from_a(a_idx: int) -> tuple[int, int, str]:
        """
        Returns (max_length, next_b_index, 'B') or (1, -1, '') if can't extend.
        """
        if a_idx in memo_a:
            return memo_a[a_idx]
        
        curr_val = A[a_idx]
        best_len = 1
        best_next = -1
        best_type = ''
        
        # Try extending to B[j] where j >= a_idx+1 and B[j] > curr_val
        for j in range(a_idx + 1, m):
            if B[j] > curr_val:
                length_from_b, _, _ = dp_from_b(j)
                total_len = 1 + length_from_b
                if total_len > best_len:
                    best_len = total_len
                    best_next = j
                    best_type = 'B'
        
        memo_a[a_idx] = (best_len, best_next, best_type)
        return memo_a[a_idx]
    
    def dp_from_b(b_idx: int) -> tuple[int, int, str]:
        """
        Returns (max_length, next_a_index, 'A') or (1, -1, '') if can't extend.
        """
        if b_idx in memo_b:
            return memo_b[b_idx]
        
        curr_val = B[b_idx]
        best_len = 1
        best_next = -1
        best_type = ''
        
        # Try extending to A[i] where i >= b_idx+1 and A[i] > curr_val
        for i in range(b_idx + 1, n):
            if A[i] > curr_val:
                length_from_a, _, _ = dp_from_a(i)
                total_len = 1 + length_from_a
                if total_len > best_len:
                    best_len = total_len
                    best_next = i
                    best_type = 'A'
        
        memo_b[b_idx] = (best_len, best_next, best_type)
        return memo_b[b_idx]
    
    # Compute DP values for all positions
    for i in range(n):
        dp_from_a(i)
    
    # Find the best starting position
    best_len = 0
    best_start_idx = 0
    
    for i in range(n):
        length, _, _ = memo_a[i]
        if length > best_len:
            best_len = length
            best_start_idx = i
    
    # Reconstruct the sequence
    sequence: list[int] = []
    curr_idx = best_start_idx
    curr_type = 'A'
    
    while curr_idx != -1:
        if curr_type == 'A':
            sequence.append(A[curr_idx])
            _, next_idx, next_type = memo_a[curr_idx]
        else:
            sequence.append(B[curr_idx])
            _, next_idx, next_type = memo_b[curr_idx]
        
        curr_idx = next_idx
        curr_type = next_type
    
    return sequence


def process_file(filename: str) -> tuple[list[int], list[int], list[int]]:
    """
    Read input file and compute longest alternating sequence.
    
    File format:
    Line 1: Size of array A
    Line 2: Size of array B
    Line 3: Elements of A (space-separated)
    Line 4: Elements of B (space-separated)
    
    Args:
        filename: Path to input file
        
    Returns:
        Tuple of (A, B, longest_sequence)
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        size_a = int(lines[0].strip())
        size_b = int(lines[1].strip())
        A = list(map(int, lines[2].strip().split()))
        B = list(map(int, lines[3].strip().split()))
    
    if len(A) != size_a:
        raise ValueError(f"Array A size mismatch: expected {size_a}, got {len(A)}")
    if len(B) != size_b:
        raise ValueError(f"Array B size mismatch: expected {size_b}, got {len(B)}")
    
    longest_seq = find_longest_alternating_sequence(A, B)
    return A, B, longest_seq


def main():
    """Main program to process a longest sequence file from stdin."""
    
    input_file = ""
    try:
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
        _, _, result = process_file(input_file)

        print(f"File Input: {input_file}")
        print(f"Longest Sequence: {' '.join(map(str, result))}")
        print(f"Length: {len(result)}")

    except FileNotFoundError:
        print(f"File Input: {input_file}")
        print(f"Error: File not found")
    except Exception as e:
        print(f"File Input: {input_file}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
