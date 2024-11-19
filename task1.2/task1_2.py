import random
from ngram_score import ngram_score
from collections import Counter

# Load quadgram scorer
quadgram_scorer = ngram_score('./english_quadgrams.txt')

# Load the ciphertext
with open('./Subst.txt', 'r') as f:
    ciphertext = f.read().replace("\n", " ")

# English letter frequencies as a reference for initializing key
ENGLISH_FREQ_ORDER = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

# Initialize the key based on frequency analysis
def initialize_key(ciphertext):
    # Frequency analysis on the ciphertext
    ciphertext_counts = Counter(char for char in ciphertext if char.isalpha())
    sorted_ciphertext_chars = [char for char, _ in ciphertext_counts.most_common()]
    
    # Create initial key mapping by matching frequency order with ciphertext characters
    key = [''] * 26
    for i, char in enumerate(sorted_ciphertext_chars):
        if i < len(ENGLISH_FREQ_ORDER):
            key[ord(char) - ord('A')] = ENGLISH_FREQ_ORDER[i]
    
    # Fill any remaining unmapped characters randomly
    remaining_chars = [c for c in ENGLISH_FREQ_ORDER if c not in key]
    for i in range(26):
        if key[i] == '':
            key[i] = remaining_chars.pop(0)
            
    return ''.join(key)

# Function to apply a key for decryption
def decrypt_with_key(ciphertext, key):
    table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", key)
    return ciphertext.translate(table)

# Hill-climbing function to optimize the decryption key
def hill_climb(ciphertext, initial_key, max_iterations=1000):
    best_key = initial_key
    best_score = quadgram_scorer.score(decrypt_with_key(ciphertext, best_key))
    best_decryption = decrypt_with_key(ciphertext, best_key)

    for i in range(max_iterations):
        # Swap two random letters in the key
        new_key = list(best_key)
        a, b = random.sample(range(26), 2)
        new_key[a], new_key[b] = new_key[b], new_key[a]
        new_key = ''.join(new_key)

        # Score the new decryption attempt
        decrypted_text = decrypt_with_key(ciphertext, new_key)
        score = quadgram_scorer.score(decrypted_text)

        # If the new key gives a better score, adopt it
        if score > best_score:
            best_score = score
            best_key = new_key
            best_decryption = decrypted_text
            print(f"Iteration {i}: New best score {best_score}")

    return best_key, best_decryption

# Run the decryption process
initial_key = initialize_key(ciphertext)
print(f"Initial Key: {initial_key}")
final_key, decrypted_text = hill_climb(ciphertext, initial_key)

# Save the final decrypted text and the key
with open('./Plain.txt', 'w') as f:
    f.write(decrypted_text)
with open('./subst.key', 'w') as f:
    f.write(final_key)

print("Decryption completed. Final key and plaintext saved.")
