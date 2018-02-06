# We need a module (library) that can communicate with the
# database server.
import pymysql.cursors
import pandas as pd
import json

# The database server is running somewhere in the network.
# I must specify the IP address (HW server) and port number
# (connection that SW server is listening on)
# Also, I do not want to allow anyone to access the database
# and different people have different permissions. So, the
# client must log on.
config = {
    'user': 'dbuser',
    'password': 'dbuser',
    'host': '10.0.1.4',
    'database': 'lahman2016',
    'raise_on_warnings': True,
    'charset': 'utf8'
}

# Connect
cnx = pymysql.connect(host='localhost',
                      user = 'dbuser',
                        password = 'dbuser',
                  db = 'lahman2016',
                       charset = 'utf8mb4',
                                 cursorclass = pymysql.cursors.DictCursor)


def run_query(q):
    print("Execution query = \n", q)
    with cnx.cursor() as cursor:
        # Create a new record
        cursor.execute(q)

    df_mysql = pd.read_sql(q, cnx)
    return df_mysql


def print_result(msg, pf):
    print(msg)
    print(pf)


def run_and_print_q(msg, q):
    r = run_query(q)
    print("\n", msg, "\n", r)


def run_query_to_d(q):
    with cnx.cursor() as cursor:
        # Create a new record
        cursor.execute(q)

    r = cursor.fetchall()
    return r
