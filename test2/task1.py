from Crypto.Cipher import AES
import itertools
import math

# Load the binary data
with open('./Subst-Rijndael.crypt', 'rb') as f:
    encrypted_data = f.read()

# Extract the IV (first 16 bytes of the encrypted data)
iv = encrypted_data[:16]
ciphertext = encrypted_data[16:]

# Shannon Entropy calculation
def shannon_entropy(data):
    byte_counts = [0] * 256
    for byte in data:
        byte_counts[byte] += 1
    entropy = 0
    data_len = len(data)
    for count in byte_counts:
        if count > 0:
            prob = count / data_len
            entropy -= prob * math.log2(prob)
    return entropy

# Brute-force through all 16-bit keys
correct_key = None
for key_part in range(2**16):
    # Create a 128-bit key by padding with zeros after the first 16 bits
    key = key_part.to_bytes(2, 'big') + b'\x00' * 14

    # Initialize AES cipher in CBC mode with the current key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Try to decrypt the ciphertext
    try:
        decrypted_data = cipher.decrypt(ciphertext)

        # Check entropy as a heuristic for plaintext detection
        entropy = shannon_entropy(decrypted_data)
        if entropy < 7:  # A threshold; plaintext usually has lower entropy
            # Save the key and decrypted data
            correct_key = key
            with open('Subst.txt', 'wb') as f:
                f.write(decrypted_data)
            with open('aes.key', 'w') as f:
                f.write(key.hex())
            print(f"Key found: {key.hex()}")
            break
    except Exception as e:
        # Skip any errors in decryption
        continue

if correct_key is None:
    print("No valid key found.")
else:
    print("Decryption completed successfully.")
