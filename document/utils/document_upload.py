import os
from .document_hash import calculate_hash

def upload_document(file_path, uploads_folder):
    new_doc_hash = calculate_hash(file_path)
    for filename in os.listdir(uploads_folder):
        existing_file_path = os.path.join(uploads_folder, filename)
        if os.path.isfile(existing_file_path):
            existing_file_hash = calculate_hash(existing_file_path)
            if new_doc_hash == existing_file_hash:
                return False, "This document already exists."
    return True, "Document uploaded successfully."
