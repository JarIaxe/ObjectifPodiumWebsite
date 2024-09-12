from logging import debug
import psycopg2
from config import load_config

def connect(config):
    try:
        with psycopg2.connect(host=config['host'],database=config['database'], user=config['user'], password= config['password']) as conn:
            print("connected to the PostgreSQL server")
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        raise error

if __name__ == "__main__":
    config = load_config(filename="database.ini", section='PostgreSQL')
    connect(config)