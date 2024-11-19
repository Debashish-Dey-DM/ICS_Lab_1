# Algorithm Description

The approach used **XOR-based** encryption properties to derive the encryption keys (k1 and k2) that allow the ciphertext to be decrypted into two different plaintexts. The main steps in the process are outlined below:
This approach demonstrated how XOR-based encryption can be reversed by using a known-plaintext attack. Both keys were successfully recovered, stored, and verified, underscoring the importance of XOR properties in cryptographic analysis.

## Steps

### Loading and Preparing Data:

- Loaded the ciphertext (`cipher.crypt`) and both plaintexts (`plaintext1.txt` and `plaintext2.txt`).
- Converted each to byte sequences, as XOR operations work directly on byte values.

### Truncation to Handle Length Differences:

- Calculated the minimum length among the ciphertext and both plaintexts, then truncated all data to this length. This ensured consistent XOR operations without mismatches due to differing lengths.

### Deriving Keys Using XOR:

- Used XOR to derive two possible keys:
  - `k1` was derived by XORing the truncated ciphertext with `plaintext1`.
  - `k2` was derived by XORing the truncated ciphertext with `plaintext2`.
- This step leveraged the XOR property that ciphertext XOR plaintext = key.

### Verification of Derived Keys:

- Verified each derived key by XORing it back with the respective plaintext to see if it recreated the original truncated ciphertext.
- Both keys passed verification, confirming they were correct.

### Saving the Keys:

- Saved the derived keys (`k1` and `k2`) in hexadecimal format to `key1.key` and `key2.key`.

## Results and Observations

- **XOR’s Invertibility:** XOR encryption allows the ciphertext to be decrypted using the same operation with the original key, making it susceptible to known-plaintext attacks.
- **Effective Key Recovery:** By leveraging known plaintexts, the encryption keys were successfully derived and verified.
