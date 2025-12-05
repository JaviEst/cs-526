import json
import sys

from pathlib import Path

from huffman_tree import HuffmanNode, build_huffman_tree


def read_compressed_file(compressed_path: str) -> tuple[str, dict[str, int], int]:
    compressed_file = Path(compressed_path)
    metadata_file = compressed_file.with_suffix(compressed_file.suffix + ".meta")
    
    if not compressed_file.exists():
        raise FileNotFoundError(f"Compressed file not found: {compressed_path}")
    
    if not metadata_file.exists():
        raise FileNotFoundError(f"Metadata file not found: {metadata_file}")
    
    metadata = json.loads(metadata_file.read_text())
    freq_map = metadata["frequency_map"]
    padding = metadata["padding"]
    
    byte_data = compressed_file.read_bytes()
    
    bit_string = "".join(format(byte, "08b") for byte in byte_data)
    
    if padding > 0:
        bit_string = bit_string[:-padding]
    
    return bit_string, freq_map, metadata.get("original_length", 0)


def decode_text(encoded_bits: str, root: HuffmanNode | None) -> str:
    if root is None:
        return ""
    
    if root.is_leaf():
        if root.char is None:
            return ""
        return root.char * len(encoded_bits)
    
    decoded: list[str] = []
    current = root
    
    for bit in encoded_bits:
        if current is not None:
            if bit == "0":
                current = current.left
            else:
                current = current.right
        
        if current is not None and current.is_leaf():
            if current.char is not None:
                decoded.append(current.char)
            current = root
    
    return "".join(decoded)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python huffman_decode.py <compressed_file> [output_file]")
        print("Example: python huffman_decode.py sample.huffman")
        sys.exit(1)
    
    compressed_path = sys.argv[1]
    
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        output_path = Path(compressed_path).stem + "_decoded.txt"
    
    print("=" * 70)
    print(f"Compressed File: {compressed_path}")
    print("=" * 70)
    
    try:
        encoded_bits, freq_map, original_length = read_compressed_file(compressed_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    print(f"\nMetadata loaded:")
    print(f"  Original length: {original_length} characters")
    print(f"  Unique characters: {len(freq_map)}")
    print(f"  Encoded bits: {len(encoded_bits)}")
    
    print("\n" + "=" * 70)
    print("Rebuilding Huffman Tree from Frequency Map:")
    print("=" * 70)
    root = build_huffman_tree(freq_map)
    
    print("\n" + "=" * 70)
    print("Decoding:")
    print("=" * 70)
    decoded_text = decode_text(encoded_bits, root)
    
    print(f"Decoded {len(decoded_text)} characters")
    
    if len(decoded_text) != original_length:
        print(f"WARNING: Decoded length ({len(decoded_text)}) != original ({original_length})")
    else:
        print(f"✓ Length matches original")
    
    output_file = Path(output_path)
    output_file.write_text(decoded_text, encoding="utf-8")
    
    print(f"\nDecoded text written to: {output_path}")
    
    print("\n" + "=" * 70)
    print("Decoded Text Preview:")
    print("=" * 70)
    if len(decoded_text) <= 500:
        print(decoded_text)
    else:
        print(decoded_text[:500] + f"\n... ({len(decoded_text) - 500} more characters)")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
