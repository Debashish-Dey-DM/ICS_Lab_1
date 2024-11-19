# Algorithm Description

The overall approach involved comparing the given plaintexts to the ciphertext and attempting to derive possible encryption keys using XOR operations. The main steps are as follows:

## Loading Data

- Load the ciphertext and plaintexts.
- The plaintexts are read as strings and then converted to byte sequences for further processing.

## Conversion to Byte Format

- Convert all text data (plaintexts and ciphertext) to byte arrays to facilitate XOR operations on byte values.

## Handling Truncation Issues

- Since the lengths of the plaintexts and ciphertext could differ, determine the minimum length among the inputs and truncate them accordingly.
- This ensures that the XOR operation does not fail due to mismatched lengths.

## Key Derivation Using XOR

- Use the XOR operation to derive potential keys by XORing the trimmed ciphertext with each of the trimmed plaintexts.
- Compute the potential keys as follows:
  - `k1 = XOR(trimCiphertext, trimPlaintext1)`
  - `k2 = XOR(trimCiphertext, trimPlaintext2)`
- Use a try-except block to catch and handle any errors that may occur during this process.

## Verification of Keys

- Verify if the derived keys are correct by testing each key to recreate the original ciphertext.
- Specifically, XOR each plaintext with the corresponding derived key (`k1` or `k2`) and check if the result matches the original ciphertext (`trimCiphertext`).
- If both tests return true, verification is considered successful, indicating that the encryption is XOR-based.

## Storing Keys

- If the verification step is successful, save the derived keys (`k1` and `k2`) in hexadecimal format to `key1.key` and `key2.key` respectively.
- Print the keys in hexadecimal format for inspection.

## Results and Analysis

- The verification of the derived keys (`k1` and `k2`) confirmed that the encryption was XOR-based.
- Both keys were able to successfully recreate the original ciphertext when XORed with their respective plaintexts, providing strong evidence that XOR was the method of encryption used.
- The recovered keys were saved to `key1.key` and `key2.key` in hexadecimal format.

### Key Observations

- **XOR Characteristics**: The nature of XOR allows decryption by applying the same operation with the original key. This makes XOR encryption simple to reverse if a plaintext-ciphertext pair is known.
- **Truncation**: Proper handling of different input lengths was crucial to ensure that the XOR operation did not encounter errors due to length mismatches.

## Conclusion

The implemented algorithm was able to successfully recover the keys from the given plaintext-ciphertext pairs. By leveraging the properties of XOR, we derived the encryption keys, confirmed their validity through verification, and stored them for further use. This process highlights the importance of understanding the properties of the XOR operation in cryptographic analysis, especially when dealing with known-plaintext attacks.
