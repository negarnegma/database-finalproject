import database.database as db
from resources.Offered import Offered
from resources.Ordered import Ordered
from resources.SSH import SSH
from user import user_crud


# ###########admin (offered) configs####################
def add_offered_resource(user_id, offered_config):
    if not (user_crud.is_admin(user_id)):
        raise Exception('access denied')

    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("insert into offered_config(os, ram, cores, disk, cpu_freq, bound_rate)"
                "values (%s, %s, %s, %s, %s, %s)",
                (offered_config.os, offered_config.ram, offered_config.cores,
                 offered_config.disk, offered_config.cpu_freq, offered_config.bound_rate))

    con.commit()
    con.close()


def get_offered_resources():
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("select id, os, ram, cores, disk, cpu_freq, bound_rate"
                " from offered_config ")

    rows = cur.fetchall()

    offers = []
    for row in rows:
        p1 = Offered(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        offers.append(p1)

    con.close()

    return offers


def update_offered_resource(user_id, offered_id, new_offered):
    if not (user_crud.is_admin(user_id)):
        raise Exception('access denied')

    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute(
        "update offered_config set os = %s ,  ram = %s ,  cores = %s , "
        " disk = %s ,  cpu_freq = %s ,  bound_rate = %s "
        "where id = %s ",
        (new_offered.os, new_offered.ram, new_offered.cores,
         new_offered.disk, new_offered.cpu_freq, new_offered.bound_rate,
         offered_id))

    con.commit()
    con.close()


# ###########user (ordered) configs####################
def add_user_resource(user_id, ordered):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute(
        "insert into user_config (os, ram, cores, disk, cpu_freq, bound_rate,"
        " ssh_id, owner_id, offered_config_id)"
        "values (%s, %s, %s, %s, %s, %s,%s, %s, %s)",
        (ordered.os, ordered.ram, ordered.cores,
         ordered.disk, ordered.cpu_freq, ordered.bound_rate,
         ordered.ssh_id, user_id, ordered.offered_config_id))

    con.commit()
    con.close()


def get_user_resources(user_id):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute(
        "select id, os, ram, cores, disk, cpu_freq, bound_rate,"
        " ssh_id, owner_id, daily_cost, offered_config_id"
        " from user_config "
        " where owner_id = %s ",
        (user_id,))

    rows = cur.fetchall()

    ordered = []
    for row in rows:
        p1 = Ordered(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        ordered.append(p1)

    con.close()

    return ordered


def get_user_resource_info(user_id, ordered_id):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute(
        "select id, os, ram, cores, disk, cpu_freq, bound_rate,"
        " ssh_id, owner_id, daily_cost, offered_config_id"
        " from user_config "
        " where owner_id = %s and id = %s ",
        (user_id, ordered_id))

    row = cur.fetchone()
    p1 = Ordered(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])

    con.close()

    return p1


def update_user_resource(user_id, ordered_id, new_ordered):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute(
        "update user_config set os = %s ,  ram = %s ,  cores = %s , "
        " disk = %s ,  cpu_freq = %s ,  bound_rate = %s ,"
        "  ssh_id = %s ,  offered_config_id = %s"
        "where id = %s and owner_id = %s",
        (new_ordered.os, new_ordered.ram, new_ordered.cores,
         new_ordered.disk, new_ordered.cpu_freq, new_ordered.bound_rate,
         new_ordered.ssh_id, new_ordered.offered_config_id,
         ordered_id, user_id))

    con.commit()
    con.close()


# ###########SSH####################
def add_ssh(user_id, ssh):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("insert into ssh(name, content, owner_id)"
                "values (%s, %s, %s)",
                (ssh.name, ssh.content, user_id))

    con.commit()
    con.close()


def get_all_ssh(user_id):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("select id, name, content from ssh"
                "where  owner_id = %s",
                (user_id,))
    rows = cur.fetchall()

    sshs = []
    for row in rows:
        p1 = SSH(row[0], row[1], row[2])
        sshs.append(p1)

    con.close()

    return sshs


# ######################################333
def owns(user_id, user_config_id):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("select id from user_config "
                "where id = %s and owner_id = %s",
                (user_config_id, user_id))

    row = cur.fetchone()
    con.close()
    return row
