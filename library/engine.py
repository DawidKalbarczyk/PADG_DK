import psycopg2

def dbConnect():
    connection = psycopg2.connect("dbname='postgresPADG' host='localhost' user='postgres' password='postgres' port=5432")

    return connection