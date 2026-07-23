import hashlib
import os
import json

folder_path = "test_files"
hash_file = "hashes.json"

with open(hash_file, "r") as file:
    original_hashes = json.load(file)

for filename in os.listdir(folder_path):

    file_path = os.path.join(folder_path, filename)

    with open(file_path, "rb") as file:
        current_hash = hashlib.sha256(file.read()).hexdigest()

    if current_hash == original_hashes[filename]:
        print(filename, "→ File is unchanged")
    else:
        print(filename, "→ WARNING: File has been modified!")