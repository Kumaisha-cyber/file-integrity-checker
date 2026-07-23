# File Integrity Checker

A Python cybersecurity tool that monitors files and detects unauthorized changes using SHA-256 hashing.

## Features

- Detects modified files
- Detects new files
- Detects deleted files
- Uses SHA-256 cryptographic hashing
- Monitors multiple files
- Stores original file hashes in JSON format

## How It Works

1. The program calculates the SHA-256 hash of each file.
2. Original hashes are stored in `hashes.json`.
3. The program scans the files again.
4. It compares the current hash with the original hash.
5. It reports whether a file is unchanged, modified, new, or deleted.

## Project Structure

```text
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