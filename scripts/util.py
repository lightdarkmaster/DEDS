import unittest
from encryption import encrypt_file
from decryption import decrypt_file
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class TestEncryptFile(unittest.TestCase):
    def test_encrypt_file(self):
        # Test that the function returns a key
        key = encrypt_file('test_file.txt', 'encrypted_file.txt')
        self.assertIsNotNone(key)

    def test_encrypt_file_invalid_input(self):
        # Test that the function raises an error with invalid input
        with self.assertRaises(TypeError):
            encrypt_file(123, 'encrypted_file.txt')

class TestDecryptFile(unittest.TestCase):
    def test_decrypt_file(self):
        # Test that the function decrypts the file correctly
        key = encrypt_file('test_file.txt', 'encrypted_file.txt')
        decrypted_file = decrypt_file('encrypted_file.txt', 'decrypted_file.txt', key)
        self.assertIsNotNone(decrypted_file)

    def test_decrypt_file_invalid_input(self):
        # Test that the function raises an error with invalid input
        with self.assertRaises(TypeError):
            decrypt_file(123, 'decrypted_file.txt', 'key')

class TestFiledialog(unittest.TestCase):
    def test_filedialog_askopenfilename(self):
        # Test that the function returns a file path
        root = tk.Tk();
        file_path = filedialog.askopenfilename()
        self.assertIsNotNone(file_path)

    def test_filedialog_askopenfilename_cancel(self):
        # Test that the function returns None when cancelled
        root = tk.Tk();
        file_path = filedialog.askopenfilename()
        self.assertIsNone(file_path)

class TestMessagebox(unittest.TestCase):
    def test_messagebox_showinfo(self):
        # Test that the function shows a message box
        root = tk.Tk();
        messagebox.showinfo('Test', 'This is a test message')

    def test_messagebox_showerror(self):
        # Test that the function shows an error message box
        root = tk.Tk()
        messagebox.showerror('Test', 'This is a test error message')

class TestOs(unittest.TestCase):
    def test_os_path_exists(self):
        # Test that the function returns True for an existing path
        self.assertTrue(os.path.exists('test_file.txt'))

    def test_os_path_exists_invalid_input(self):
        # Test that the function raises an error with invalid input
        with self.assertRaises(TypeError):
            os.path.exists(123)

if __name__ == '__main__':
    unittest.main();