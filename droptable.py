#!/usr/bin/env python

import pymysql
import re
import sys

def deletetables():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='kaixin001')
    cursor = conn.cursor()
    cursor.execute('show databases')
    dbs = list(cursor.fetchall())
    dbs = [x[0] for x in dbs if 'kx_football_' in x[0]]
    for x in dbs:
        conn.select_db(x)    
        cursor.execute('show tables')
        tables = list(cursor.fetchall())
        for t in tables:
            table = re.match(r"kx_football_.*_log_2017_.*", t[0])
            if not table is None:
                cursor.execute('drop table %s' %table.group())
    cursor.close()
    conn.close()

deletetables()

