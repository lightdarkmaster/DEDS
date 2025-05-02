import unittest
from encryption import encrypt_file
from decryption import decrypt_file
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from unittest import skip

class TestEncryptFile(unittest.TestCase):
    def test_encrypt_file(self):
        # Create a temporary test file
        with open('test_file.txt', 'w') as f:
            f.write('Sample content')

        # Encrypt the file
        key = encrypt_file('test_file.txt', 'encrypted_file.txt')
        self.assertIsNotNone(key)

        # Clean up
        os.remove('test_file.txt')
        os.remove('encrypted_file.txt')

    def test_encrypt_file_invalid_input(self):
        with self.assertRaises(TypeError):
            encrypt_file(123, 'encrypted_file.txt')

class TestDecryptFile(unittest.TestCase):
    def test_decrypt_file(self):
        # Prepare encryption
        with open('test_file.txt', 'w') as f:
            f.write('Sample content')

        key = encrypt_file('test_file.txt', 'encrypted_file.txt')

        # Decrypt the file
        decrypt_file('encrypted_file.txt', 'decrypted_file.txt', key)
        self.assertTrue(os.path.exists('decrypted_file.txt'))

        # Clean up
        os.remove('test_file.txt')
        os.remove('encrypted_file.txt')
        os.remove('decrypted_file.txt')

    def test_decrypt_file_invalid_input(self):
        with self.assertRaises(TypeError):
            decrypt_file(123, 'decrypted_file.txt', 'key')

@skip("Skipping GUI test in terminal environment")
class TestFiledialog(unittest.TestCase):
    def test_filedialog_askopenfilename(self):
        root = tk.Tk()
        root.withdraw()  # Hide main window
        file_path = filedialog.askopenfilename()
        self.assertIsNotNone(file_path)

    def test_filedialog_askopenfilename_cancel(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        self.assertIsNone(file_path)

@skip("Skipping GUI test in terminal environment")
class TestMessagebox(unittest.TestCase):
    def test_messagebox_showinfo(self):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo('Test', 'This is a test message')

    def test_messagebox_showerror(self):
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror('Test', 'This is a test error message')

class TestOs(unittest.TestCase):
    def test_os_path_exists(self):
        # Create a file for testing
        with open('test_file.txt', 'w') as f:
            f.write('Sample content')
        self.assertTrue(os.path.exists('test_file.txt'))
        os.remove('test_file.txt')

    def test_os_path_exists_invalid_input(self):
        with self.assertRaises(TypeError):
            os.path.exists(123)

if __name__ == '__main__':
    unittest.main(verbosity=2)
