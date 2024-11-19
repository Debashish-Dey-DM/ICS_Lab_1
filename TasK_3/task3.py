import binascii

# Load the encrypted file
with open('./XOR.zip.crypt', 'rb') as f:
    encryptedData = f.read()

knownHeader = b'\x50\x4B\x03\x04' # Known plaintext header for a zip file (magic number "PK" in hexadecimal)


keyLength = 12 #(96 bits = 12 bytes)

key = bytearray([0] * keyLength) # Initialize the key with zeros


for i in range(len(knownHeader)):
    key[i] = encryptedData[i] ^ knownHeader[i] # XOR the known header with the encrypted data to derive the key

# XOR decryption function
def xor_decrypt(data, key):
    decrypted = bytearray(len(data)) # Initialize the decrypted data with zeros
    for i in range(len(data)):
        decrypted[i] = data[i] ^ key[i % len(key)] # XOR each byte of the encrypted data with the key
    return decrypted

decrypted = xor_decrypt(encryptedData, key) # Decrypt the encrypted data using the derived key

# Verify if the decrypted data is a valid zip by checking the header
if decrypted[:4] == knownHeader:
    print("Decryption successful: Valid zip file header found.")
else:
    print("Decryption may be incorrect: Zip file header not found.")

# Save the decrypted data as a zip file
with open('./XOR_decrypted.zip', 'wb') as f:
    f.write(decrypted)

# Convert the key to hexadecimal format
key_hex = binascii.hexlify(key).decode()

# Store the derived key in XOR.key as a hexadecimal string
with open('./XOR.key', 'w') as f:
    f.write(key_hex)

