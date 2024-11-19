def find_custom_keys(ciphertext, plaintext1, plaintext2):
    """Attempt to find byte-by-byte keys that map ciphertext to both plaintexts."""
    key1 = bytearray(len(ciphertext))
    key2 = bytearray(len(ciphertext))

    # Try to match each byte individually to create key mappings
    for i in range(len(ciphertext)):
        byte_found = False
        for k1_byte in range(256):
            for k2_byte in range(256):
                if (ciphertext[i] - k1_byte) % 256 == plaintext1[i] and \
                   (ciphertext[i] - k2_byte) % 256 == plaintext2[i]:
                    key1[i] = k1_byte
                    key2[i] = k2_byte
                    byte_found = True
                    break
            if byte_found:
                break
        if not byte_found:
            print(f"No matching bytes found for position {i}.")
            return None, None

    return bytes(key1), bytes(key2)

# Load ciphertext and plaintexts
with open('cipher.crypt', 'rb') as f:
    ciphertext = f.read()
with open('plaintext1.txt', 'rb') as f:
    plaintext1 = f.read().strip()
with open('plaintext2.txt', 'rb') as f:
    plaintext2 = f.read().strip()

# Find the keys
key1, key2 = find_custom_keys(ciphertext, plaintext1, plaintext2)

if key1 and key2:
    # Save the keys if both were successfully found
    with open("k1.key", "wb") as f1:
        f1.write(key1)
    with open("k2.key", "wb") as f2:
        f2.write(key2)
    print("Both keys found and saved.")
else:
    print("Could not find suitable keys.")
