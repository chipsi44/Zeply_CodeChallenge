from eth_account import Account
from COIN_AddGen.seed_generator import create_seed
import hashlib

def create_privateKey() : 
    #create the seed
    seed = create_seed()
    #create the private key with the seed
    hash_value = hashlib.sha256(seed.encode('utf-8')).digest()
    #return the private key and the seed
    return seed,hash_value.hex()

def ETH_address_generator(private_key) :
    if  private_key :
        #create address with the private key
        acct = Account.from_key(private_key)
        #return No Seed, the private key and the public address
        return(None,private_key,acct.address[2:])
    else : 
        #create the private key
        seed,private_key = create_privateKey()
        #create address with the private key
        acct = Account.from_key(private_key)
        #return the seed, the private key and the public address
        return(seed,private_key[2:],acct.address[2:])
        

