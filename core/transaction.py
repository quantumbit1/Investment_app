# On purchase

class Transaction:
    def __init__(self,date,amount,nav):
        self.date = date
        self.amount = amount
        self.nav = nav
        self.units = amount/nav
        