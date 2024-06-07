import unittest
from src.encryption import encrypt, decrypt
from src.key_management import generate_key, save_key, load_key

class TestEncryption(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.key = generate_key()
        save_key(cls.key, filename='test_key.key')  # Save to a test-specific key file

    def test_encrypt_decrypt(self):
        original_text = 'Hello, World!'
        encrypted_text = encrypt(original_text, self.key)
        decrypted_text = decrypt(encrypted_text, self.key)
        
        # Check if the decrypted text is the same as the original text
        self.assertEqual(decrypted_text.decode('utf-8'), original_text)

    def test_key_save_load(self):
        loaded_key = load_key('test_key.key')
        self.assertEqual(loaded_key, self.key)

if __name__ == '__main__':
    unittest.main()
