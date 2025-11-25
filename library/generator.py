import psycopg2
def dbConnect():
    connectionConfig = """
                            host = 'localhost'
                            dbname= 'postgres'
                            user= 'postgres'
                            password= 'postgres'
                            port = 5432
                            """

    db = psycopg2.connect(connectionConfig)
    cursor = db.cursor()

    return cursor, db
