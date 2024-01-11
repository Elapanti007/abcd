import os
import hashlib

def calculate_hash(file_path):
    if os.path.isfile(file_path):
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as file:
            buf = file.read()
            hasher.update(buf)
        return hasher.hexdigest()
    else:
        return None  # or handle directories differently
