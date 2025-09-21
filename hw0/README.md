# Homework 0

## Overview
This project implements a simple Python script that reads lines from standard input and prints them to standard output.

## Implementation Details

The `helloworld.py` script:
- Uses `sys.stdin` to read from standard input
- Iterates through each line in the input
- Strips trailing newlines using `rstrip('\n')` to avoid double newlines
- Prints each line to standard output using the `print()` function
- Includes proper error handling for KeyboardInterrupt and other exceptions

## How to Run

```bash
python helloworld.py < input_file
```
