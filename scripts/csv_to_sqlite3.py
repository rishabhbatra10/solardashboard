# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:46:23 2018

@author: Rishabh Batra
"""
import sqlite3, csv
"""Connecting to the sqlite DataBase """
conn = sqlite3.connect('E://final_year_proj/data.db')
cur = conn.cursor() #defining the cursor

def createTable(no):
    for i in range(no):
        cur.execute("CREATE TABLE t%s (col1,col2);" % i)

def addCsv('path', no):
    with open('path', 'rb') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['col1'], i['col2']) for i in dr]
    for i in range(no):
        cur.executemany("INSERT INTO t%s (col1, col2) VALUES (?, ?);" %i, to_db)