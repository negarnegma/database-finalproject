import psycopg2


def get_connection_func():
    con = psycopg2.connect(database="projV0", user="postgres", password="36016778", host="127.0.0.1", port="5432")
    return con