from cryptography.fernet import Fernet
from verification import generate_checksum

def decrypt_file(encrypted_file_path):
    key = open("key.key", "rb").read()
    fernet = Fernet(key)
    with open(encrypted_file_path, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(encrypted_file_path.replace(".enc", ""), "wb") as dec_file:
        dec_file.write(decrypted)

def verify_integrity(original_file_path, checksum_file):
    original_checksum = generate_checksum(original_file_path)
    with open(checksum_file, "r") as file:
        stored_checksum = file.read()
    return original_checksum == stored_checksum

# Example usage:
decrypt_file("example.txt.enc")
is_valid = verify_integrity("example.txt", "checksum.txt")
print("Integrity Valid:", is_valid)