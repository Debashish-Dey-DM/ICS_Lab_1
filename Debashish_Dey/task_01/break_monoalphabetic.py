import random
from ngram_score import ngram_score
from collections import Counter

# Load quadgram scorer and ciphertext
quadgramScorer = ngram_score('./english_quadgrams.txt')
with open('./Subst.txt', 'r') as f:
    ciphertext = f.read().replace("\n", " ")

ENGLISH_FREQ = 'ETAOINSHRDLCUMWFGYPBVKJXQZ' # English letter frequency

# Initialize key function by frequency analysis
def initialize_key(ciphertext):
    counts = Counter(char for char in ciphertext if char.isalpha()) # Count letter frequencies
    sortedChars = [char for char, _ in counts.most_common()] # Sort by frequency
    keyMap = {char: ENGLISH_FREQ[i] for i, char in enumerate(sortedChars[:len(ENGLISH_FREQ)])} # Map most frequent letters to English frequency
    unused = [c for c in ENGLISH_FREQ if c not in keyMap.values()] # Get unused letters
    return ''.join(keyMap.get(char, unused.pop(0) if unused else char) for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') # Fill in unused letters

# Decrypt function using a substitution key
def decrypt_with_key(text, key):
    return text.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", key))

# Hill climb function to optimize key
def hill_climb(ciphertext, key, max_iters=10000):
    bestKey, bestScore = key, quadgramScorer.score(decrypt_with_key(ciphertext, key)) # Initialize best key and score
    for _ in range(max_iters):
        newKey = list(bestKey)
        a, b = random.sample(range(26), 2) 
        newKey[a], newKey[b] = newKey[b], newKey[a] # Randomly swap two letters
        newDecrypt = decrypt_with_key(ciphertext, ''.join(newKey)) # Decrypt with new key
        score = quadgramScorer.score(newDecrypt) # Score new decryption
        if score > bestScore: # Update best key if new score is better
            bestKey, bestScore = ''.join(newKey), score
            print(f"New best score: {bestScore}") 
    return bestKey, decrypt_with_key(ciphertext, bestKey) # Return best key and decryption

# Calling the functions
initialKey = initialize_key(ciphertext)
finalKey, decryptedText = hill_climb(ciphertext, initialKey) 
with open('./Plain.txt', 'w') as f: f.write(decryptedText)
with open('./subst.key', 'w') as f: f.write(finalKey)


print("Decryption completed.")
