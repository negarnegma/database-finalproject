class User:
    def __init__(self, user_id, nasional_number, full_name, address, register_date):
        self.user_id = user_id
        self.nasional_number = nasional_number
        self.full_name = full_name
        self.address = address
        self.register_date = register_date

    def __str__(self):
        return "%s %s %s %s %s" % (self.user_id, self.nasional_number,
                                   self.full_name, self.address, self.register_date)
