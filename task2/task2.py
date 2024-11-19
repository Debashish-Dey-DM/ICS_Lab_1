import math
from collections import Counter

def calculate_entropy(data):
    """Calculate the Shannon entropy of binary data."""
    if not data:
        return 0
    entropy = 0
    data_len = len(data)
    for x in range(256):
        p_x = data.count(x) / data_len
        if p_x > 0:
            entropy -= p_x * math.log2(p_x)
    return entropy

def inspect_byte_patterns(data, description):
    """Inspect the byte patterns by printing the most common byte values."""
    counter = Counter(data)
    print(f"\n{description} - Byte Patterns (Most common values):")
    for byte, count in counter.most_common(10):
        print(f"Byte: {byte}, Count: {count}")

# Load the files
with open('cipher.crypt', 'rb') as f:
    ciphertext = f.read()
with open('plaintext1.txt', 'rb') as f:
    plaintext1 = f.read().strip()
with open('plaintext2.txt', 'rb') as f:
    plaintext2 = f.read().strip()

# Calculate and display entropy
print(f"Entropy of ciphertext: {calculate_entropy(ciphertext):.4f}")
print(f"Entropy of plaintext1: {calculate_entropy(plaintext1):.4f}")
print(f"Entropy of plaintext2: {calculate_entropy(plaintext2):.4f}")

# Inspect byte patterns in each file
inspect_byte_patterns(ciphertext, "Ciphertext")
inspect_byte_patterns(plaintext1, "Plaintext 1")
inspect_byte_patterns(plaintext2, "Plaintext 2")
