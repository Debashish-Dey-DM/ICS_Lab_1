# Loading plaintexts and ciphertext
with open('./plaintext1.txt', 'r') as f:
    plainText1 = f.read()
with open('./plaintext2.txt', 'r') as f:
    plainText2 = f.read()
with open('./cipher.crypt', 'rb') as f:
    cipherText = f.read()

# print("Plaintext 1:", plaintext1)
# print("Plaintext 2:", plaintext2)
# print("Ciphertext:", ciphertext)

# XOR bytes function for keys
def xorBytes(bytes1, bytes2):
    return bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])

# Converting to byte format
plaintext1Bytes = plainText1.encode('utf-8')
plaintext2Bytes = plainText2.encode('utf-8')
ciphertextBytes = cipherText

# avoiding truncation issues
min_len = min(len(ciphertextBytes), len(plaintext1Bytes), len(plaintext2Bytes))
trimCiphertext = ciphertextBytes[:min_len]
trimPlaintext1 = plaintext1Bytes[:min_len]
trimPlaintext2 = plaintext2Bytes[:min_len]
print("trimCiphertext:", len(trimCiphertext))
print("lengthText1", len(trimPlaintext1) , "trimmedText1:", trimPlaintext1)
print("lengthText2", len(trimPlaintext2) , "trimmedText2:", trimPlaintext2)

# Finding the keys using XOR
try:
    k1 = xorBytes(trimCiphertext, trimPlaintext1)
    k2 = xorBytes(trimCiphertext, trimPlaintext2)
    print("found keys")
except Exception as e:
    print(e)
    
# Verification of keys
testCipher1 = xorBytes(trimPlaintext1, k1)
testCipher2 = xorBytes(trimPlaintext2, k2)
isXorK1 = (testCipher1 == trimCiphertext)
isXorK2 = (testCipher2 == trimCiphertext)

print("XORk1", isXorK1)
print("XORk2:", isXorK2)

if isXorK1 and isXorK2:
    # print("Key k1", k1.hex())
    # print("Key k2", k2.hex())
    with open('./key1.key', 'w') as f:
        f.write(k1.hex())

    with open('./key2.key', 'w') as f:
        f.write(k2.hex())
else:
    print("Not XOR")

print("Complete")
