import json
import sys

from pathlib import Path
from typing import Optional

from huffman_tree import (
    build_encoding_table,
    build_frequency_map,
    build_huffman_tree,
    print_tree,
)


def encode_text(text: str, encoding_table: dict[Optional[str], str]) -> str:
    return "".join(encoding_table[char] for char in text)


def write_compressed_file(
    encoded_bits: str,
    freq_map: dict[str, int],
    output_path: str
) -> None:
    padding = (8 - len(encoded_bits) % 8) % 8
    encoded_bits += "0" * padding
    
    byte_array = bytearray()
    for i in range(0, len(encoded_bits), 8):
        byte = encoded_bits[i:i+8]
        byte_array.append(int(byte, 2))
    
    metadata: dict[str, object] = {
        "frequency_map": freq_map,
        "padding": padding,
        "original_length": sum(freq_map.values())
    }
    
    output = Path(output_path)
    output.write_bytes(byte_array)
    
    metadata_path = output.with_suffix(output.suffix + ".meta")
    metadata_path.write_text(json.dumps(metadata, indent=2))
    
    print(f"\nCompressed data written to: {output_path}")
    print(f"Metadata written to: {metadata_path}")
    print(f"Original bits needed: {sum(freq_map.values()) * 8}")
    print(f"Compressed bits: {len(encoded_bits) - padding}")
    print(f"Compression ratio: {len(encoded_bits) - padding}/{sum(freq_map.values()) * 8} = {(len(encoded_bits) - padding) / (sum(freq_map.values()) * 8):.2%}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python huffman_encode.py <input_file> [output_file]")
        print("Example: python huffman_encode.py inputs/sample.txt")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        output_path = Path(input_path).stem + ".huffman"
    
    input_file = Path(input_path)
    if not input_file.exists():
        print(f"Error: File '{input_path}' not found")
        sys.exit(1)
    
    text = input_file.read_text(encoding="utf-8")
    if not text:
        print("Error: Input file is empty")
        sys.exit(1)
    
    print("=" * 70)
    print(f"Input File: {input_path}")
    print("=" * 70)
    print(f"\nOriginal text ({len(text)} characters):")
    print("-" * 70)

    if len(text) <= 500:
        print(text)
    else:
        print(text[:500] + f"\n... ({len(text) - 500} more characters)")
    
    print("\n" + "=" * 70)
    print("Frequency Map:")
    print("=" * 70)

    freq_map = build_frequency_map(text)
    
    sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    for char, freq in sorted_freq:
        char_display = repr(char) if char not in (' ', '\n', '\t') else {
            ' ': '<space>',
            '\n': '<newline>',
            '\t': '<tab>'
        }.get(char, repr(char))
        print(f"  {char_display:15} : {freq:5} ({freq/len(text)*100:5.2f}%)")
    
    print("\n" + "=" * 70)
    print("Huffman Tree:")
    print("=" * 70)
    root = build_huffman_tree(freq_map)
    print_tree(root)
    
    encoding_table = build_encoding_table(root)
    
    print("\n" + "=" * 70)
    print("Huffman Codes:")
    print("=" * 70)

    sorted_codes = sorted(encoding_table.items(), key=lambda x: (len(x[1]), x[0]))
    for char, code in sorted_codes:
        char_display = repr(char) if char not in (' ', '\n', '\t') else {
            ' ': '<space>',
            '\n': '<newline>',
            '\t': '<tab>'
        }.get(char, repr(char))
        print(f"  {char_display:15} : {code}")
    
    encoded_bits = encode_text(text, encoding_table)
    
    print("\n" + "=" * 70)
    print("Writing Compressed File:")
    print("=" * 70)
    write_compressed_file(encoded_bits, freq_map, output_path)
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
