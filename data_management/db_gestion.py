import psycopg2

'''
Note: This could have been transformed into OOP, but since we only use one database, I don't see the importance of doing it. 
If we were using multiple databases, the use of OOP could have been a great idea.
'''

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

def select_all(table_name) : 
    connection = connect_to_db()
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT * FROM " + table_name

    cursor.execute(postgreSQL_select_Query)

    coin_address_row = cursor.fetchall()
    cursor.close()
    connection.close()

    return coin_address_row

def select_specified_id(table_name,id) : 
    connection = connect_to_db()
    cursor = connection.cursor()
    #Error handling
    cursor.execute("SELECT id FROM " + table_name)
    id_values = [row[0] for row in cursor.fetchall()]
    if int(id) not in id_values:
        raise ValueError("id not in db")
    #Select the asked id
    postgreSQL_select_Query = "SELECT * FROM " + table_name + " WHERE id='" + str(id) +"';"
    #Execute the queries
    cursor.execute(postgreSQL_select_Query)
    coin_address_row = cursor.fetchall()
    #close everything and return the result
    cursor.close()
    connection.close()
    return coin_address_row