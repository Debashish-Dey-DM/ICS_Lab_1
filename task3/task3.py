# Load the encrypted file data
with open("XOR.zip.crypt", "rb") as file:
    encrypted_data = file.read()
# Known ZIP file header (4 bytes)
known_plaintext = bytes([0x50, 0x4B, 0x03, 0x04])
# Derive the first few bytes of the key by XORing with known plaintext
key_fragment = bytearray()
for i in range(len(known_plaintext)):
    key_fragment.append(encrypted_data[i] ^ known_plaintext[i])

# Extend the fragment to the full 12-byte key if possible
key_length = 12
key = key_fragment * (key_length // len(key_fragment)) + key_fragment[:key_length % len(key_fragment)]
# XOR decryption function
def xor_decrypt(data, key):
    return bytearray(data[i] ^ key[i % len(key)] for i in range(len(data)))

# Decrypt the file using the derived key
decrypted_data = xor_decrypt(encrypted_data, key)
# Write the decrypted data to a new file to inspect the result
with open("decrypted_XOR.zip", "wb") as output_file:
    output_file.write(decrypted_data)

# Save the key as a hexadecimal string
with open("XOR.key", "w") as key_file:
    key_file.write(key.hex())
