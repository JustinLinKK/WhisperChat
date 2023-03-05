# .venv\Scripts\activate.bat

# Created by Justin Lin in Mar.4th
# This file is to do the AS encryption to the message string
# Included generate keys, encryption and decryption function
# Install requirement before deployment
# Warning: the input bytes is a byte string so make sure encode that before the input
# Example:
# my_string = "Hello, world!"
# my_bytes = my_string.encode(encoding='utf-8')
# encrypt(my_bytes)
# We would use 'utf-8' as the encoder and decoder
#Key length would be 2048 bits 

# library import
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import json
import os


# Private Key Generation function
# Return private key and public key
def generate_key_pairs():
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key


# Private Key Store function
# Store the private key as private_key.pem
def store_private_key_file(private_key):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=None,
    )
    filename = "private_key.pem"
    if not os.path.exists(filename):
        with open(filename, "xb") as f:
            f.write(pem)
    else:
        print(f"File {filename} already exists.")


# Public Key Store function
# Store the public key as public_key.txt
def store_public_key_file(public_key, username):
    try:
        with open('public_keys.txt', 'r') as f:
            public_keys = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or can't be read as JSON, create an empty dictionary
        public_keys = {}

    # Add the new public key and username to the dictionary
    public_keys[username] = public_key.decode()

    # Write the updated dictionary to the file
    with open('public_keys.txt', 'w') as f:
        json.dump(public_keys, f)


# Private Key reading function
# Read the private key and return
# Input is the file name string of the private key, should be a pem file
def read_private_key():
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(), password=None, backend=default_backend()
        )

    return private_key


# Public Key reading function
# Read the public key and return
# Input is the file name string of the public key, should be a txt file
def read_public_key(username):

    try:
        with open('public_keys.txt', 'r') as f:
            public_keys = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or can't be read as JSON, return 1
        return 1

    if username in public_keys:
        # If the username exists in the dictionary, return the corresponding value
        public_key = public_keys[username]
        return public_key.encode()
    else:
        # If the username doesn't exist, return 2
        return 2


# Encryption function
# Input the message and return the encrypted message
# Warning: the input is a byte string so make sure encode that before the input
# Example:
# my_string = "Hello, world!"
# my_bytes = my_string.encode(encoding='utf-8')
# encrypt(my_bytes)
# We would use 'utf-8' as the encoder and decoder
# SHA256 is used to protect the message from modify
def encrypt(input_string: bytes, public_key):
    encrypted_message = public_key.encrypt(
        input_string,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    return encrypted_message


# decryption function
# Input the message and return the decrypted message
# Warning: the input is a byte string so make sure encode that before the input
# Example:
# my_string = "Hello, world!"
# my_bytes = my_string.encode(encoding='utf-8')
# encrypt(my_bytes)
# We would use 'utf-8' as the encoder and decoder
# SHA256 is used to protect the message from modify


def decrypt(encrypted_message, private_key):
    original_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    return original_message
