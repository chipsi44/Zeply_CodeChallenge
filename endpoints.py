from data_management.db_gestion import add_to_db, select_all, select_specified_id
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
    
    #Verify the coin
    if coin not in dic_coin_function.keys() :
        raise Exception("Sorry, coin not recognized")
    #use the function in the dictionary with the chosen coin
    seed,private_key,public_address = dic_coin_function[coin](private_key)

    #
    #Just a bit of help for the dev the intersting part is the return ! 
    print(f"Private key, KEEP THIS FOR YOU : {private_key}")
    print(f"SEED, KEEP THIS FOR YOU : {seed}")
    print(f'Public address : {public_address}')

    #add the data to the db
    add_to_db(coin,public_address)

    return (seed,private_key,public_address)
def list_address() :
    all_record = select_all('address_coin')
    return all_record

def retrieve_address(id) :
    my_address = select_specified_id("address_coin",id)
    return my_address[0]