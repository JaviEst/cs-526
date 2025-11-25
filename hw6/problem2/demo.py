import os
import sys
import time

from radix_sort import radix_sort


def read_numbers(path: str) -> list[int]:
    with open(path, "r", encoding="utf-8") as handle:
        data = handle.read().strip()
    if not data:
        return []
    return [int(token) for token in data.split()]


def process_file(path: str) -> None:
    numbers = read_numbers(path)
    total = len(numbers)

    print("=" * 70)
    print(f"File Input: {path}")
    print(f"Number of values: {total}")
    print("=" * 70)

    start = time.perf_counter()
    try:
        sorted_numbers = radix_sort(numbers)
    except Exception as exc:  # surface unexpected issues without halting
        print(f"Error while running radix_sort: {exc}")
        return
    elapsed_ms = (time.perf_counter() - start) * 1000.0
    correct = sorted_numbers == sorted(numbers)

    print("\n" + "-" * 70)
    print("Sorting Technique: radix_sort")
    print("-" * 70)
    print(f"Time: {elapsed_ms:8.3f} ms")
    print(f"Correct: {correct}")
    print(f"Outputs: {sorted_numbers}")
    print("\n" + "=" * 70)


def main() -> None:
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = sys.stdin.readline().strip()

    if not target:
        print("Error: No input file provided")
        return

    if not os.path.isfile(target):
        print(f"File Input: {target}")
        print(f"Error: File '{target}' not found")
        return

    process_file(target)


if __name__ == "__main__":
    main()
