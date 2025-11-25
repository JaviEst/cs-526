import os
import sys
import time

from gale_shapley import gale_shapley, is_stable, parse_preferences


def read_lines(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.readlines()


def process_file(path: str) -> None:
    raw_lines = read_lines(path)
    start_parse = time.perf_counter()
    try:
        men_prefs, women_prefs = parse_preferences(raw_lines)
    except ValueError as exc:
        print(f"Error parsing file '{path}': {exc}")
        return
    parse_ms = (time.perf_counter() - start_parse) * 1000.0

    participant_count = len(men_prefs)

    print("=" * 70)
    print(f"File Input: {path}")
    print(f"Number of participants: {participant_count}")
    print(f"Parse Time: {parse_ms:8.3f} ms")
    print("=" * 70)

    start = time.perf_counter()
    matches = gale_shapley(men_prefs, women_prefs)
    elapsed_ms = (time.perf_counter() - start) * 1000.0

    stability = is_stable(matches, men_prefs, women_prefs)
    sorted_pairs = sorted(matches.items(), key=lambda pair: pair[0])

    print("\n" + "-" * 70)
    print("Algorithm: gale_shapley")
    print("-" * 70)
    print(f"Time: {elapsed_ms:8.3f} ms")
    print(f"Stable: {stability}")
    print("Matches (man woman):")
    for man, woman in sorted_pairs:
        print(f"{man} {woman}")
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
