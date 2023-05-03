import psycopg2

def connect_to_db() :
    #Connection to my data base, I created a PostgreSQL one hosted on render.com but of course this can be changed. 
    passconn = psycopg2.connect(
    host="dpg-ch90gb6kobicv5q9isjg-a.frankfurt-postgres.render.com",
    database="zeply_addressgenerator",
    user="zeply_addressgenerator_user",
    password="kw2FKkCzmEbra8kIxAWj73BHPaMBYk4v")

    # return the connector
    return passconn

def add_to_db(coin,public_key) :
    #make the connection and create the cursor
    passconn = connect_to_db()
    cursor = passconn.cursor()
    
    #Create the queries to insert the data in the db 
    postgres_insert_query = """ INSERT INTO address_coin (coin, public_key) VALUES (%s,%s)"""
    record_to_insert = (coin,public_key)
    #execute and commit the queries
    cursor.execute(postgres_insert_query, record_to_insert)
    passconn.commit()

    #close the connection
    print("Address committed into the DB")
    cursor.close()
    passconn.close()

