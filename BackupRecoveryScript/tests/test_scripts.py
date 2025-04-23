import unittest
from backup import encrypt_file, backup_file
from verification import generate_checksum
from restoration import decrypt_file, verify_integrity

class TestBackupRecovery(unittest.TestCase):
    def test_encryption_decryption(self):
        encrypt_file("test.txt")
        decrypt_file("test.txt.enc")
        self.assertTrue(verify_integrity("test.txt", "test_checksum.txt"))

    def test_checksum(self):
        checksum1 = generate_checksum("test.txt")
        checksum2 = generate_checksum("test.txt")
        self.assertEqual(checksum1, checksum2)

if __name__ == "__main__":
    unittest.main()