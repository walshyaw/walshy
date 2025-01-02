# ALEX WALSH
# Created on 01/02/2024. Last modified on 01/02/2024.
# https://github.com/walshyaw/

import random
import string

def main():
    is_running = True
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)

    while is_running:

        plain_text = input("Enter text to encrypt: ")

        cipher_text = encrypt(plain_text, chars, key)

        print(f"\nYour encrypted message is: {cipher_text}.")
        input("Press any key to decrpyt and see your original message...")

        plain_text = decrypt(cipher_text, chars, key)

        print(f"\nYour message has been decrypted back to: {plain_text}\n")

        temp = input("Encrypt new message? [Y, N]: ")

        while temp != "Y" and temp != "N":
            temp = input("Encrypt new message? [Y, N]: ")
        
        if temp == "N":
            is_running = False
            print()

def encrypt(plain_text, chars, key):
    cipher_text = ""
    for char in plain_text:
        cipher_text += key[chars.index(char)]
    
    return cipher_text

def decrypt(cipher_text, chars, key):
    plain_text = ""
    for char in cipher_text:
        plain_text += chars[key.index(char)]

    return plain_text

if __name__ == "__main__":
    main()