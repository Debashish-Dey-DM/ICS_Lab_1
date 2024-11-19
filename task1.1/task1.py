from Crypto.Cipher import AES
import math
import itertools

# Load the encrypted data and IV
with open('./Subst-Rijndael.crypt', 'rb') as f:
    encrypted_data = f.read()

iv = encrypted_data[:16]  # The IV is the first 16 bytes
ciphertext = encrypted_data[16:]  # Rest is the ciphertext

# Shannon entropy function to help detect valid plaintext
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

# Attempt decryption with brute-forced keys
found_key = None
for key_part in range(2**16):
    # Create the weak 128-bit AES key with padding
    key = key_part.to_bytes(2, 'big') + b'\x00' * 14

    # Initialize AES cipher in CBC mode with the current key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    decrypted_data = cipher.decrypt(ciphertext)
    
    # Check for likely plaintext using entropy (lower entropy implies readable text)
    if shannon_entropy(decrypted_data) < 7:  # Adjust threshold if needed
        # Save decrypted result and key
        found_key = key
        with open('./Subst.txt', 'wb') as f:
            f.write(decrypted_data)
        with open('./aes.key', 'w') as f:
            f.write(key.hex())
        print(f"Key found: {key.hex()}")
        break

if found_key is None:
    print("No valid key found.")
else:
    print("Decryption complete.")
