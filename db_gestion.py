from COIN_AddGen.BTC_AddGen import bitcoin_address_generator
import psycopg2



def connect_to_db() :
    passconn = psycopg2.connect(
    host="dpg-ch90gb6kobicv5q9isjg-a.frankfurt-postgres.render.com",
    database="zeply_addressgenerator",
    user="zeply_addressgenerator_user",
    password="kw2FKkCzmEbra8kIxAWj73BHPaMBYk4v")

    return passconn

def add_to_db(coin,public_key) :
    passconn = connect_to_db()
    cursor = passconn.cursor()
    
    postgres_insert_query = """ INSERT INTO address_coin (coin, public_key) VALUES (%s,%s)"""
    record_to_insert = (coin,public_key)
    cursor.execute(postgres_insert_query, record_to_insert)
    passconn.commit()

    cursor.close()
    passconn.close()

def generate_address(coin,private_key = False) :
    dic_coin_function = {
        'BTC' : lambda x : bitcoin_address_generator(x),
    }
    seed,private_key,public_key = dic_coin_function[coin](private_key)
    add_to_db(coin,public_key)

generate_address("BTC")