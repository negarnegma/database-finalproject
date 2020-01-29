import database.database as db
import datetime
import time
import psycopg2
from tkinter import *

# ###########tickets####################
from ticket.ticket import Ticket


def add_ticket(user_id, content):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("insert into ticket(owner_id, content, c_date,  status, first_ticket_id, \"order\")"
                " values (%s, %s, %s, %s, %s, %s)",
                (user_id, content, psycopg2.TimestampFromTicks(time.time()), 0, None, 0))

    con.commit()
    con.close()


def answer_ticket(user_id, answer, last_ticket_id):
    # if not (user_crud.is_admin(user_id)):
    #     raise Exception('access denied')
    con = db.get_connection_func()
    cur = con.cursor()
    # cur.execute("insert into ticket(owner_id, content, c_date,  status, first_ticket_id, \"order\")"
    #             " values (%s, %s, %s, %s, %s, %s)",
    #             (user_id, answer, psycopg2.TimestampFromTicks(time.time()), 1, last_ticket.first_ticket_id,
    #              last_ticket.order + 1))
    cur.execute("insert into ticket(owner_id, content, c_date,  status, first_ticket_id, \"order\")"
                " values (%s, %s, %s, %s, %s, %s)",
                (user_id, answer, psycopg2.TimestampFromTicks(time.time()), 1, last_ticket_id,
                  1))

    con.commit()
    con.close()


def get_all_user_tickets(ui, user_id):
    tickets = []
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute(
        "select id, owner_id, content, c_date, status  from ticket"
        " where  owner_id = %s and first_ticket_id is null ",
        (user_id,))
    rows = cur.fetchall()

    if rows is None:
        return

    for x in rows:
        p1 = Ticket(x[0], x[1], x[2], x[3], x[4], 0, 0)
        tickets.append(p1)

    con.close()
    # print all_user_tickets
    ui.textEdit_5.setText("")
    ui.textEdit_5.insertPlainText("  id   date                   content")
    for ticket in tickets:
        ui.textEdit_5.insertPlainText("\n  %2.2s   %21.21s  %s" %
                                      (ticket.ticket_id, ticket.c_date, ticket.content))
    # else:
    #     ui.textEdit_5.setText("")


def get_all_answers_for_a_ticket(ui, user_id, ticket_id):
    if ticket_id == 0:
        ui.textEdit_4.setText("")
        return None
    tickets = []
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("select id, owner_id, content, c_date, status, \"order\"  from ticket"
                " where id = %s",
                (ticket_id,))
    row = cur.fetchone()

    if row is None:
        return

    p1 = Ticket(row[0], row[1], row[2], row[3], row[4], 0, 0)
    tickets.append(p1)

    if p1.owner_id != user_id:
        ui.textEdit_4.setText("access denied!")
        return None

    cur.execute("select id, owner_id, content, c_date, status, \"order\"  from ticket"
                " where first_ticket_id = %s",
                (ticket_id,))
    rows = cur.fetchall()

    if rows is None:
        return

    for row in rows:
        p1 = Ticket(row[0], row[1], row[2], row[3], row[4], ticket_id, row[5])
        tickets.append(p1)

    con.close()

    # sorted(key=lambda x: x.order)

    # print all_answers_for_a_ticket
    ui.textEdit_4.setText("")
    ui.textEdit_4.insertPlainText("  id   date                   content")
    for ticket in tickets:
        ui.textEdit_4.insertPlainText("\n  %2.2s   %21.21s  %s" %
                                      (ticket.ticket_id, ticket.c_date, ticket.content))
    # else:
    #     ui.textEdit_4.setText("")


if __name__ == "__main__":
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("insert into ticket(owner_id, content, c_date,  status, first_ticket_id, \"order\")"
                " values (%s, %s, %s, %s, %s, %s)",
                (11, "hihi", psycopg2.TimestampFromTicks(time.time()), 0, None, 0))

    con.commit()
    con.close()
