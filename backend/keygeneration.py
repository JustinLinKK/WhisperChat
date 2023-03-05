import encryption

private_key,public_key = encryption.generate_key_pairs()


encryption.store_private_key_file(private_key)
encryption.store_public_key_file(public_key, "localhost")


