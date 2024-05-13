def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift_amount) %26) + ord('a'))
            else:
                encrypted_text += chr(((ord(char) - ord('A') + shift_amount) %26) + ord('A'))
        else:
            encrypted_text += char 
    return encrypted_text
def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)
choice = input("Enter 'E' for Encrypt and 'D' For Decrypt: ").upper()
if choice=='E':
    text = input("Text to encrypt: ")
    shift = int(input("Enter shift key: "))
    encrypted_text = caesar_cipher_encrypt(text, shift)
    print("Text Encrypted: ", encrypted_text)
elif choice=='D':
    text = input("Text To Decrypt: ")
    shift = int(input("Enter shift key: "))
    decrypted_text = caesar_cipher_decrypt(text, shift)
    print("Encrypted text: ", decrypted_text)
