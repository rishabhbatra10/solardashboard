# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:49:44 2018

@author: Rishabh Batra
"""

""" This Code contains functions to diplay and create tables"""
import sqlite3, csv
from sqlite3 import error

def create_connection(db_file):
    """This creates the connection to the SQLite database specified by the db_file"""
    try:
        db_conn = sqlite3.connect(db_file)
        return db_conn
    except error as e:
        print (e)
    return None

def print_tables_list(db_conn):
    """This function display tables present in the DataBase"""
    cur = db_conn.cursor() # this defines the cursor
    res = cur.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
    for name in res:
        print(name[0])

def copying_csv(db_conn, table, file):
    cur = db_conn.cursor()
    
    with open('E://final_year_proj/Kartikay_Data/89_final.csv','rt') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    
        cur.execute("CREATE TABLE table (Time, Temperature, Eac_Today, Vpv, Ipv, Ppv, Vac, Iac, Pac, Fac, Eac_Total);") # use your column names here

        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['Time'], i['Temperature'], i['Eac_Today'], i['Vpv'], i['Ipv'], i['Ppv'], i['Vac'], i['Iac'], i['Pac'], i['Fac'], i['Eac_Total']) for i in dr]

    cur.executemany("INSERT INTO SN0005000043200089 (Time, Temperature, Eac_Today, Vpv, Ipv, Ppv, Vac, Iac, Pac, Fac, Eac_Total) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    db_conn.commit()
