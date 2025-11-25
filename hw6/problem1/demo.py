import os
import sys
import time
from typing import Callable

from merge_sort import merge_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort

def sort_functions() -> list[tuple[str, Callable[[list[int]], list[int]]]]:
    return [
        ("insertion_sort", insertion_sort),
        ("merge_sort", merge_sort),
        ("quick_sort", quick_sort),
    ]


def read_numbers_from_file(path: str) -> list[int]:
    with open(path, 'r') as f:
        data = f.read().strip()
    # allow numbers separated by spaces or newlines
    parts = data.split()
    return [int(x) for x in parts]


def process_file(path: str) -> None:
    arr = read_numbers_from_file(path)
    n = len(arr)

    print('=' * 70)
    print(f'File Input: {path}')
    print(f'Number of values: {n}')
    print('=' * 70)

    for name, func in sort_functions():
        print('\n' + '-' * 70)
        print(f'Sorting Technique: {name}')
        print('-' * 70)

        a_copy = arr.copy()
        start = time.perf_counter()
        try:
            sorted_arr = func(a_copy)
        except Exception as e:
            print(f'Error while running {name}: {e}')
            continue
        elapsed_ms = (time.perf_counter() - start) * 1000.0
        correct = sorted_arr == sorted(arr)

        print(f'Time: {elapsed_ms:8.3f} ms')
        print(f'Correct: {correct}')
        print(f'Outputs: {sorted_arr}')

    print('\n' + '=' * 70)


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = input().strip()

    if not os.path.isfile(input_file):
        print(f"File Input: {input_file}")
        print(f"Error: File '{input_file}' not found")
        return

    process_file(input_file)


if __name__ == '__main__':
    main()
