from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(input_path: str, output_path: str, key: bytes):
    """
    Decrypts an AES-encrypted file.

    Args:
        input_path (str): Path to the encrypted input file.
        output_path (str): Path to save the decrypted output file.
        key (bytes): AES key used during encryption.
    """
    with open(input_path, 'rb') as f_in:
        iv = f_in.read(16)  # First 16 bytes are the IV
        ciphertext = f_in.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_path, 'wb') as f_out:
        f_out.write(plaintext)
