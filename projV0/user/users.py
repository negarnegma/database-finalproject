import database as db
from user.user import User


def print_users():
    con = db.get_connection_func()

    cur = con.cursor()
    cur.execute("SELECT * from \"user\"")
    rows = cur.fetchall()

    for row in rows:
        p1 = User(row[0], row[1])
        print(p1.user_id, p1.full_name)

    print("Operation done successfully")
    con.close()
