import database.database as db
from resources.ssh import SSH
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
