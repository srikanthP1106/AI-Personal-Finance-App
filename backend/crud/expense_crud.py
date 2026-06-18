from database.db import cursor, connection


def get_all_expense():

    cursor.execute("SELECT * FROM expense")

    return cursor.fetchall()