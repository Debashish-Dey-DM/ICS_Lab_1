from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import math

# File paths (update these paths as needed)
input_file_path = "./Subst-Rijndael.crypt"
output_file_path = "./Subst.txt"
key_output_file_path = "./aes.key"
print (input_file_path)
def calculate_shannon_entropy(data):
    """Calculate Shannon entropy for a given data."""
    if not data:
        return 0
    freq = {}
    for byte in data:
        freq[byte] = freq.get(byte, 0) + 1
    entropy = -sum((f / len(data)) * math.log2(f / len(data)) for f in freq.values())
    return entropy

def brute_force_aes(input_file, output_file, key_output_file):
    # Load the encrypted file and extract the IV
    with open(input_file, "rb") as f:
        ciphertext = f.read()
    iv = ciphertext[:16]
    encrypted_data = ciphertext[16:]

    # Brute-force all possible 16-bit key combinations
    best_key = None
    best_plaintext = None
    lowest_entropy = float('inf')
    
    for key_fragment in range(65536):
        # Construct the 128-bit key: first 2 bytes are key_fragment, rest are 0
        key = key_fragment.to_bytes(2, 'big') + b'\x00' * 14
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        try:
            # Attempt to decrypt and unpad the data
            decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
            
            # Calculate Shannon entropy
            entropy = calculate_shannon_entropy(decrypted_data)
            
            # Check if this entropy is the lowest found
            if entropy < lowest_entropy:
                lowest_entropy = entropy
                best_key = key
                best_plaintext = decrypted_data
                
        except (ValueError, KeyError):
            # Skip keys that result in padding errors or decryption issues
            continue

    # Write the best plaintext to Subst.txt
    if best_plaintext:
        with open(output_file, "wb") as f:
            f.write(best_plaintext)

    # Write the discovered AES key to aes.key
    if best_key:
        with open(key_output_file, "w") as f:
            f.write(best_key.hex())
        print("AES Key found:", best_key.hex())
    else:
        print("Failed to find the correct AES key.")

# Run the brute-force function with specified file paths
brute_force_aes(input_file_path, output_file_path, key_output_file_path)
