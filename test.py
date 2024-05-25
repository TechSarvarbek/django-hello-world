import psycopg2
from psycopg2 import sql

# Connection details
config = {
    "host": "postgresql-techsarvarbek.alwaysdata.net",
    "user": "techsarvarbek",
    "password": "0126s100",
    "dbname": "techsarvarbek_djangohellotech"
}

# Establish a connection
try:
    connection = psycopg2.connect(**config)
    print("Connection to PostgreSQL DB successful")
except Exception as error:
    print(f"Error: {error}")