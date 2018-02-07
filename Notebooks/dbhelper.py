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

# Connect
def get_connection():
    cnx = pymysql.connect(host='localhost',
                          user = 'dbuser',
                          password = 'dbuser',
                          db = 'lahman2016',
                          charset = 'utf8mb4',
                         cursorclass = pymysql.cursors.DictCursor)
    cnx.autocommit(True)
    return cnx


def run_query(q, result):
    print("Execution query = \n", q)

    cnx = get_connection()

    with cnx.cursor() as cursor:
        cursor.execute(q)
        cnx.commit()
        cnx.close()

    if (result):
        cnx = get_connection()
        df_mysql = pd.read_sql(q, cnx)
        cnx.commit()
        cnx.close()
        return df_mysql
    else:
        return True


def print_result(msg, pf):
    print(msg)
    print(pf)


def run_and_print_q(msg, q, result):
    r = run_query(q, result)
    print("\n", msg, "\n", r)


def run_query_to_d(q):
    cnx = get_connection()
    with cnx.cursor() as cursor:
        # Create a new record
        cursor.execute(q)

    r = cursor.fetchall()
    cnx.close()
    return r


#run_and_print_q("Hello", "INSERT INTO University.person (last_name, first_name) VALUES('Ferguson', 'Donald');", False)
