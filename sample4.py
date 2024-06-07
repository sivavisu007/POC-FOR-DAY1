import hashlib


def calculate_file_hash(file_path, algorithm='sha256'):
    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        # Create a hash object using the specified algorithm
        hash_object = hashlib.new(algorithm)

        # Read the file in chunks to conserve memory
        for chunk in iter(lambda: f.read(4096), b''):
            hash_object.update(chunk)

    # Get the hexadecimal representation of the hash
    file_hash = hash_object.hexdigest()
    return file_hash


# Example usage
file_path = r'C:\Users\sivav\OneDrive\Documents\resume\Coverletter.pdf'  # Add 'r' before the string to treat it as a raw string
hash_value = calculate_file_hash(file_path)
print(f"The hash of {file_path} is: {hash_value}")
