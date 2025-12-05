import sys
import heapq


def read_input(filepath: str) -> tuple[int, int, int, list[tuple[int, int]]]:
    with open(filepath, 'r') as f:
        lines = f.read().strip().split('\n')
    
    n = int(lines[0])
    threshold = int(lines[1])
    drain = int(lines[2])
    
    cracks: list[tuple[int, int]] = []
    for i in range(3, 3 + n):
        time, size = map(int, lines[i].split())
        cracks.append((time, size))
    
    return n, threshold, drain, cracks


def simulate_flood(n: int, threshold: int, drain: int, cracks: list[tuple[int, int]]) -> tuple[bool, int, int]:
    """
    Simulate the flood.
    
    Strategy: Always fix the largest crack first (greedy approach).
    This minimizes water flow at each time step.
    """
    current_water = 0
    max_water = 0
    crack_index = 0
    unfixed_cracks: list[int] = []
    current_time = 0
    
    if cracks:
        last_crack_time = cracks[-1][0]
        max_time = last_crack_time + n
    else:
        return False, -1, 0
    
    while current_time <= max_time or unfixed_cracks:
        while crack_index < n and cracks[crack_index][0] == current_time:
            _, initial_size = cracks[crack_index]
            heapq.heappush(unfixed_cracks, -initial_size)
            crack_index += 1
        
        if unfixed_cracks:
            heapq.heappop(unfixed_cracks)
        
        water_in = sum(-crack_size for crack_size in unfixed_cracks)
        current_water = max(0, current_water + water_in - drain)
        max_water = max(max_water, current_water)
        
        if current_water >= threshold:
            return True, current_time, current_water
        
        if unfixed_cracks:
            temp = [-crack_size + 1 for crack_size in unfixed_cracks]
            unfixed_cracks = [-size for size in temp]
            heapq.heapify(unfixed_cracks)
        
        current_time += 1
        
        if crack_index >= n and not unfixed_cracks:
            break
    
    return False, -1, max_water


def main():
    if len(sys.argv) < 2:
        print("Usage: python flood.py <input_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    n, threshold, drain, cracks = read_input(filepath)
    flooded, time_unit, water_level = simulate_flood(n, threshold, drain, cracks)
    
    if flooded:
        print("FLOOD")
        print(time_unit)
        print(water_level)
    else:
        print("SAFE")
        print(water_level)


if __name__ == "__main__":
    main()
