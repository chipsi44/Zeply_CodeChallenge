from db_gestion import add_to_db
from COIN_AddGen.BTC_AddGen import bitcoin_address_generator
from COIN_AddGen.ETH_AddGen import ETH_address_generator

def generate_address(coin,private_key = False) :
    '''
    Want to add another coin? No problem!
    Add your coin to the dictionary and link it to your function.

    Your function should be created in a file named COIN_addGen.py (replace COIN with your coin) in the directory COIN_AddGen. 
    It should return the seed, the private key (hex without "Ox"), and the public address.

    If no seed is provided in your library, you can use our seed generator to create a private key with the new seed generated.
    If you provide the private key, then the seed is not needed. (Can be return as None)
    '''

    dic_coin_function = {
        'BTC' : lambda x : bitcoin_address_generator(x),
        'ETH' : lambda x : ETH_address_generator(x)
    }

    #use the function in the dictionary with the chosen coin
    seed,private_key,public_address = dic_coin_function[coin](private_key)

    #You can modify this part to output them on your website for example
    print(f"Private key, KEEP THIS FOR YOU : {private_key}")
    print(f"SEED, KEEP THIS FOR YOU : {seed}")
    print(f'Public address : {public_address}')

    #add the data to the db
    add_to_db(coin,public_address)

