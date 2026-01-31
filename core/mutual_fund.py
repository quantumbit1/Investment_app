# Fund Math

class MutualFund:
    def __init__(self,name,scheme_code):
        self.name = name
        self.scheme_code = scheme_code
        self.transactions = []

    def add_transactions(self,transaction):
        self.transactions.append(transaction)

    #@property is used to define a method as a attribute so that we don't need to call it 
    # with fund.total_units() instead we can call it with fund.total_units
    # This is useful when we want to calculate a value on the fly based on other attributes 
    # and not store it as a separate 
    @property
    def total_units(self):
        return sum(t.units for t in self.transactions)
    
    @property
    def total_invested(self):
        return sum(t.amount for t in self.transactions)
    
    def current_value(self,nav):
        # NOTE: toal_units is working likea attribute and not as a method and hence we don't use () though internally it is a method
        return self.total_units*nav
    
    def profit(self,nav):
        return self.current_value(nav) - self.total_invested