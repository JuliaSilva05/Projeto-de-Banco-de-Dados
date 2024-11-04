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
connection = create_db_connection("localhost","root","","webdriver")
execute_query(connection,use)

def ants():
    j = 1
    print('Reutilizar comandos anteriores')
    for i in anteriores:
        print('  ',j,' - ',i)
        
        j = j + 1
    print('   0 - Sair')
    op = int(input())
    if op == 0 or op >= j:
        return
    else:
        return anteriores[op-1]

def opcoes():
    print("1 - Ver comandos anteriores")

opcoes()
frase = input()
anteriores = []

while frase != "exit":
    res = read_query(connection,frase)
    
    if (res != None):
        for i in res:
            print(i)
        if frase.casefold() not in (com.casefold() for com in anteriores) and 'select'.casefold() in frase.casefold():
            anteriores.append(frase)
        elif 'select'.casefold() not in frase.casefold():
            execute_query(connection,frase)
    print("")
    frase = input()
    if frase == '1':
        frase = ants()
