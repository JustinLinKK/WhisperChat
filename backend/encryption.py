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

# library import
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


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
def store_private_key_file(private_key, password: bytes):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password),
    )
    with open("private_key.pem", "wb") as f:
        f.write(pem)


# Public Key Store function
# Store the public key as public_key.pem
def store_public_key_file(public_key):
    pem = public_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    with open("public_key.pem", "wb") as f:
        f.write(pem)


# Private Key reading function
# Read the private key and return
# Input is the file name string of the private key, should be a pem file
def read_private_key(private_key_file, password_input: bytes):
    with open(private_key_file, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(), password=password_input, backend=default_backend()
        )

    return private_key


# Public Key reading function
# Read the public key and return
# Input is the file name string of the public key, should be a pem file
def read_public_key(public_key_file):
    with open(public_key_file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(), backend=default_backend()
        )

    return public_key


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
