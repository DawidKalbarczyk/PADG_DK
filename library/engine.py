import psycopg2

def dbConnect():
    connection = psycopg2.connect("dbname='postgres' user='postgres' password='postgres' port=5432")

    return connection