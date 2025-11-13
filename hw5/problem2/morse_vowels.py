import sys


# Morse code mapping for vowels only
VOWEL_MORSE: dict[str, str] = {
    'A': '.-',
    'E': '.',
    'I': '..',
    'O': '---',
    'U': '..-'
}


def count_vowel_sequences(morse_sequence: str) -> int:
    """
    Count the number of ways to decode a morse sequence into vowel-only letter sequences.
    
    Algorithm:
    - dp[i] represents the number of valid vowel-only decodings for sequence[0:i]
    - At each position, try to match each vowel's morse code
    - If a vowel matches at current position, add dp[previous_position] to dp[current_position]
    
    Time Complexity: O(n * k) where n is sequence length, k is number of vowels (5)
    Space Complexity: O(n) for the DP array
    
    Args:
        morse_sequence: String of dots and dashes
        
    Returns:
        Number of valid vowel-only decodings
    """
    morse_sequence_length = len(morse_sequence)
    
    if morse_sequence_length == 0:
        return 0
    
    # dp[i] = number of ways to decode sequence[0:i] into vowels only
    dp = [0] * (morse_sequence_length + 1)
    dp[0] = 1  # Empty sequence has one way (empty decoding)
    
    for i in range(1, morse_sequence_length + 1):
        for _, morse_code in VOWEL_MORSE.items():
            code_len = len(morse_code)
            
            if i >= code_len:
                # Extract the substring that would match this vowel
                substring = morse_sequence[i - code_len:i]
                
                # If it matches, add the number of ways to decode up to i-code_len
                if substring == morse_code:
                    dp[i] += dp[i - code_len]
    
    return dp[morse_sequence_length]


def process_file(filename: str) -> int:
    """
    Read morse sequence from file and count vowel combinations.
    
    File format:
    Line 1: Length of the sequence (n)
    Line 2: The morse sequence (dots and dashes)
    
    Args:
        filename: Path to input file
        
    Returns:
        Number of vowel combinations
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        morse_sequence = lines[1].strip()
    
    # Verify the sequence length matches
    if len(morse_sequence) != n:
        raise ValueError(f"Sequence length {len(morse_sequence)} doesn't match expected {n}")
    
    return count_vowel_sequences(morse_sequence)


def main():
    """Main program to process a morse vowel sequence file from stdin."""

    input_file = ""
    try:
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
        result = process_file(input_file)
        print(f"File Input: {input_file}")
        print(f"The Number of Vowel combinations is: {result}")

    except FileNotFoundError:
        print(f"\nFile Input: {input_file}")
        print(f"Error: File '{input_file}' not found")
    except Exception as e:
        print(f"\nFile Input: {input_file}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
