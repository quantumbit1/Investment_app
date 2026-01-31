#main.py
from core.mutual_fund import MutualFund
from core.transaction import Transaction
from services.nav_fetcher import NAVFetcher
from storage.repository import PortfolioRepository

DATA_FILE = "storage/portfolio.json"

FUNDS = {
    "SBI Gold Direct Plan - Growth": "119789",
    "HDFC Silver ETF FoF Direct - Growth": "150737"
}

def main():
    repo = PortfolioRepository()
    portfolio = repo.load(DATA_FILE)

    for name, code in FUNDS.items():
        if name not in portfolio:
            portfolio[name] = MutualFund(name, code)

    for fund in portfolio.values():
        nav, nav_date = NAVFetcher.get_latest_nav(fund.scheme_code)

        print(f"\n{fund.name}")
        print(f"NAV: ₹{nav} ({nav_date})")

        if input("Add transaction? (y/n): ").lower() == "y":
            date = input("Date: ")
            amount = float(input("Amount: "))
            purchase_nav = float(input("Purchase NAV: "))
            fund.add_transaction(Transaction(date, amount, purchase_nav))

        invested = fund.total_invested
        value = fund.current_value(nav)
        profit = fund.profit(nav)

        print(f"Invested: ₹{invested:.2f}")
        print(f"Value   : ₹{value:.2f}")
        print(f"P/L     : ₹{profit:.2f}")

    repo.save(portfolio, DATA_FILE)

if __name__ == "__main__":
    main()
