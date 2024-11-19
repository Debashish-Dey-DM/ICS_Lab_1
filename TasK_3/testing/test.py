def derive_xor_key(ciphertext_path, known_plaintext):
    # Open the encrypted file in binary mode
    with open(ciphertext_path, 'rb') as f:
        ciphertext = f.read()

    # The known ZIP file header (as bytes)
    known_header = bytes.fromhex(known_plaintext)  # Example: '504B0304' is ZIP header

    # Calculate the key by XOR-ing the first bytes of the encrypted file with the known plaintext
    key = bytearray()
    for i in range(len(known_header)):
        key_byte = ciphertext[i] ^ known_header[i]
        key.append(key_byte)

    # The 96-bit key requires 12 bytes (assuming repeating pattern derived from the initial segment)
    # Extend the key up to 12 bytes if the ciphertext segment does not provide enough data
    full_key = key * (12 // len(key)) + key[:12 % len(key)]

    # Print and save the derived key in hexadecimal
    key_hex = full_key.hex()
    print(f"Derived XOR Key (Hex): {key_hex}")

    # Save the key to a file
    with open('XOR.key', 'w') as key_file:
        key_file.write(key_hex)

# Example usage
ciphertext_path = 'XOR.zip.crypt'
known_plaintext = '504B0304'  # ZIP header in hexadecimal
derive_xor_key(ciphertext_path, known_plaintext)
