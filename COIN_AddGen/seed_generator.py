import secrets

def create_seed() :
    # Generate a 32-byte random seed
    seed = secrets.token_bytes(32)
    # Convert the bytes to a hex string for storage
    seed_hex = seed.hex()
    # return the seed
    return seed_hex



