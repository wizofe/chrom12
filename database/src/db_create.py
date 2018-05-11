#!/usr/bin/env python3

"""
Program: Creating Database
File: db_create.py

Version: V1.0
Date: 08.05.18
Function: To create tables, indexes and insert information into database
Copyright (c) 2018, Jenny Su, Birkbeck, 2018
Author: Jenny Su
See the LICENSE.txt for licensing information

Database tier of implementation of a Chromosome (12) Browser
MSc. Bioinformatics, Birkbeck & UCL - BioComputing II
Taught by: Dr. Andrew C.R. Martin. UCL

Description:
============
This program contains functions that are used by Genbank_parser.py to create tables, indexes and
to insert information into database


Usage: Genbank_parser.py and middle layer


"""
#********************************************************************************************************
#Import libraries

import pymysql
import dbconnection

#*********************************************************************************************************

def create_tables(table_names, columns_data_list):
    """this function is used by Genbank_parser.py to create tables in the database
    """

    connection = dbconnection.getdbconnection()

    for i in range(len(table_names)):
        table_name = table_names[i]
        columns_data = columns_data_list[i]

        table_create_sql = "CREATE TABLE IF NOT EXISTS %s(" % table_name
        for column_info in columns_data:
            table_create_sql += " " + column_info[0] + " " + column_info[1] + ","

        table_create_sql = table_create_sql[:-1] + ")"
        

        cursor = connection.cursor()
        cursor.execute(table_create_sql)
        connection.commit()

    connection.close()
    

def create_indexes(index_info):
    """this function is used by Genbank_parser.py to create indexes in the database
    """
    
    
    connection = dbconnection.getdbconnection()

    for table in index_info.keys():
        
        sql = "ALTER TABLE %s ADD INDEX (%s)" %(table, ', '.join(index_info[table][1]))
        

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

    connection.close()


def insert_row(table_name, columns, values):
    """this function is used by Genbank_parser.py to insert information as row to table in the database
    """
    connection = dbconnection.getdbconnection()
    try:
        sql = 'INSERT INTO %s (%s) VALUES (' % (table_name, ", ".join(columns))

        for value in values:

            if type(value) == str:
                sql += '"%s"' % value + ", "
            else:
                sql += str(value) + ", "

        sql = sql[:-2] + ")"
        

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

    except pymysql.err.IntegrityError:
        pass

    connection.close()


def fetch_one(table_name, select_columns, where_dict):
    connection = dbconnection.getdbconnection()

    sql = 'SELECT %s FROM %s WHERE ' % (", ".join(select_columns), table_name)
    for key in where_dict.keys():
        if type(where_dict.get(key)) == str:
            sql += '%s = "%s" AND ' % (key, where_dict.get(key))

        else:
            sql += '%s = %s AND ' % (key, where_dict.get(key))

    sql = sql[:-5]
    
    cursor = connection.cursor()
    cursor.execute(sql)

    row = cursor.fetchone()

    connection.close()

    return row



