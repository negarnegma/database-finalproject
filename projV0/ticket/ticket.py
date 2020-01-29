class Ticket:
    def __init__(self, ticket_id, owner_id, content, c_date, status, first_ticket_id,
                 order):
        self.ticket_id = ticket_id
        self.owner_id = owner_id
        self.content = content
        # self.responder_id = responder_id
        # self.answer = answer
        self.c_date = c_date
        self.status = status
        self.first_ticket_id = first_ticket_id
        self.order = order
