import os
import random
import time

import psycopg2
from dotenv import load_dotenv

load_dotenv(verbose=True)

def hello_dummy():
    return "howdy"

    
def db_connect(connectStr):
    try:
        conn = psycopg2.connect(connectStr)
        return conn
    except Exception as e:
        print(e)
        return None


def add_meteo_data(conn):
    x = random.uniform(20.0, 35.0)
    cursor = conn.cursor()
    SQL = 'INSERT INTO meteo("temperature") values ({});'.format(x)
    print("Writing data.", flush=True)
    cursor.execute(SQL)
    cursor.close()
    conn.commit()


def get_connection_str():
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    connectStr = f"dbname='{DB_NAME}' user='{DB_USER}' host='{DB_HOST}' port={DB_PORT} password='{DB_PASSWORD}'"
    return connectStr


if __name__ == "__main__":

    conn = db_connect(get_connection_str())

    if conn is None:
        print("Could not connect to database.", flush=True)
        exit()

    sleepInterval = int(os.getenv("WRITE_INTERVAL_SECONDS", -1))
    if sleepInterval == -1:
        print("Interval not set or invalid. Using default of 30 seconds.", flush=True)
        sleepInterval = 30

    try:
        while True:
            add_meteo_data(conn)
            time.sleep(sleepInterval)
    except KeyboardInterrupt:
        pass

    conn.close()
