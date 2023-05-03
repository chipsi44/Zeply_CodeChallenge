from db_gestion import add_to_db
from COIN_AddGen.BTC_AddGen import bitcoin_address_generator

def generate_address(coin,private_key = False) :
    dic_coin_function = {
        'BTC' : lambda x : bitcoin_address_generator(x),
    }
    seed,private_key,public_key = dic_coin_function[coin](private_key)
    add_to_db(coin,public_key)

generate_address('BTC')