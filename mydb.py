#installing mqsql
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Harsh25@'
)

# prepare a cursor object 
cursorObject = dataBase.cursor()

# Cretae a database
cursorObject.execute('CREATE DATABASE SyncFusion')

print('Donee!')