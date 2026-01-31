# Read/Write Json

import json
from core.transaction import Transaction
from core.mutual_fund import MutualFund

class PortfolioRepository:
    def load(self,file_path):
        # portfolio is a dict of mutual funds
        portfolio = {}
        try:
            with open(file_path,'r') as f:
                # here data is a dict of fund name and its details like scheme_code and transactions 
                data = json.load(f)

            for name,info in data.items():
                fund = MutualFund(name,info['scheme_code'])
                for t in info['transactions']:
                    transaction = Transaction(t['date'],t['amount'],t['nav'])
                    fund.add_transactions(transaction)

                portfolio[name] = fund
        except FileNotFoundError:
            pass
        return portfolio

    def save(self,portfolio,file_path):
        data = {}
        for fund in portfolio.values():
            data[fund.name] = {
                "scheme_code": fund.scheme_code,,
                "transactions" : [vars(t) for t in fund.Transactions]
            }

        with open(file_path,'w') as f:
            json.dump(data,f,indent=4)