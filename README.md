# File Integrity Checker 🔐

A Python cybersecurity tool that detects file modifications using SHA-256 hashing.

## Features

- Calculates SHA-256 hash of a file
- Detects unauthorized file modifications
- Compares original and current file hashes
- Displays SAFE or COMPROMISED status

## Technologies Used

- Python
- SHA-256
- hashlib

## How to Run

Run the following command:

python file_integrity_checker.py

Then enter the file name:

test.txt

## How It Works

The program creates an original SHA-256 hash of the file.

After the file is modified, the program creates a new SHA-256 hash.

If both hashes are the same:

FILE INTEGRITY: SAFE

If the hashes are different:

FILE INTEGRITY: COMPROMISED

## Cybersecurity Concepts

- File Integrity Monitoring
- Cryptographic Hashing
- SHA-256
- Data Integrity
- Tamper Detection