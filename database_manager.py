import sqlite3 as sql

def listExtension():
    con = sql.connect("database/data_source.db")