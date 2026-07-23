# File Integrity Checker 🔐

A Python cybersecurity tool that monitors multiple files and detects unauthorized modifications, new files, and deleted files using SHA-256 cryptographic hashing.

## Features

- Calculates SHA-256 hashes of multiple files
- Detects unauthorized file modifications
- Detects newly added files
- Detects deleted files
- Compares original and current file hashes
- Stores original hashes in JSON format
- Provides clear security warnings

## Technologies Used

- Python
- SHA-256
- hashlib
- JSON
- os module

## Project Structure

file-integrity-checker/
│
├── file_integrity_checker.py
├── hashes.json
├── README.md
│
└── test_files/
    ├── file1.txt
    ├── file2.txt
    └── new_file.txt

## How It Works

1. The program calculates the SHA-256 hash of each file.
2. The original hashes are stored in `hashes.json`.
3. The program scans the files again.
4. Current hashes are compared with the original hashes.
5. The program detects whether a file is unchanged, modified, new, or deleted.

## Example Output

file1.txt → WARNING: File has been modified!

file2.txt → File is unchanged

new_file.txt → WARNING: New file detected!

file3.txt → WARNING: File has been deleted!

## How to Run

Run the following command:

```bash
python file_integrity_checker.py