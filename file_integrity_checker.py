import hashlib


def calculate_hash(filename):

    sha256_hash = hashlib.sha256()

    with open(filename, "rb") as file:

        for byte_block in iter(
            lambda: file.read(4096),
            b""
        ):

            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()


filename = input(
    "Enter the file path: "
)

file_hash = calculate_hash(filename)

print("\nSHA-256 Hash:")
print(file_hash)
