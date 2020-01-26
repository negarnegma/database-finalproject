import database.database as db
from resources.snapshot import Snapshot
from resources import resources_crud
import time


def add_snapshot(user_id, user_config_id, size):
    if not (resources_crud.owns(user_id, user_config_id)):
        raise Exception('access denied')

    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("insert into \"snapshot\"(create_date, size, user_config_id)"
                "values (%s, %s, %s)",
                (time.time(), size, user_config_id))

    con.commit()
    con.close()


def get_snapshots(user_config_id):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("select id, create_date, size, user_config_id from \"snapshot\" "
                "where user_config_id = %s ",
                (user_config_id,))
    rows = cur.fetchall()

    snapshots = []
    for row in rows:
        p1 = Snapshot(row[0], row[1], row[2], row[3])
        snapshots.append(p1)

    con.close()

    return snapshots
