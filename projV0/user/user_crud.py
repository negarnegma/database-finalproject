import hashlib
import uuid

import database.database as db
from user.user import User


# ###########wallet####################
def add_balance(user_id, amount):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("SELECT balance from wallet where owner_id = %s", (user_id,))
    row = cur.fetchone()
    cur.execute("update wallet set balance =%s where owner_id = %s", (row[0] + amount, user_id))
    con.commit()
    con.close()


def get_balance(user_id):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("SELECT balance from "
                "wallet where owner_id = %s", (user_id,))
    row = cur.fetchone()
    con.close()
    return row[0]

# ############register and login####################
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
    con.close()
    if row:
        hashed = row[0]
        salt = row[1]
        password = hashlib.sha512((password + salt).encode()).hexdigest()
        if hashed == password:
            return True
        return False
    else:
        return False


def get_all_users(size, page):
    con = db.get_connection_func()

    cur = con.cursor()
    cur.execute("select  id, nasional_number, fullname, address, register_date "
                "from \"user\" "
                "order by register_date desc "
                "limit %s offset %s", (size, size * (page - 1)))
    rows = cur.fetchall()

    users = []
    for row in rows:
        p1 = User(row[0], row[1], row[2], row[3], row[4])
        users.append(p1)
    con.close()

    return users


def is_admin(user_id):
    con = db.get_connection_func()

    cur = con.cursor()
    cur.execute("select  role "
                "from \"user\" "
                "where id = %s", (user_id,))
    row = cur.fetchone()

    con.close()

    return row[0] == 0  # todo check