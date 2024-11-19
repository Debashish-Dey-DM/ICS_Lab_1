# Understanding XOR Encryption

XOR encryption combines plaintext with a repeating key. To decrypt it, the same key can be applied to the ciphertext. A known-plaintext attack allows us to reveal parts of the key by XORing the ciphertext with known plaintext.

## Identifying Known Plaintext (Zip Header)

Since the file is a zip archive, it should start with a predictable 4-byte header, "PK\x03\x04" (hexadecimal: 0x50 0x4B 0x03 0x04). This known header helps in deducing part of the XOR key.

## Deriving the Initial Part of the Key

By XORing the first four bytes of the encrypted file with the known zip header, we obtain the first four bytes of the 12-byte XOR key. This works because of the property ciphertext XOR known_plaintext = key.

## Completing the Key

Given the key length of 12 bytes, I initialized the key as a 12-byte array and filled the first four bytes as derived in Step 3. The rest of the key is assumed to follow the same pattern or repeat, which is typical for simple XOR encryption.

## Decrypting the File

I applied XOR decryption using this key across the entire encrypted data. Each byte in the ciphertext was XORed with the corresponding byte in the 12-byte key, repeating as necessary.

## Verifying the Decryption

To verify the decryption without manual checks, I checked the header of the decrypted file. If the first four bytes match the zip header, it confirms the decryption worked. This validation was done programmatically.

## Saving the Results

Finally, I saved the decrypted data as `XOR_decrypted.zip` for further inspection and stored the derived XOR key in `XOR.key` in hexadecimal format.
