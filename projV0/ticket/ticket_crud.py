import database.database as db
from ticket.ticket import Ticket
import time


# ###########tickets####################
def add_ticket(user_id, question):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("insert into ticket(owner_id, question, answer_date,  status, first_ticket_id, order)"
                "values (%s, %s, %s, %s, %s, %s)",
                (user_id, question, time.time(), 0, 0, 0))

    con.commit()
    con.close()


def answer_ticket(user_id, answer, last_ticket):
    # if not (user_crud.is_admin(user_id)):
    #     raise Exception('access denied')
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("insert into ticket(owner_id, question, answer_date,  status, first_ticket_id, order)"
                "values (%s, %s, %s, %s, %s, %s)",
                (user_id, last_ticket.question, time.time(), 1, last_ticket.first_ticket_id,
                 last_ticket.order + 1))

    con.commit()
    con.close()


def get_all_user_tickets(user_id):
    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("select id, owner_id, question, answer_date, status  from ticket"
                "where  owner_id = %s and first_ticket_id = %s",
                (user_id, 0))
    rows = cur.fetchall()

    tickets = []
    for row in rows:
        p1 = Ticket(row[0], row[1], row[2], row[3], row[4], 0, 0)
        tickets.append(p1)

    con.close()

    return tickets


def get_all_answers_for_a_ticket(user_id, ticket_id):
    tickets = []

    con = db.get_connection_func()
    cur = con.cursor()
    cur.execute("select id, owner_id, question, answer_date, status, order  from ticket"
                "where  owner_id = %s and id = %s",
                (user_id, ticket_id))
    rows = cur.fetchall()
    for row in rows:
        p1 = Ticket(row[0], row[1], row[2], row[3], row[4], 0, 0)
        tickets.append(p1)

    cur.execute("select id, owner_id, question, answer_date, status, order  from ticket"
                "where  owner_id = %s and first_ticket_id = %s",
                (user_id, ticket_id))
    rows = cur.fetchall()
    for row in rows:
        p1 = Ticket(row[0], row[1], row[2], row[3], row[4], ticket_id, row[5])
        tickets.append(p1)

    con.close()

    return tickets