import encryption

username = input("Input target username:")
public_key = input("Input target public_key:")
encryption.store_public_key_file(public_key, username)