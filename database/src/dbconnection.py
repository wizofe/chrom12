#!/usr/bin/env python3

"""
Program: Database connection
File: dbconnection.py

Version: V1.0
Date: 22.04.18
Function: A utility module to connect to the database and to define the getConnection() function to return a connection.
Copyright (c) 2018, Jenny Su, Birkbeck, 2018
Author: Jenny Su
See the LICENSE.txt for licensing information

Database tier of implementation of a Chromosome (12) Browser
MSc. Bioinformatics, Birkbeck & UCL - BioComputing II
Taught by: Dr. Andrew C.R. Martin. UCL

Description:
============
This program connects to MySQL database from Python using PyMySQL Connector/Python API and is used by Genbank.parser.py
to establish connection. 

Usage: for Genbank_parser.py

"""
#****************************************************************
#Import libraries
import time
import pymysql
import pymysql.cursors


#   Create a connection object. Parameters can be changed to suit user

dbserver = 'hope'          # IP address of the MySQL database server
dbuser =   'sj004'         # User name of the databaseserver
dbpass =   'sj004'         # Password for the database user

newdbname = 'sj004'   # Name of the database that is to be created
charset = 'utf8mb4'     # Character set
cursortype = pymysql.cursors.DictCursor

# For bbk student account,  we dont have access privilege to create new database on Hope server,
# so, we will create tables in existing user database
# For user wanting to create database on to another server, the followiing script can be enable and executed.  
#   Connect to the server
#server = pymysql.connect(host=dbserver,
                         #user=dbuser,
                         #password=dbpass,
                         #charset=charset,
                         #cursorclass=cursortype
                         #)

#   Create the database
#sql_statement = 'CREATE DATABASE IF NOT EXISTS ' + newdbname
#cursor = server.cursor()
#cursor.execute(sql_statement)


def getdbconnection():
    """ Function returns a database connection
    """

    while True:
        try:
            connection = pymysql.connect(host=dbserver,
                                         port=3306,
                                         user=dbuser,
                                         password=dbpass,
                                         db=newdbname,
                                         charset=charset,
                                         cursorclass=cursortype)
            return connection
        except pymysql.err.OperationalError:
            print("sleeping")
            time.sleep(10)
