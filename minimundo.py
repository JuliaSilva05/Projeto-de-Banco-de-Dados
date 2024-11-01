import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")



use = "USE webdriver;"
select_usuario = "SELECT * FROM usuario;"
select_arquivo = "SELECT * FROM arquivo;"
connection = create_db_connection("localhost","carlos","1234","webdriver")
execute_query(connection,use)
res1 = read_query(connection,select_usuario)
res2 = read_query(connection,select_arquivo)

for i in res1:
    print(i)
print("")
for i in res2:
    print(i)
