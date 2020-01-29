import psycopg2


def get_connection_func():
    con = psycopg2.connect(database="projV0", user="postgres", password="12", host="127.0.0.1", port="5432")
    return con


def insert_primery_data_offered_config(offered_configs):
    con = get_connection_func()
    cur = con.cursor()
    for config in offered_configs:
        cur.execute("insert into offered_config(os, ram, cores, disk, cpu_freq, bound_rate)"
                    "values (%s, %s, %s, %s, %s, %s) returning id",
                    (config.os, config.ram, config.cores, config.disk, config.cpu_freq,
                     config.bound_rate))

        row = cur.fetchone()
        config.offered_id = row[0]
    con.commit()
    con.close()
