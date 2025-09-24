import sys

def main():
    """
    Read all lines from standard input and print them to standard output.
    """
    try:
        for line in sys.stdin:
            print(line.rstrip('\n'))
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
