import hashlib
import os

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


filename = input("Enter the file path: ")

if os.path.exists(filename):

    original_hash = calculate_hash(filename)

    print("\nOriginal SHA-256 Hash:")
    print(original_hash)

    print("\nNow modify the file if you want to test integrity.")
    input("Press Enter after modifying the file...")

    current_hash = calculate_hash(filename)

    print("\nCurrent SHA-256 Hash:")
    print(current_hash)

    if original_hash == current_hash:
        print("\nFILE INTEGRITY: SAFE")
        print("The file has not been modified.")

    else:
        print("\nFILE INTEGRITY: COMPROMISED")
        print("The file has been modified!")

else:
    print("File not found!")