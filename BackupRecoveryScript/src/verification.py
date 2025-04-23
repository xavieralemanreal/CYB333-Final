import hashlib

def generate_checksum(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def save_checksum(file_path, checksum_file):
    checksum = generate_checksum(file_path)
    with open(checksum_file, "w") as file:
        file.write(checksum)

# Example usage:
save_checksum("example.txt", "checksum.txt")