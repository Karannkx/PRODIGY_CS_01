# Caesar Cipher Encryption/Decryption Script

This Python script provides functionalities to encrypt and decrypt text using the Caesar Cipher technique.

## How to Use

1. Run the script in a Python environment.
2. Choose 'E' for Encryption or 'D' for Decryption.
3. If encrypting:
   - Enter the text to encrypt.
   - Input the shift key (an integer) to determine the encryption pattern.
4. If decrypting:
   - Enter the encrypted text.
   - Input the shift key used for encryption.
5. The script will output the encrypted or decrypted text accordingly.

## Functions

### `caesar_cipher_encrypt(text, shift)`

This function encrypts the given text using the Caesar Cipher technique with the specified shift.

- `text`: The text to encrypt.
- `shift`: The shift key, an integer indicating the number of positions to shift each character.

### `caesar_cipher_decrypt(text, shift)`

This function decrypts the given text using the Caesar Cipher technique with the specified shift.

- `text`: The text to decrypt.
- `shift`: The shift key used for encryption, which is reversed to decrypt the text.

## Example

```python
Enter 'E' for Encrypt and 'D' For Decrypt: E
Text to encrypt: Hello, World!
Enter shift key: 3
Text Encrypted:  Khoor, Zruog!
```

```python
Enter 'E' for Encrypt and 'D' For Decrypt: D
Text To Decrypt: Khoor, Zruog!
Enter shift key: 3
Encrypted text:  Hello, World!
```
