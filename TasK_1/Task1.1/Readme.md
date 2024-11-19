1st task :
A cipher text is given. For this lab you were provided a file called
Subst-Rijndael.crypt
Which contains the binary data of a text that has been encrypted TWICE.
1st layer : Monoalphabetic substitution
2nd layer : AES algiorthm in CBC mode

So the task is divided into two parts:
1.1. Decrypt the AES encrypted text
1.2. Decrypt the monoalphabetic substitution cipher text

1.1. Decrypt the AES encrypted text:
Information :
The AES encryyption used a weak key, where 128 bit key is used. Where the first 16bits were chosen and rest of the bits were set to 0. Here the iniitalization vector is the first block of the cipher text.

Solution notes & Hints:

- We have to bruite force Weak AES.
- We have to write a script to decrypt the AES encrypted text.
- We must find a critrion that allows us to know when we have found the correct key.
- We have to store the decrypted text in a file named "Subst.txt"
- We have to store the key in a file named "aes.key" as a hexademical text string.

Hints:

1. Notice that there are already many libraries that can help you to decrypt AES. as an example, you can use the "pycryptodome" library.
2. Take a look at Shannon's Entropy to find the correct key.

1.2. Decrypt the monoalphabetic substitution cipher text:
Information:

- We can't use the brute force method to decrypt the monoalphabetic substitution cipher text.
-
