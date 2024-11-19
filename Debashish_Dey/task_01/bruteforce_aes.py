from Crypto.Cipher import AES
import math
# Load the encrypted data and IV
with open('./Subst-Rijndael.crypt', 'rb') as f:
    encryptedData = f.read()

iv = encryptedData[:16]  
ciphertext = encryptedData[16:] 
entropyThreshold = 7  # Adjusting threshold based on expected plaintext entropy
# Shannon entropy function to help detect valid plaintext
def shannon_entropy(data):
    byteCounts = [0] * 256
    for byte in data:
        byteCounts[byte] += 1
    entropy = 0
    dataLen = len(data)
    for count in byteCounts:
        if count > 0:
            prob = count / dataLen
            entropy -= prob * math.log2(prob)
    return entropy
# Attempt decryption with brute-forced keys
finalKey = None
for partialKey in range(2**16):
    key = partialKey.to_bytes(2, 'big') + b'\x00' * 14  # Padding with zeros to make 16 bytes
    cipher = AES.new(key, AES.MODE_CBC, iv) # Initialize AES cipher with the key and IV
    decrypted = cipher.decrypt(ciphertext) 
    
    # Check for likely plaintext using entropy (lower entropy implies readable text)
    if shannon_entropy(decrypted) < entropyThreshold: 
        finalKey = key
        with open('./Subst.txt', 'wb') as f:
            f.write(decrypted) # Save the decrypted data to a file
        with open('./aes.key', 'w') as f:
            f.write(key.hex()) # Save the key to a file
        print(f"Key found: {key.hex()}")
        break

if finalKey is None:
    print("No valid key found.")
else:
    print("Decryption complete.")
