import psycopg2

def dbConnect():
    connection = psycopg2.connect("dbname='postgres' host='localhost' user='postgres' password='postgres' port=5432")

    return connection