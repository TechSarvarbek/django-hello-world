import mysql.connector

# Connection details
config = {
    "host": "mysql-techsarvarbek.alwaysdata.net",
    "user": "360346_admin",
    "password": "0126s100",
    "database": "techsarvarbek_djangohellotech"
}

# Establish a connection
connection = mysql.connector.connect(**config)