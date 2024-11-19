def custom_decrypt(ciphertext, key):
    """Decrypt the ciphertext by reversing the transformation used to create it."""
    return bytes([(c - k) % 256 for c, k in zip(ciphertext, key)])

# Load the original plaintexts
with open('plaintext1.txt', 'rb') as f:
    plaintext1 = f.read().strip()
with open('plaintext2.txt', 'rb') as f:
    plaintext2 = f.read().strip()

# Load the generated keys
with open('k1.key', 'rb') as f1:
    key1 = f1.read()
with open('k2.key', 'rb') as f2:
    key2 = f2.read()

# Load the ciphertext
with open('cipher.crypt', 'rb') as f:
    ciphertext = f.read()

# Decrypt the ciphertext with both keys
decrypted_with_k1 = custom_decrypt(ciphertext, key1)
decrypted_with_k2 = custom_decrypt(ciphertext, key2)

# Verify if decryption results match the plaintexts
if decrypted_with_k1 == plaintext1:
    print("Decryption with key1 matches plaintext1.")
else:
    print("Decryption with key1 does NOT match plaintext1.")

if decrypted_with_k2 == plaintext2:
    print("Decryption with key2 matches plaintext2.")
else:
    print("Decryption with key2 does NOT match plaintext2.")
