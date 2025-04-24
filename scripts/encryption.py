from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import os

def encrypt_file(input_path: str, output_path: str, key: bytes = None) -> bytes:
    """
    Encrypts the file at input_path using AES and saves it to output_path.
    
    Args:
        input_path (str): Path to the input file to encrypt.
        output_path (str): Path to save the encrypted file.
        key (bytes): 16, 24, or 32 bytes AES key. If None, a random 32-byte key will be generated.
    
    Returns:
        bytes: The AES key used for encryption.
    """
    if key is None:
        key = get_random_bytes(32)  # AES-256

    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    with open(input_path, 'rb') as f_in:
        plaintext = f_in.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_path, 'wb') as f_out:
        f_out.write(iv + ciphertext)  # Prepend IV for decryption later

    return key
