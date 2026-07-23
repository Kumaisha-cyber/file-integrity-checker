import hashlib
import os
import json

folder_path = "test_files"
hash_file = "hashes.json"

with open(hash_file, "r") as file:
    original_hashes = json.load(file)

current_files = set(os.listdir(folder_path))
original_files = set(original_hashes.keys())

for filename in current_files:

    file_path = os.path.join(folder_path, filename)

    with open(file_path, "rb") as file:
        current_hash = hashlib.sha256(file.read()).hexdigest()

    if filename not in original_hashes:
        print(filename, "→ WARNING: New file detected!")

    elif current_hash == original_hashes[filename]:
        print(filename, "→ File is unchanged")

    else:
        print(filename, "→ WARNING: File has been modified!")

for filename in original_files - current_files:
    print(filename, "→ WARNING: File has been deleted!")