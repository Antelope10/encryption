# RSA encryption

Output key-pairs in terminal by running generate_keys.py.

For either encryption or decryption, enter the necessary key into the first line of keys.txt (public key for encryption, private key for decryption), which is the only line that will be read by encrypt.py. Store any keys you want to remember in keys.txt as well. 

Enter text into in.txt and run encrypt.py with a command-line argument of "e" for encrypting the text or "d" for decrypting the text. The corresponding message will be encrypted or decrypted using the key in keys.txt and then appeneded to out.txt.
