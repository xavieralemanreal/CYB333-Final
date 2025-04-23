import os
import shutil
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def encrypt_file(file_path):
    key = open("key.key", "rb").read()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

def backup_file(file_path, backup_directory):
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    shutil.copy(file_path + ".enc", backup_directory)

# Example usage:
generate_key()
encrypt_file("example.txt")
backup_file("example.txt", "backup/")