import os
import sqlite3

def get_connection():
    return sqlite3.connect("./database/sessao.db")
