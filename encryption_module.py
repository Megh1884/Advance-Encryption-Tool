from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

BLOCK_SIZE = 16  # AES block size

def pad(data):
    padding = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding] * padding)

def unpad(data):
    return data[:-data[-1]]

def encrypt_file(file_path, key):
    key = key.encode('utf-8')
    key = key[:32].ljust(32, b'\0')  # 32 bytes for AES-256

    with open(file_path, 'rb') as f:
        plaintext = f.read()

    plaintext = pad(plaintext)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)

    encrypted_data = base64.b64encode(iv + ciphertext)

    with open(file_path + ".enc", 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(file_path, key):
    key = key.encode('utf-8')
    key = key[:32].ljust(32, b'\0')

    with open(file_path, 'rb') as f:
        encrypted_data = base64.b64decode(f.read())

    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))

    output_path = file_path.replace('.enc', '.dec')
    with open(output_path, 'wb') as f:
        f.write(plaintext)
