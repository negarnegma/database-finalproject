import hashlib
import uuid

import database as db
from user.user import User


def register_user(nasional_number, fullname, address, password):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512((password + salt).encode()).hexdigest()

    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("insert into registering_users_view (nasional_number, fullname, address, pass, salt)"
                "values (%s,%s,%s,%s,%s)", (nasional_number, fullname, address, hashed_password, salt))
    con.commit()
    con.close()


def login_user(nasional_number, password):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("SELECT pass, salt from registering_users_view where nasional_number = %s", (nasional_number,))
    row = cur.fetchone()
    if row:
        hashed = row[0]
        salt = row[1]
        password = hashlib.sha512((password + salt).encode()).hexdigest()
        if hashed == password:
            return True
        return False
    else:
        return False


def print_users():
    con = db.get_connection_func()

    cur = con.cursor()
    cur.execute("SELECT * from \"user\"", )
    rows = cur.fetchall()

    for row in rows:
        p1 = User(row[0], row[1])
        print(p1.user_id, p1.full_name)

    print("Operation done successfully")
    con.close()
