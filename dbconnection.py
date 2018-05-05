# Copyright (c) 2018, Jenny Su
# See the LICENSE.txt for licensing information
#
# Database tier of implementation of a Chromosome (12) Browser
# MSc. Bioinformatics, Birkbeck & UCL - BioComputing II
# Taught by: Dr. Andrew C.R. Martin. UCL
import time

import pymysql
import pymysql.cursors


#   Create a connection object

dbserver = 'localhost'  # IP address of the MySQL database server
dbuser = 'root'         # User name of the databaseserver
dbpass = '1234'           # Password for the database user

newdbname = 'chromdb'  # Name of the database that is to be created
charset = 'utf8mb4'    # Character set
cursortype = pymysql.cursors.DictCursor


#   Connect to the server
server = pymysql.connect(host=dbserver,
                         user=dbuser,
                         password=dbpass,
                         charset=charset,
                         cursorclass=cursortype
                         )

#   Create the database
sql_statement = 'CREATE DATABASE IF NOT EXISTS ' + newdbname
cursor = server.cursor()
cursor.execute(sql_statement)


#    Function to return a database connection.
def getdbconnection():
    #   Connection arguments can be changed.
    while True:
        try:
            connection = pymysql.connect(host=dbserver,
                                         user=dbuser,
                                         password=dbpass,
                                         db=newdbname,
                                         charset=charset,
                                         cursorclass=cursortype)
            return connection
        except pymysql.err.OperationalError:
            print("sleeping")
            time.sleep(10)
