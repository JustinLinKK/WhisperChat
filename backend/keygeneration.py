import encryption

public_key, private_key = encryption.generate_key_pairs()


encryption.store_private_key_file(private_key)
encryption.store_public_key_file(public_key, "localhost")

username = input("Input target username:")
public_key = input("Input target public_key:")
