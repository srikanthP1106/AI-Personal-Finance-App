from database.db import cursor, connection


def get_all_income():

    cursor.execute("SELECT * FROM income")

    return cursor.fetchall()